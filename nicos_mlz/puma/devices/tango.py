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
#   Jens Krüger <jens.krueger@frm2.tum.de>
#
# *****************************************************************************
"""Special TANGO devices for PUMA."""

from nicos.devices.entangle import CounterChannel


class CycleCounter(CounterChannel):
    """Special counter channel.

    This devices sets the number of cycles, or in other words it has to add a
    1 to the monitor count to create a cycle as difference between to events.
    """

    def doReadPreselection(self):
        val = self._dev.preselection
        return val if val == 0 else val - 1

    def doWritePreselection(self, preselectionvalue):
        self.doStop()
        val = preselectionvalue
        self._dev.setPreselection = val if val == 0 else val + 1
