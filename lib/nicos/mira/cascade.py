#  -*- coding: utf-8 -*-
# *****************************************************************************
# Module:
#   $Id$
#
# Author:
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
# NICOS-NG, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2011 by the NICOS-NG contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# *****************************************************************************

from __future__ import with_statement

"""Class for CASCADE detector measurement and readout."""

__author__  = "$Author$"
__date__    = "$Date$"
__version__ = "$Revision$"

import threading
from os import path
from time import sleep, time

import numpy as np

from nicos import session, status
from nicos.data import NeedsDatapath
from nicos.utils import existingdir, tupleof, oneof, dictof, \
     readFileCounter, updateFileCounter
from nicos.device import Measurable, Param, Override, Value
from nicos.errors import CommunicationError
from nicos.mira import cascadeclient


class CascadeDetector(Measurable, NeedsDatapath):

    parameters = {
        'server':   Param('"host:port" of the cascade server to connect to',
                          type=str, mandatory=True, preinit=True),
        'debugmsg': Param('Whether to print debug messages from the client',
                          type=bool, settable=True, default=False),
        'nametemplate': Param('Template for the data file names',
                              type=dictof(str, str),
                              default={'image': 'cascade_%05d.pad',
                                       'tof':   'cascade_%05d.tof'}),
        'roi':      Param('Region of interest, given as (x1, y1, x2, y2)',
                          type=tupleof(int, int, int, int),
                          default=(-1, -1, -1, -1), settable=True),
        'mode':     Param('Data acquisition mode (tof or image)',
                          type=oneof(str, 'tof', 'image'), settable=True),
        # XXX what about monitor preselection?
        'preselection': Param('Current preselection', unit='s',
                              settable=True, type=float),
    }

    parameter_overrides = {
        'fmtstr':   Override(default='roi %s, total %s, file %s'),
    }

    def doPreinit(self):
        self._client = cascadeclient.NicosClient()
        self.doReset()

    def doInit(self):
        self._datapath = None
        self._filenumber = -1
        self._lastfilename = '<none>'
        self._last_preset = self.preselection
        self._last_total = -1
        self._last_roi = -1
        self._dataprefix = (self.mode == 'image') and 'IMAG' or 'DATA'
        self._datashape = (self.mode == 'image') and (128, 128) or (128, 128, 128)
        self._xres, self._yres = (128, 128)
        self._tres = (self.mode == 'image') and 1 or 128
        self._measure = threading.Event()
        self._processed = threading.Event()
        self._processed.set()

        self._thread = threading.Thread(target=self._thread_entry)
        self._thread.setDaemon(True)
        self._thread.start()

    def doReset(self):
        self._client.disconnect()
        host, port = self.server.split(':')
        port = int(port)
        if not self._client.connecttohost(host, port):
            raise CommunicationError(self, 'could not connect to server')

    def _setDatapath(self, value):
        value = value[0]  # always use only first data path
        self._datapath = path.join(value, 'cascade')
        self._filenumber = readFileCounter(path.join(self._datapath, 'counter'))
        self._lastfilename = path.join(
            self._datapath, self.nametemplate[self.mode] % self._filenumber)

    def valueInfo(self):
        return Value(self.name + '.roi', unit='cts', type='counter',
                     errors='sqrt', active=self.roi != (-1, -1, -1, -1)), \
               Value(self.name + '.total', unit='cts', type='counter',
                     errors='sqrt'), \
               Value(self.name + '.file', type='info')

    def doWriteDebugmsg(self, value):
        self._client.SetDebugLog(value)

    def doShutdown(self):
        self._client.disconnect()

    def doStatus(self):
        if not self._client.isconnected():
            return status.ERROR, 'disconnected from server'
        elif self._measure.isSet():
            return status.BUSY, 'measuring'
        elif not self._processed.isSet():
            return status.BUSY, 'processing',
        return status.OK, 'idle'

    def doStart(self, **preset):
        if self._datapath is None:
            self._setDatapath(session.experiment.datapath)
        self._lastfilename = path.join(
            self._datapath, self.nametemplate[self.mode] % self._filenumber)
        self._filenumber += 1
        updateFileCounter(path.join(self._datapath, 'counter'), self._filenumber)
        self._processed.wait()
        self._processed.clear()
        try:
            if preset.get('t'):
                self.preselection = self._last_preset = preset['t']
        except:
            self._processed.set()
            raise
        self._measure.set()

    def doIsCompleted(self):
        return not self._measure.isSet() and self._processed.isSet()

    def doStop(self):
        reply = str(self._client.communicate('CMD_stop'))
        if reply != 'OKAY':
            raise CommunicationError(self, 'could not stop measurement: %s'
                                     % reply[4:])

    def doRead(self):
        return (self._last_roi, self._last_total, self._lastfilename)

    def _getconfig(self):
        cfg = self._client.communicate('CMD_getconfig')
        if cfg[:4] != 'CFG_':
            raise CommunicationError(self, 'could not get configuration : %s'
                                     % cfg[4:])
        return dict(v.split('=') for v in str(cfg[4:]).split(' '))

    def doReadMode(self):
        return self._getconfig()['mode']

    def doWriteMode(self, value):
        reply = self._client.communicate('CMD_config mode=%s' % value)
        if reply != 'OKAY':
            raise CommunicationError(self, 'could not set mode: %s' % reply[4:])
        self._dataprefix = (value == 'image') and 'IMAG' or 'DATA'
        self._datashape = (value == 'image') and (128, 128) or (128, 128, 128)
        self._tres = (value == 'image') and 1 or 128

    def doReadPreselection(self):
        return int(self._getconfig()['time'])

    def doWritePreselection(self, value):
        reply = self._client.communicate('CMD_config time=%s' % value)
        if reply != 'OKAY':
            raise CommunicationError(self, 'could not set measurement time: %s'
                                     % reply[4:])

    def _thread_entry(self):
        while True:
            try:
                # wait for start signal
                self._measure.wait()
                # start measurement
                reply = str(self._client.communicate('CMD_start'))
                if reply != 'OKAY':
                    raise CommunicationError(self, 'could not start '
                                             'measurement: %s' % reply[4:])
                started = time()
                # wait for completion of measurement
                while True:
                    sleep(0.2)
                    status = self._client.communicate('CMD_status')
                    if status == '':
                        raise CommunicationError(self, 'no response from server')
                    #self.printdebug('got status %r' % status)
                    status = dict(v.split('=')
                                  for v in str(status[4:]).split(' '))
                    if status.get('stop', '0') == '1':
                        break
                    data = self._client.communicate('CMD_readsram')
                    session.updateLiveData('<i4', self._xres, self._yres,
                                           self._tres, time() - started,
                                           buffer(data, 4))
                    # XXX should update counts
            except:
                self._lastfilename = '<error>'
                self.printexception('measuring failed')
                self._measure.clear()
                self._processed.set()
                continue
            self._measure.clear()
            try:
                # get final data including all events from detector
                data = self._client.communicate('CMD_readsram')
                if data[:4] != self._dataprefix:
                    raise CommunicationError(self, 'error receiving data from '
                                             'server: %s' % data[:4])
                buf = buffer(data, 4)
                # send final image to live plots
                session.updateLiveData('<i4', self._xres, self._yres,
                                       self._tres, self._last_preset, buf)
                # write to data file
                with open(self._lastfilename, 'w') as fp:
                    fp.write(buf)
                # determine total and roi counts
                # XXX temporary until self._client component can do this
                ar = np.ndarray(buffer=data, offset=4,
                                shape=self._datashape, order='F', dtype='<I4')
                self._last_total = int(long(ar.sum()))
                if self.roi != (-1, -1, -1, -1):
                    x1, y1, x2, y2 = self.roi
                    self._last_roi = int(long(ar[x1:x2, y1:y2].sum()))
                else:
                    self._last_roi = self._last_total
            except:
                self._lastfilename = '<error>'
                self.printexception('saving measurement failed')
            finally:
                self._processed.set()
