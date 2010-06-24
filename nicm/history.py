#  -*- coding: utf-8 -*-
# *****************************************************************************
# Module:
#   $Id$
#
# Description:
#   NICOS history managers
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

"""NICOS history managers."""

__author__  = "$Author$"
__date__    = "$Date$"
__version__ = "$Revision$"

import time

from nicm.device import Device
from nicm.scratchpad import ScratchPadConnection


class History(Device):
    """
    History manager base class.
    """


class LocalHistory(History):
    """
    A history manager that simply stores the history locally.
    """

    parameters = {
        'maxage': (float, 12, False,
                   'The maximum age of history entries in hours.'),
    }

    def doInit(self):
        self.__db = {}

    def put(self, dev, name, tstamp, value):
        self.__db.setdefault(dev.name, {}).\
                  setdefault(name, []).append((tstamp, value))

    def get(self, dev, name, fromtime, totime):
        history = self.__db.get(dev.name, {}).get(name, [])
        if not history:
            return None
        i1, i2 = None, None
        for i, (tstamp, _) in enumerate(history):
            if i1 is None and fromtime is not None and tstamp >= fromtime:
                i1 = i
            if i2 is None and totime is not None and tstamp >= totime:
                i2 = i
        return history[i1:i2]


class ScratchPadHistory(History):
    """
    A history manager that sends updates to ScratchPad.
    """

    parameters = {
        'server': (str, '', True,
                   '"host:port" of the ScratchPad instance to connect to.'),
        'prefix': (str, '', True, 'ScratchPad key prefix.'),
    }

    def doInit(self):
        try:
            host, port = self.server.split(':')
            self.__conn = ScratchPadConnection(self.prefix, host, int(port))
        except ValueError:
            host = self.server
            self.__conn = ScratchPadConnection(self.prefix, host)

    def put(self, dev, name, tstamp, value):
        self.__conn.tell(dev.name + '/' + name, value, tstamp)

    def get(self, dev, name, fromtime, totime):
        return None


class LogfileHistory(History):
    """
    A history manager that writes device values to a logfile.
    """

    parameters = {
        'basefilename': (str, '', True,
                         'Directory and base name for logfile names.'),
    }

    def doInit(self):
        self.__files = {}

    def doShutdown(self):
        for fd in self.__files.itervalues():
            fd.close()

    def put(self, dev, name, tstamp, value):
        if (dev.name, name) not in self.__files:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
            newname = '%s%s_%s_%s.log' % (self.basefilename, dev.name,
                                          name, timestamp)
            self.__files[dev.name, name] = open(newname, 'a')
        self.__files[dev.name, name].write('%s\t%s\n' % (tstamp, value))
        self.__files[dev.name, name].flush()

    def get(self, dev, fromtime, totime):
        return None
