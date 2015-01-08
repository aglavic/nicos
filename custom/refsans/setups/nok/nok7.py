#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2015 by the NICOS contributors (see AUTHORS)
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
#   Enrico Faulhaber <enrico.faulhaber@frm2.tum.de>
#
# **************************************************************************


description = "Devices for REFSANS's nok7"

group = 'lowlevel'

includes = ['nok_ref', 'nokbus3']

nethost = 'refsanssrv.refsans.frm2'

devices = dict(
    nok7           = device('nicos.refsans.nok_support.DoubleMotorNOK',
                            description = 'NOK7',
                            nok_start = 7665.5,
                            nok_length = 1190.0,
                            nok_end = 8855.5,
                            nok_gap = 1.0,
                            inclinationlimits = (-10, 10),   # invented values, PLEASE CHECK!
                            motor_r = 'nok7r_axis',
                            motor_s = 'nok7s_axis',
                            nok_motor = [7915.0, 8605.0],
                            backlash = -2,   # is this configured somewhere?
                            precision = 0.05,
                           ),

# generated from global/inf/resources.inf, geometrie.inf, optic.inf
    nok7r_axis     = device('nicos.devices.generic.Axis',
                            description = 'Axis of NOK7, reactor side',
                            motor = 'nok7r_motor',
                            coder = 'nok7r_motor',
                            obs = ['nok7r_obs'],
                            backlash = 0,
                            precision = 0.05,
                            unit = 'mm',
                            lowlevel = True,
                           ),

# generated from global/inf/resources.inf, geometrie.inf, optic.inf and taco *.res files
    nok7r_motor    = device('refsans.nok_support.NOKMotorIPC',
                            description = 'IPC controlled Motor of NOK7, reactor side',
                            abslimits = (-437.6, 116.15),
                            userlimits = (-89.475, 116.1),
                            bus = 'nokbus3',     # from ipcsms_*.res
                            addr = 0x52,     # from resources.inf
                            slope = 800.0,   # FULL steps per physical unit
                            speed = 10,
                            accel = 10,
                            confbyte = 48,
                            ramptype = 2,
                            microstep = 1,
                            refpos = 62.4,   # from ipcsms_*.res
                            zerosteps = int(687.6 * 800),    # offset * slope
                            lowlevel = True,
                           ),

# generated from global/inf/poti_tracing.inf
    nok7r_obs      = device('refsans.nok_support.NOKPosition',
                            description = 'Position sensing for NOK7, reactor side',
                            reference = 'nok_refc1',
                            measure = 'nok7r_poti',
                            poly = [17.162881, 1001.504 / 3.843],    # off, mul * 1000 / sensitivity, higher orders...
                            serial = 7540,
                            length = 250.0,
                            lowlevel = True,
                           ),

# generated from global/inf/poti_tracing.inf
    nok7r_poti     = device('refsans.nok_support.NOKMonitoredVoltage',
                            description = 'Poti for NOK7, reactor side',
                            tacodevice = '//%s/test/wb_c/1_0' % nethost,
                            scale = -1,  # mounted from top
                            lowlevel = True,
                           ),

# generated from global/inf/resources.inf, geometrie.inf, optic.inf
    nok7s_axis     = device('nicos.devices.generic.Axis',
                            description = 'Axis of NOK7, sample side',
                            motor = 'nok7s_motor',
                            coder = 'nok7s_motor',
                            obs = ['nok7s_obs'],
                            backlash = 0,
                            precision = 0.05,
                            unit = 'mm',
                            lowlevel = True,
                           ),

# generated from global/inf/resources.inf, geometrie.inf, optic.inf and taco *.res files
    nok7s_motor    = device('refsans.nok_support.NOKMotorIPC',
                            description = 'IPC controlled Motor of NOK7, sample side',
                            abslimits = (-96.94, 125.56),
                            userlimits = (-96.94, 125.55),
                            bus = 'nokbus3',     # from ipcsms_*.res
                            addr = 0x53,     # from resources.inf
                            slope = 800.0,   # FULL steps per physical unit
                            speed = 10,
                            accel = 10,
                            confbyte = 48,
                            ramptype = 2,
                            microstep = 1,
                            refpos = 66.84,  # from ipcsms_*.res
                            zerosteps = int(683.19 * 800),   # offset * slope
                            lowlevel = True,
                           ),

# generated from global/inf/poti_tracing.inf
    nok7s_obs      = device('refsans.nok_support.NOKPosition',
                            description = 'Position sensing for NOK7, sample side',
                            reference = 'nok_refc1',
                            measure = 'nok7s_poti',
                            poly = [24.5752, 1000.564 / 3.836],  # off, mul * 1000 / sensitivity, higher orders...
                            serial = 7546,
                            length = 250.0,
                            lowlevel = True,
                           ),

# generated from global/inf/poti_tracing.inf
    nok7s_poti     = device('refsans.nok_support.NOKMonitoredVoltage',
                            description = 'Poti for NOK7, sample side',
                            tacodevice = '//%s/test/wb_c/1_1' % nethost,
                            scale = -1,  # mounted from top
                            lowlevel = True,
                           ),
)
