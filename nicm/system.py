#  -*- coding: utf-8 -*-
# *****************************************************************************
# Module:
#   $Id$
#
# Description:
#   NICOS System device
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

"""
NICOS system device.
"""

__author__  = "$Author$"
__date__    = "$Date$"
__version__ = "$Revision$"


from nicm.data import Storage
from nicm.utils import listof
from nicm.device import Device


class Logging(Device):
    """A special singleton device to configure logging."""

    parameters = {
        'logpath': (str, '', True, 'Path for logfiles.'),
    }


class System(Device):
    """A special singleton device that serves for global configuration of
    the NICM system.
    """

    parameters = {
        'histories': (listof(str), [], False,
                      'Global history managers for all devices.'),
    }

    attached_devices = {
        'logging': Logging,
        'storage': Storage,
    }

    def __repr__(self):
        return '<NICM System>'

    @property
    def storage(self):
        return self._adevs['storage']

    @property
    def logging(self):
        return self._adevs['logging']
