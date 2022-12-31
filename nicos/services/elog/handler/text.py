#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2023 by the NICOS contributors (see AUTHORS)
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
#   Georg Brandl <g.brandl@fz-juelich.de>
#
# *****************************************************************************

"""The NICOS electronic logbook."""

from os import path

from nicos.services.elog.handler import Handler as BaseHandler
from nicos.services.elog.utils import create_or_open, formatMessagePlain


class Handler(BaseHandler):
    def __init__(self, log, plotformat):
        BaseHandler.__init__(self, log, plotformat)
        self.fd = None

    def close(self):
        if self.fd:
            self.fd.close()
            self.fd = None

    def handle_directory(self, time, data):
        BaseHandler.handle_directory(self, time, data)
        self.close()
        logfile = path.join(self.logdir, 'nicos_log.txt')
        self.fd = create_or_open(logfile)
        self.log.info('Opened new output in %s', logfile)

    def handle_message(self, time, message):
        formatted = formatMessagePlain(message)
        if not formatted or not self.fd:
            return
        self.fd.write(formatted.encode())
        self.fd.flush()
