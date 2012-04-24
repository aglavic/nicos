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

"""CCR switch device classes."""

__version__ = "$Revision$"

from nicos.core import Moveable, Override
from nicos.taco import DigitalInput, DigitalOutput 

class DigitalOutput(Moveable):
    """Class for CCR box switches.

    """

    attached_devices = {
        'write':   	(DigitalOutput, 'TACO digital output device'),
        'feedback':   	(DigitalInput, 'TACO digital input device (feedback)'),
    }

    parameter_overrides = {
        'fmtstr': Override(default='%d'),
        'unit'  : Override(default='', mandatory=False),
    }

    def doStart(self, target):
        if (self.read() != target) :
            self._adevs['write'].start(1)

    def doRead(self):
        return self._adevs['feedback'].read()

