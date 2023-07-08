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
#   Jens Krüger <jens.krueger@frm2.tum.de>
#
# *****************************************************************************

name = 'test_refsans setup'

includes = ['detector']

sysconfig = dict(
    datasinks = ['configsink'],
    instrument = 'REFSANS',
)

devices = dict(
    REFSANS = device('nicos.devices.instrument.Instrument',
        instrument = 'REFSANS',
        responsible = 'Joe Doe <joe@doe.org>',
    ),
    shutter_gamma = device('nicos_mlz.refsans.devices.nok_support.SingleMotorNOK',
        motor = device('nicos.devices.generic.VirtualMotor',
            unit = 'mm',
            abslimits = (-56.119, 1.381),
        ),
        nok_start = 198.0,
        nok_end = 288.0,
        nok_gap = 1.0,
        backlash = -2,
        precision = 0.05,
    ),
    nok2 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        nok_start = 334.0,
        nok_end = 634.0,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        motor_r = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.VirtualMotor',
                unit = 'mm',
                abslimits = (-25., 25.),
            ),
            precision = 0.05,
        ),
        motor_s = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.VirtualMotor',
                unit = 'mm',
                abslimits = (-25., 25.),
            ),
            precision = 0.05,
        ),
        nok_motor = [408.5, 585.0],
        backlash = -2,
        precision = 0.05,
        masks = {
            'ng':    0.0,
            'rc':  22.5,
            'vc':  37.5,
            'fc':  52.5,
        },
    ),
    nok_inc_failed = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        nok_start = 334.0,
        nok_end = 634.0,
        nok_gap = 1.0,
        inclinationlimits = (10, -10),
        motor_r = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.VirtualMotor',
                unit = 'mm',
                abslimits = (-25., 25.),
            ),
            precision = 0.05,
        ),
        motor_s = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.VirtualMotor',
                unit = 'mm',
                abslimits = (-25., 25.),
            ),
            precision = 0.05,
        ),
        nok_motor = [408.5, 585.0],
        backlash = -2,
        precision = 0.05,
        masks = {
            'ng':    0.0,
            'rc':  22.5,
            'vc':  37.5,
            'fc':  52.5,
        },
    ),
    obs = device('nicos_mlz.refsans.devices.nok_support.NOKPosition',
        reference = device('nicos.devices.generic.VirtualCoder',
            motor = device('nicos.devices.generic.VirtualMotor',
                abslimits = (0, 10),
                unit = 'V',
                curvalue = 10.,
            ),
        ),
        measure = device('nicos.devices.generic.VirtualCoder',
            motor = device('nicos.devices.generic.VirtualMotor',
                abslimits = (0, 10),
                unit = 'V',
                curvalue = 5.,
            ),
        ),
        # off, mul * 1000 / sensitivity, higher orders...
        poly = [9., 900.],
        serial = 6510,
        length = 250.0,
    ),
    zb0 = device('nicos_mlz.refsans.devices.slits.SingleSlit',
        motor = device('nicos.devices.generic.VirtualMotor',
            unit = 'mm',
            abslimits = (-155.7889, 28.111099999999997),
            speed = 1.,
        ),
        nok_start = 4138.8,
        nok_end = 4151.8,
        nok_gap = 1,
        masks = {
            'slit': 0,
            'point': 0,
            'gisans': -110,
        },
        unit = 'mm',
    ),
    zb1 = device('nicos_mlz.refsans.devices.slits.SingleSlit',
        motor = device('nicos.devices.generic.virtual.VirtualMotor',
            abslimits = (-184, 0.0),
            userlimits = (-184, 0.0),
            unit = 'mm',
            speed = 0.,
        ),
        nok_start = 5856.5,
        nok_end = 5862.5,
        nok_gap = 1,
        masks = {
            'slit': 0,
            'point': 0,
            'gisans': -100,
        },
        unit = 'mm',
    ),
    zb3r = device('nicos_mlz.refsans.devices.slits.SingleSlit',
        motor = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.virtual.VirtualMotor',
                abslimits = (-677.125, 99.125),
                userlimits = (-221.0, 95.0),
                unit = 'mm',
            ),
            precision = 0.5,
            unit = 'mm',
        ),
        nok_start = 8837.5,
        nok_end = 8850.5,
        nok_gap = 1.0,
        masks = {
            'slit': -0,
            'point': -0,
            'gisans': -110,
        },
        unit = 'mm',
    ),
    zb3s = device('nicos_mlz.refsans.devices.slits.SingleSlit',
        motor = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.virtual.VirtualMotor',
                abslimits = (-150.8125, 113.5625),
                userlimits = (-150.0, 113.562),
                unit = 'mm',
            ),
            precision = 0.5,
            unit = 'mm',
        ),
        nok_start = 8837.5,
        nok_end = 8850.5,
        nok_gap = 1.0,
        masks = {
            'slit': -0,
            'point': -0,
            'gisans': -110,
        },
        unit = 'mm',
    ),
    zb3 = device('nicos_mlz.refsans.devices.slits.DoubleSlit',
        slit_r = 'zb3r',
        slit_s = 'zb3s',
        unit = 'mm x mm',
    ),
    zb3r_acc = device('nicos.devices.generic.ManualMove',
         abslimits = (0, 10),
         unit = 'mm'
    ),
    zb3s_acc = device('nicos.devices.generic.ManualMove',
         abslimits = (0, 10),
         unit = 'mm'
    ),
    configsink = device('nicos_mlz.refsans.datasinks.ConfigObjDatafileSink',
    ),
    vacuum_CB = device('nicos.devices.generic.ManualMove',
        default = 3.5e-6,
        abslimits = (0, 1000),
        unit = 'mbar',
    ),
    shutter = device('nicos.devices.generic.ManualSwitch',
        states = ['closed', 'open'],
    ),
    table_mot = device('nicos.devices.generic.VirtualMotor',
        abslimits = (620, 11025),
        unit = 'mm',
    ),
    table = device('nicos.devices.generic.Axis',
        motor = 'table_mot',
        precision = 0.05,
    ),
    table_pos = device('nicos.devices.generic.VirtualCoder',
        motor = 'table_mot',
        offset = 10,
    ),
    table_acc = device('nicos_mlz.refsans.devices.accuracy.Accuracy',
        absolute = True,
        motor = 'table_mot',
        analog = 'table_pos',
        unit = 'mm',
    ),
    tube = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-120, 1000),
        unit = 'mm',
    ),
    top_phi = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-10.5, 10.5),
        unit = 'deg',
    ),
    pivot = device('nicos.devices.generic.ManualSwitch',
        states = list(range(1, 14)),
    ),
    chopper = device('nicos_mlz.refsans.devices.chopper.base.ChopperMaster',
        fmtstr = '%s',
        unit = '',
        chopper1 = 'chopper_speed',
        chopper2 = 'chopper2',
        chopper3 = 'chopper3',
        chopper4 = 'chopper4',
        chopper5 = 'chopper5',
        chopper6 = 'chopper6',
        shutter = 'shutter',
        wlmin = 3,
        wlmax = 21,
        dist = 22.8,
    ),
    chopper_speed = device('nicos_mlz.refsans.devices.chopper.virtual.ChopperDisc1',
        chopper = 1,
        edge = 'open',
        gear = 1,
        discs = ['chopper2', 'chopper3', 'chopper4', 'chopper5', 'chopper6'],
        speed = 0,
        jitter = 0,
        # visibility = (),
    ),
    chopper2 = device('nicos_mlz.refsans.devices.chopper.virtual.ChopperDisc2',
        chopper = 2,
        gear = 1,
        edge = 'close',
        translation = 'chopper2_pos',
        speed = 0,
        jitter = 0,
        visibility = (),
    ),
    chopper2_pos = device('nicos_mlz.refsans.devices.chopper.virtual.ChopperDiscTranslation',
        disc = 'chopper3',
        curvalue = 5,
        speed = 0,
        visibility = (),
    ),
    chopper3 = device('nicos_mlz.refsans.devices.chopper.virtual.ChopperDisc',
        chopper = 3,
        gear = 1,
        edge = 'open',
        speed = 0,
        jitter = 0,
        visibility = (),
    ),
    chopper4 = device('nicos_mlz.refsans.devices.chopper.virtual.ChopperDisc',
        chopper = 4,
        gear = 1,
        edge = 'close',
        speed = 0,
        jitter = 0,
        visibility = (),
    ),
    chopper5 = device('nicos_mlz.refsans.devices.chopper.virtual.ChopperDisc',
        chopper = 5,
        gear = 2,
        edge = 'open',
        speed = 0,
        jitter = 0,
        visibility = (),
    ),
    chopper6 = device('nicos_mlz.refsans.devices.chopper.virtual.ChopperDisc',
        chopper = 6,
        gear = 2,
        edge = 'close',
        speed = 0,
        jitter = 0,
        visibility = (),
    ),
    height = device('nicos_mlz.refsans.devices.tristate.TriState',
        unit = 'mm',
        port = 'height_port',
    ),
    height_port = device('nicos.devices.generic.ManualMove',
        abslimits = (0, 1),
        default = 1,
        unit = 'mm',
        visibility = (),
    ),
    bsh_input_low = device('nicos.devices.generic.ManualMove',
        abslimits = (0, 10),
        unit = 'V',
        default = 3,
    ),
    bsh_input = device('nicos_mlz.refsans.devices.beamstop.BeamStopDevice',
        unit = 'mm',
        att = 'bsh_input_low',
    ),
    bsh = device('nicos_mlz.refsans.devices.converters.LinearKorr',
        unit = 'mm',
        informula = '50 * x',
        dev = 'bsh_input',
    ),
    bsc_input = device('nicos.devices.generic.ManualSwitch',
        states = [i for i in range(3, 9)],
    ),
    bsc = device('nicos_mlz.refsans.devices.beamstop.BeamStopCenter',
        unit = '',
        att = 'bsc_input',
    ),
    backguard = device('nicos_mlz.refsans.devices.skew_motor.SkewMotor',
        one = 'backguard_1',
        two = 'backguard_2',
        abslimits = (-60, 60),
        precision = 0.1,
        skew = 2,
        unit = 'mm',
    ),
    backguard_1 = device('nicos.devices.generic.Axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-0.5, 61.0),
            unit = 'mm',
        ),
        precision = 0.01,
    ),
    backguard_2 = device('nicos.devices.generic.Axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-0.5, 61.0),
            unit = 'mm',
        ),
        precision = 0.01,
    ),
    det_table = device('nicos_mlz.refsans.devices.focuspoint.FocusPoint',
        unit = 'mm',
        table = 'det_table_a',
        pivot = 'det_pivot',
        abslimits = [1065, 10864],
    ),
    det_table_a = device('nicos.devices.generic.Axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            unit = 'mm',
            abslimits = (1000, 11025),
        ),
        precision = 1,
        dragerror = 15.,
        visibility = (),
    ),
    det_pivot = device('nicos_mlz.refsans.devices.pivot.PivotPoint',
        states = [i for i in range(1, 14 + 1)],
        fmtstr = 'Point %d',
        unit = '',
    ),
    real_flight_path = device('nicos_mlz.refsans.devices.resolution.RealFlightPath',
        table = 'det_table',
        pivot = 'det_pivot',
    ),
    resolution = device('nicos_mlz.refsans.devices.resolution.Resolution',
        chopper = 'chopper',
        flightpath = 'real_flight_path',
    ),
    gonio_theta = device('nicos.devices.generic.Axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-500, 500),
            unit = 'deg',
        ),
        precision = 0.01,
    ),
    User2Voltage = device('nicos.devices.generic.ManualMove',
        abslimits = (0, 10),
        unit = 'V',
    ),
    mon1 = device('nicos.devices.generic.VirtualCounter',
        fmtstr = '%d',
        type = 'monitor',
        countrate = 100,
    ),
    timer = device('nicos.devices.generic.VirtualTimer',
    ),
    image = device('nicos.devices.generic.VirtualImage',
        fmtstr = '%d',
        size = (256, 256),
        background = 0,
    ),
    det = device('nicos.devices.generic.Detector',
        timers = ['timer'],
        monitors = ['mon1'],
        images = ['image'],
    ),
    rawcoder = device('nicos.devices.generic.ManualMove',
        abslimits = (-10, 10),
        default = 0,
        unit = 'mm',
    ),
    acoder = device('nicos_mlz.refsans.devices.analogencoder.AnalogEncoder',
        device = 'rawcoder',
        poly = [1, 2],
        unit = 'mm',
    ),
    identitycoder = device('nicos_mlz.refsans.devices.analogencoder.AnalogEncoder',
        device = 'rawcoder',
        unit = 'mm',
    ),
    primary_aperture = device('nicos.devices.generic.DeviceAlias'),
    last_aperture = device('nicos.devices.generic.DeviceAlias'),
    dix_value = device('nicos.devices.generic.VirtualMotor',
        abslimits = (0, 12000),
        unit = 'mm',
        visibility = (),
        curvalue = 1234,
    ),
    dix_signal = device('nicos.devices.generic.VirtualMotor',
        abslimits = (7000, 20000),
        unit = '',
        visibility = (),
        curvalue = 10000,
    ),
    dix = device('nicos_mlz.refsans.devices.dimetix.DimetixLaser',
        value = 'dix_value',
        signal = 'dix_signal',
    ),
    h2_ctrl_r = device('nicos.devices.generic.VirtualMotor',
        unit = 'mm',
        abslimits = (3, 138.),
        visibility = (),
    ),
    h2_ctrl_l = device('nicos.devices.generic.VirtualMotor',
        unit = 'mm',
        abslimits = (3, 138.),
        visibility = (),
    ),
    h2_motor_l = device('nicos_mlz.refsans.devices.analogencoder.AnalogMove',
        device = 'h2_ctrl_l',
        unit = 'mm',
        poly = [61.6156,  -1],
        visibility = (),
    ),
    h2_motor_r = device('nicos_mlz.refsans.devices.analogencoder.AnalogMove',
        device = 'h2_ctrl_r',
        unit = 'mm',
        poly = [60.3869,  -1, 0],
        visibility = (),
    ),
    h2l = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-69.5, 5),
        unit = 'mm',
        visibility = (),
    ),
    h2r = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-5, 69.5),
        unit = 'mm',
        visibility = (),
    ),
    h2 = device('nicos.devices.generic.slit.HorizontalGap',
        left = 'h2l',
        right = 'h2r',
        opmode = 'offcentered',
    ),
    h2opposite = device('nicos.devices.generic.slit.HorizontalGap',
        left = 'h2l',
        right = 'h2r',
        opmode = 'offcentered',
        coordinates = 'opposite',
    ),
    ttr = device('nicos_mlz.refsans.devices.converters.Ttr',
        unit = 'mbar',
        att = device('nicos.devices.generic.ManualMove',
            abslimits = (0, 10),
            unit = 'V',
            default = 1,
        ),
    ),
)

alias_config = {
    'primary_aperture': {'zb3.height': 100},
    'primary_aperture': {'zb3.height': 100},
}
