#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2020 by the NICOS contributors (see AUTHORS)
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
#   Matt Clarke <matt.clarke@ess.eu>
#
# *****************************************************************************
from nicos.core import Param, anytype, dictof, tupleof
from nicos.devices.sample import Sample


class EssSample(Sample):
    """Device that collects the various sample properties specific to
    samples at ESS.
    """

    parameters = {
        'sample_name': Param('name', type=str, settable=True,
                             category='sample'),
        'sample_formula': Param('formula', type=str, settable=True,
                                category='sample'),
        'number_of': Param('number_of', type=int, settable=True,
                           category='sample'),
        'mass_volume': Param('mass/volume', type=str, settable=True,
                             category='sample'),
        'density': Param('density', type=str, settable=True, category='sample'),
    }

    def new(self, parameters):
        # EssSample being set using NewSample should have sample_name?
        # i.e. parameter in NewSample(name, **parameters) must also have
        # sample_name key.
        if 'sample_name' in parameters:
            Sample.new(self, parameters)
