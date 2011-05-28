#  -*- coding: utf-8 -*-
# *****************************************************************************
# Module:
#   $Id$
#
# Author:
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
# NICOS-NG, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2011 by the NICOS-NG contributors (see AUTHORS)
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
# *****************************************************************************

name = 'devices for the TAS setup'

includes = ['system']

sysconfig = dict(
    instrument = 'tas',
)

devices = dict(
    tas      = device('nicos.tas.TAS',
                      instrument = 'VTAS',
                      responsible = 'R. Esponsible <responsible@frm2.tum.de>',
                      cell = 'Sample',
                      phi = 'phi',
                      psi = 'psi',
                      mono = 'mono',
                      ana = 'ana'),

    phi      = device('nicos.virtual.VirtualMotor',
                      abslimits = (-180, 180),
                      initval = 0,
                      unit = 'deg'),

    psi      = device('nicos.virtual.VirtualMotor',
                      abslimits = (0, 360),
                      initval = 0,
                      unit = 'deg'),

    mono     = device('nicos.tas.Monochromator',
                      unit = 'A-1',
                      dvalue = 2.88,
                      theta = 'mth',
                      twotheta = 'mtt',
                      focush = None,
                      focusv = None,
                      abslimits = (0, 10)),

    mth      = device('nicos.virtual.VirtualMotor',
                      unit = 'deg',
                      abslimits = (-180, 180),
                      precision = 0.05,
                      initval = 45),

    mtt      = device('nicos.virtual.VirtualMotor',
                      unit = 'deg',
                      abslimits = (-180, 180),
                      precision = 0.05,
                      initval = 90),

    ana      = device('nicos.tas.Monochromator',
                      unit = 'A-1',
                      dvalue = 3.325,
                      theta = 'ath',
                      twotheta = 'att',
                      focush = None,
                      focusv = None,
                      abslimits = (0, 10)),

    ath      = device('nicos.virtual.VirtualMotor',
                      unit = 'deg',
                      abslimits = (-180, 180),
                      precision = 0.05,
                      initval = 35),

    att      = device('nicos.virtual.VirtualMotor',
                      unit = 'deg',
                      abslimits = (-180, 180),
                      precision = 0.05,
                      initval = 70),

    ki       = device('nicos.tas.Wavevector',
                      unit = 'A-1',
                      base = 'mono',
                      tas = 'tas',
                      scanmode = 'CKI',
                      abslimits = (0, 10)),

    kf       = device('nicos.tas.Wavevector',
                      unit = 'A-1',
                      base = 'ana',
                      tas = 'tas',
                      scanmode = 'CKF',
                      abslimits = (0, 10)),
)
