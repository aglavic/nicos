#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2012 by the NICOS contributors (see AUTHORS)
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
# Module authors:
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
# *****************************************************************************

"""NICOS test suite."""

__version__ = "$Revision$"

from os import path
from logging import ERROR, WARNING

from nicos import session
from nicos.sessions import Session
from nicos.utils.loggers import ColoredConsoleHandler, NicosLogger


class ErrorLogged(Exception):
    """Raised when an error is logged by NICOS."""


class TestLogHandler(ColoredConsoleHandler):
    def __init__(self):
        ColoredConsoleHandler.__init__(self)
        self._warnings = []
        self._raising = True

    def emit(self, record):
        if record.levelno >= ERROR and self._raising:
            if record.exc_info:
                # raise the original exception
                raise record.exc_info[1], None, record.exc_info[2]
            else:
                raise ErrorLogged(record.message)
        elif record.levelno >= WARNING:
            self._warnings.append(record)
        ColoredConsoleHandler.emit(self, record)

    def enable_raising(self, raising):
        self._raising = raising

    def warns(self, func, *args, **kwds):
        plen = len(self._warnings)
        func(*args, **kwds)
        return len(self._warnings) == plen + 1


class TestSession(Session):
    autocreate_devices = False

    def __init__(self, appname):
        Session.__init__(self, appname)
        self._mode = 'master'
        self.setSetupPath(path.join(path.dirname(__file__), 'setups'))

    def createRootLogger(self, prefix='nicos'):
        self.log = NicosLogger('nicos')
        self.log.parent = None
        self.testhandler = TestLogHandler()
        self.log.addHandler(self.testhandler)
        self._master_handler = None

TestSession.config.user = None
TestSession.config.group = None
TestSession.config.control_path = path.join(path.dirname(__file__), 'root')


session.__class__ = TestSession
session.__init__('test')
