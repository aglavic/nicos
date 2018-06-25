#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2018 by the NICOS contributors (see AUTHORS)
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
#   Nikhil Biyani <nikhil.biyani@psi.ch>
#
# *****************************************************************************

from nicos.core import Param, pvname, usermethod, status, Override
from nicos.core.errors import PositionError
from nicos.devices.abstract import MappedReadable
from nicos.devices.epics import EpicsReadable


class ProgrammableUnit(MappedReadable, EpicsReadable):
    """ AMOR has a Siemens programmable logic unit for controlling the shutter
    and a switch for the alignment laser and the spin flipper. This is SPS-S5
    which is connected to the world as such via a custom RS232 interface and a
    terminal server. *readpv* returns a waveform record with 16 bytes giving
    the state of the SPS digital inputs. *commandpv* sends the commands to
    toggle SPS buttons.
    """

    parameters = {
        'byte': Param('Byte number representing the state of this unit',
                      type=int, mandatory=True, userparam=False,
                      settable=False),
        'bit': Param('Bit number from the byte representing the state',
                     type=int, mandatory=True, userparam=False,
                     settable=False),
        'commandpv': Param('PV to issue commands to the asyn controller',
                           type=pvname, mandatory=True, settable=False,
                           userparam=False),
        'commandstr': Param('Command to issue on commandpv for switching '
                            'the state ', type=str, mandatory=True,
                            settable=False, userparam=False),
    }

    parameter_overrides = {
        'mapping': Override(userparam=False, settable=False),
        'fallback': Override(userparam=False),
        'unit': Override(userparam=False)
    }

    def _get_pv_parameters(self):
        return EpicsReadable._get_pv_parameters(self) | {'commandpv'}

    def doInit(self, mode):
        MappedReadable.doInit(self, mode)
        EpicsReadable.doInit(self, mode)

    def doStatus(self, maxage=0):
        epics_status = EpicsReadable.doStatus(self, maxage)
        if epics_status[0] == status.OK:
            return status.OK, ''

        return epics_status

    def _readRaw(self, maxage=0):
        raw = EpicsReadable.doRead(self, maxage)

        if self.byte > len(raw):
            raise PositionError('Byte specified is out of bounds')

        powered = 1 << self.bit
        return int(raw[self.byte] & powered == powered)

    @usermethod
    def toggle(self):
        self._put_pv('commandpv', self.commandstr)
