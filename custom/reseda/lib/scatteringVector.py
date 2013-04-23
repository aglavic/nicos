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
#   Aleks Wischolit <aleks.wischolit@frm2.tum.de>
#
# *****************************************************************************

"""Calculation of Q vector from wavelength and scattering angle."""

import math

from nicos.core import Readable, Override, status


class ScatteringVector(Readable):

    attached_devices = {
        'wavelength': (Readable, 'to calculate the wavelength'),
        'twotheta': (Readable, 'Scattering angle')
    }

    parameter_overrides = {
        'unit':   Override(mandatory=False, default='1/A')
    }

    def doRead(self, maxage=0):
        Lambda = self._adevs['wavelength'].read(maxage)
        Degree = self._adevs['twotheta'].read(maxage)
        Q = 4*math.pi/Lambda*math.sin(Degree/2*math.pi/180)
        return Q

    def doStatus(self, maxage=0):
        return status.OK, ''
