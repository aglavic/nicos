#  -*- coding: utf-8 -*-
# *****************************************************************************
# Module:
#   $Id$
#
# Description:
#   Virtual NICOS test devices
#
# Author:
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
#   The basic NICOS methods for the NICOS daemon (http://nicos.sf.net)
#
#   Copyright (C) 2009 Jens Krüger <jens.krueger@frm2.tum.de>
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

"""Virtual devices for testing."""

__author__  = "$Author$"
__date__    = "$Date$"
__version__ = "$Revision$"

import time
import threading

from nicm import nicos, status
from nicm.motor import Motor
from nicm.coder import Coder


class VirtualMotor(Motor):
    parameters = {
        'initval': (0, True, 'Initial value for the virtual device.'),
        'speed': (0, False, 'Virtual speed of the device.'),
    }

    def doInit(self):
        self.__val = self.getPar('initval')
        self.__busy = False

    def doStart(self, pos):
        self.__busy = True
        if self.getSpeed() != 0:
            thread = threading.Thread(target=self.__moving, args=(pos,))
            thread.start()
        else:
            self.printdebug('moving to %s' % pos)
            self.__val = pos
            self.__busy = False

    def doRead(self):
        return self.__val

    def doStatus(self):
        if self.__busy:
            return status.BUSY
        return status.OK

    def __moving(self, pos):
        incr = self.getSpeed()
        delta = pos - self.read()
        steps = int(abs(delta) / incr)
        incr = delta < 0 and -incr or incr
        for i in range(steps):
            time.sleep(0.5)
            self.printdebug('thread moving to %s' % (self.__val + incr))
            self.__val += incr
        self.__val = pos
        self.__busy = False


class VirtualCoder(Coder):
    parameters = {
        'motor': ('', True, 'Device whose value to mirror.'),
    }

    def doInit(self):
        self._motor = nicos.get_device(self.getMotor())

    def doRead(self):
        return self._motor.read()

    def doStatus(self):
        return status.OK
