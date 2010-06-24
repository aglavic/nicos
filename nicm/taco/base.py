#  -*- coding: iso-8859-15 -*-
# *****************************************************************************
# Module:
#   $Id$
#
# Description:
#   NICOS TACO base classes
#
# Author:
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
#   The basic NICOS methods for the NICOS daemon (http://nicos.sf.net)
#
#   Copyright (C) 2009 Jens Kr�ger <jens.krueger@frm2.tum.de>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# *****************************************************************************

"""NICOS-TACO base classes."""

__author__  = "$Author$"
__date__    = "$Date$"
__version__ = "$Revision$"

import sys
import threading

import TACOStates
from TACOClient import TACOError

from nicm import status
from nicm.utils import tacodev
from nicm.errors import NicmError, ProgrammingError, CommunicationError


class TacoDevice(object):
    """Mixin class for TACO devices.

    Use it in concrete device classes like this:

        class Counter(TacoDevice, Countable):
            taco_class = IO.Counter

            # more overwritten methods

    i.e., put TacoDevice first in the base class list.
    """

    parameters = {
        'tacodevice': (tacodev, '', True, 'TACO device name.'),
        'tacotimeout': (float, 3, False,
                        'TACO client network timeout (in seconds).'),
        'tacolog': (bool, False, False, 'If true, log all TACO calls.'),
        # the unit isn't mandatory -- TACO usually knows it already
        'unit': (str, '', False, 'Unit of the device main value.'),
    }

    # the TACO client class to instantiate
    taco_class = None
    # whether to call deviceReset() if the initial switch-on fails
    taco_resetok = True
    # TACO device instance
    _dev = None

    def doPreinit(self):
        self.__lock = threading.Lock()

    def doInit(self):
        if self.tacolog:
            self._taco_guard = self._taco_guard_log
        if self.taco_class is None:
            raise ProgrammingError('missing taco_class attribute in class '
                                   + self.__class__.__name__)
        self._dev = self._create_client()

    def doVersion(self):
        return [(self.tacodevice,
                 self._taco_guard(self._dev.deviceVersion))]

    def doRead(self):
        return self._taco_guard(self._dev.read)

    def doStatus(self):
        state = self._taco_guard(self._dev.deviceState)
        if state in (TACOStates.ON, TACOStates.DEVICE_NORMAL):
            return status.OK
        return status.ERROR # or status.UNKNOWN?

    def doReset(self):
        self._taco_guard(self._dev.deviceReset)

    def doGetUnit(self):
        if 'unit' in self._params and self._params['unit']:
            return self._params['unit']
        unit = self._taco_guard(self._dev.unit)
        self._params['unit'] = unit
        return unit

    def doSetTacotimeout(self, value):
        self._params['tacotimeout'] = value
        if self._dev:
            self._taco_guard(self._dev.setClientNetworkTimeout, value)

    def doSetTacolog(self, value):
        value = bool(value)
        self._params['tacolog'] = value
        self._taco_guard = value and self._taco_guard_log or \
                           self._taco_guard_nolog
        # automatically set the loglevel to debug, otherwise taco log
        # messages won't be emitted
        self.loglevel = 'debug'

    # internal utilities

    def _create_client(self, devname=None, class_=None, resetok=None,
                       timeout=None):
        """
        Create a new TACO client and initialize the device in a
        consistent state, handling eventual errors.
        """

        if devname is None:
            devname = self.tacodevice
        if class_ is None:
            class_ = self.taco_class
        if resetok is None:
            resetok = self.taco_resetok
        if timeout is None:
            timeout = self.tacotimeout
        log = self.tacolog

        if log:
            self.printdebug('creating %s TACO device' % class_.__name__)

        try:
            dev = class_(devname)
        except TACOError, err:
            self._raise_taco(err, 'Could not connect to device %r' % devname)

        try:
            if timeout != 0:
                dev.setClientNetworkTimeout(timeout)
        except TACOError, err:
            self.printwarning('Setting TACO network timeout failed: '
                              '[TACO %d] %s' % (err.errcode, err))

        try:
            if dev.isDeviceOff():
                dev.deviceOn()
        except TACOError, err:
            self.printwarning('Switching TACO device %r on failed: '
                              '[TACO %d] %s' % (devname, err.errcode, err))
            try:
                if dev.deviceState() == TACOStates.FAULT:
                    if resetok:
                        dev.deviceReset()
                dev.deviceOn()
            except TACOError, err:
                self._raise_taco(err, 'Switching device %r on after '
                                 'reset failed' % devname)

        return dev

    def _taco_guard_log(self, function, *args):
        """Like _taco_guard(), but log the call."""
        self.printdebug('TACO call: %s%s' % (function.__name__, args))
        self.__lock.acquire()
        try:
            ret = function(*args)
        except TACOError, err:
            self._raise_taco(err)
        else:
            self.printdebug('TACO return: %s' % ret)
            return ret
        finally:
            self.__lock.release()

    def _taco_guard_nolog(self, function, *args):
        """Try running the TACO function, and raise a NicmError on exception."""
        self.__lock.acquire()
        try:
            return function(*args)
        except TACOError, err:
            self._raise_taco(err)
        finally:
            self.__lock.release()

    _taco_guard = _taco_guard_nolog

    def _taco_update_resource(self, resname, value):
        """Update a TACO resource, switching the device off and on."""
        self.__lock.acquire()
        try:
            if self._params['tacolog']:
                self.printdebug('TACO resource update: %s %s' %
                                (resname, value))
            self._dev.deviceOff()
            self._dev.deviceUpdateResource(resname, value)
            self._dev.deviceOn()
            if self._params['tacolog']:
                self.printdebug('TACO resource update successful')
        except TACOError, err:
            self._raise_taco(err)
        finally:
            self.__lock.release()

    def _raise_taco(self, err, addmsg=None):
        """Raise a suitable NicmError for a given TACOError instance."""
        tb = sys.exc_info()[2]
        code = err.errcode
        cls = NicmError
        if code == 2:
            # client call timeout
            cls = CommunicationError
        elif 401 <= code < 499:
            # error number 401-499: database system error messages
            cls = CommunicationError
        # TODO: add more cases
        msg = '[TACO %d] %s' % (err.errcode, err)
        if addmsg is not None:
            msg = addmsg + ': ' + msg
        raise cls(self, msg), None, tb
