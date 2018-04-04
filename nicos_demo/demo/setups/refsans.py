description = 'REFSANS demo setup'

group = 'basic'

excludes = ['detector', 'qmchannel', 'table']

includes = ['zb0', 'zb1', 'zb2', 'zb3']

sysconfig = dict(
    datasinks = ['configsink'],
)

devices = dict(
    Sample = device('nicos.devices.sample.Sample',
        description = 'Demo sample',
    ),

    nok1 = device('nicos_mlz.refsans.devices.nok_support.SingleMotorNOK',
        description = 'NOK1',
        motor = device('nicos.devices.generic.VirtualMotor',
            speed = 5,
            abslimits = (-56.119, 1.381),
            unit = 'mm',
        ),
        obs = [],
        nok_start = 198.0,
        nok_length = 90.0,
        nok_end = 288.0,
        nok_gap = 1.0,
        backlash = -2,
        precision = 0.05,
    ),
    nok2 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK2',
        nok_start = 334.0,
        nok_length = 300.0,
        nok_end = 634.0,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [408.5, 585.0],
        backlash = -2,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-22.36, 10.88),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-21.61, 6.885),
            speed = 5,
            unit = 'mm',
        ),
    ),
    nok3 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK3',
        nok_start = 680.0,
        nok_length = 600.0,
        nok_end = 1280.0,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [831.0, 1131.0],
        backlash = -2,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-21.967, 47.782),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-20.944, 40.8055),
            speed = 5,
            unit = 'mm',
        ),
    ),
    nok4 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK4',
        nok_start = 1326.0,
        nok_length = 1000.0,
        nok_end = 2326.0,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [1477.0, 2177.0],
        backlash = -2,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-20.477, 48.523),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-21.3025, 41.197),
            speed = 5,
            unit = 'mm',
        ),
    ),
    nok5a = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK5A',
        nok_start = 2418.5,
        nok_length = 1720.0,
        nok_end = 4138.5,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [3108.0, 3888.0],
        backlash = -2,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-33.04875, 61.30375),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-37.49, 66.25),
            speed = 5,
            unit = 'mm',
        ),
    ),
    nok5b = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK5B',
        nok_start = 4153.5,
        nok_length = 1720.0,
        nok_end = 5873.5,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [4403.0, 5623.0],
        backlash = -2,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-44.85, 78.8),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-59.08, 93.41),
            speed = 5,
            unit = 'mm',
        ),
    ),
    nok6 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK6',
        nok_start = 5887.5,
        nok_length = 1720.0,
        nok_end = 7607.5,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [6137.0, 7357.0],
        backlash = -2,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-68.0, 96.59125),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-81.0, 110.875),
            speed = 5,
            unit = 'mm',
        ),
    ),
    nok7 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK7',
        nok_start = 7665.5,
        nok_length = 1190.0,
        nok_end = 8855.5,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [7915.0, 8605.0],
        backlash = -2,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-89.475, 116.1),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-96.94, 125.55),
            speed = 5,
            unit = 'mm',
        ),
    ),
    nok8 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK8',
        nok_start = 8870.5,
        nok_length = 880.0,
        nok_end = 9750.5,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [9120.0, 9500.0],
        backlash = -2,   # is this configured somewhere?
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-102.835, 128.41),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-104.6, 131.636),
            speed = 5,
            unit = 'mm',
        ),
    ),
    nok9 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'NOK9',
        nok_start = 9773.5,
        nok_length = 840.0,
        nok_end = 10613.5,
        nok_gap = 1.0,
        inclinationlimits = (-10, 10),
        nok_motor = [10023.5, 10362.7],
        backlash = -2,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-112.03425, 142.95925),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-114.51425, 142.62775),
            speed = 5,
            unit = 'mm',
        ),
    ),
    det_timer = device('nicos.devices.generic.VirtualTimer',
        description = 'demo timer',
    ),
    det_img = device('nicos.devices.generic.VirtualImage',
        description = 'demo 2D detector',
        distance = None,
        collimation = None,
    ),
    det = device('nicos.devices.generic.Detector',
        description = 'demo 2D detector',
        timers = ['det_timer'],
        images = ['det_img'],
    ),
    table = device('nicos.devices.generic.Axis',
        description = 'Detector table inside tube',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (620, 11025),
            unit = 'mm',
        ),
        precision = 0.05,
    ),
    pivot = device('nicos.devices.generic.ManualSwitch',
        description = 'Distance between sample position and pivot '
                      'point of the detector tube',
        states = range(1, 14),
        fmtstr = 'point %d',
        unit = '',
    ),
    tube = device('nicos.devices.generic.Axis',
        description = 'tube height',
        motor = device('nicos.devices.generic.VirtualMotor',
            description = 'tube Motor',
            abslimits = (-120, 1000),
            unit = 'mm',
        ),
        obs = [],
        precision = 0.05,
        dragerror = 10.,
    ),
    configsink = device('nicos_mlz.refsans.devices.datasinks.ConfigObjDatafileSink',
    ),
    vacuum_CB = device('nicos.devices.generic.ManualMove',
        description = 'Vacuum sensor in chopper chamber',
        default = 1.7e-6,
        abslimits = (0, 1000),
        unit = 'mbar',
    ),
    vacuum_SFK = device('nicos.devices.generic.ManualMove',
        description = 'Vacuum sensor in beam guide chamber',
        default = 0.00012,
        abslimits = (0, 1000),
        unit = 'mbar',
    ),
    vacuum_SR = device('nicos.devices.generic.ManualMove',
        description = 'Vacuum sensor in scattering chamber',
        default = 3.5e-6,
        abslimits = (0, 1000),
        unit = 'mbar',
    ),
    shutter = device('nicos.devices.generic.ManualSwitch',
        description = 'Instrument shutter',
        states = ['closed', 'open'],
    ),
    bs1 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'BS1',
        nok_start = 9764.5,
        nok_length = 6.0,
        nok_end = 9770.5,
        nok_gap = 18.0,
        inclinationlimits = (-1000, 1000),
        masks = dict(
            k1 = [-40.0, 0.0, -1.83, 0.0],
            slit = [0.0, 0.0, -0.67, -0.89],
        ),
        nok_motor = [9764.75, 9770.25],
        backlash = -2,
        precision = 0.05,
        motor_r = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-323.075, 458.17375),
            speed = 5,
            unit = 'mm',
        ),
        motor_s = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-177.315, 142.685),
            speed = 5,
            unit = 'mm',
        ),
    ),
    # zb0 = device('nicos_mlz.refsans.devices.nok_support.SingleMotorNOK',
    #     description = 'ZB0',
    #     motor = device('nicos.devices.generic.VirtualMotor',
    #         abslimits = (-180.815, 69.185),
    #         speed = 5,
    #         unit = 'mm',
    #     ),
    #     obs = [],
    #     nok_start = 4121.5,
    #     nok_length = 13.0,
    #     nok_end = 4134.5,
    #     nok_gap = 1.0,
    #     masks = dict(
    #         k1 = [-110.0, 0.0],
    #         slit = [0.0, 0.0],
    #     ),
    #     nok_motor = 4128.5,
    #     backlash = -2,
    #     precision = 0.05,
    # ),
    # zb1 = device('nicos_mlz.refsans.devices.nok_support.SingleMotorNOK',
    #     description = 'ZB1',
    #     motor = device('nicos.devices.generic.VirtualMotor',
    #         abslimits = (-443.52875, 81.47125),
    #         speed = 5,
    #         unit = 'mm',
    #     ),
    #     obs = [],
    #     nok_start = 5856.5,
    #     nok_length = 13.0,
    #     nok_end = 5869.5,
    #     nok_gap = 1.0,
    #     masks = dict(
    #         k1 = [-120.0, 0.0],
    #         slit = [0.0, 0.0],
    #     ),
    #     nok_motor = 5862.5,
    #     backlash = -2,
    #     precision = 0.05,
    # ),
    # zb2 = device('nicos_mlz.refsans.devices.nok_support.SingleMotorNOK',
    #     description = 'ZB2',
    #     motor = device('nicos.devices.generic.VirtualMotor',
    #         abslimits = (-681.9525, 568.04625),
    #         speed = 5,
    #         unit = 'mm',
    #     ),
    #     obs = [],
    #     nok_start = 7591.5,
    #     nok_length = 6.0,
    #     nok_end = 7597.5,
    #     nok_gap = 1.0,
    #     masks = dict(
    #         k1 = [-120.0, 0.0],
    #         slit = [0.0, 0.0],
    #     ),
    #     nok_motor = 7597.5,
    #     backlash = -2,
    #     precision = 0.05,
    # ),
    # zb3 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
    #     description = 'ZB3',
    #     nok_start = 8837.5,
    #     nok_length = 13.0,
    #     nok_end = 8850.5,
    #     nok_gap = 1.0,
    #     inclinationlimits = (-1000, 1000),
    #     masks = dict(
    #         k1 = [-110.0, 0.0, -2.64, 0.0],
    #         slit = [0.0, 0.0, -2.63, -0.57],
    #     ),
    #     motor_r = device('nicos.devices.generic.VirtualMotor',
    #         abslimits = (-677.125, 99.125),
    #         speed = 5,
    #         unit = 'mm',
    #     ),
    #     motor_s = device('nicos.devices.generic.VirtualMotor',
    #         abslimits = (-150.8125, 113.5625),
    #         speed = 5,
    #         unit = 'mm',
    #     ),
    #     nok_motor = [8843.5, 8850.5],
    #     backlash = -2,
    #     precision = 0.05,
    # ),

    b1 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'aperture B1',
        nok_start = 0,
        nok_end = 0,
        nok_length = 0,
        nok_gap = 1,
        inclinationlimits = (-1000, 1000),
        masks = dict(
            k1 = [0, -85, -2.81, -0.24],
            slit = [0, 0, -2.734, -2.15],
        ),
        motor_r = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.VirtualMotor',
                abslimits = (-70, 68),
                speed = 5,
                unit = 'mm',
            ),
            backlash = 0,
            precision = 0.002,
        ),
        motor_s = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.VirtualMotor',
                abslimits = (-70, 68),
                speed = 5,
                unit = 'mm',
            ),
            backlash = 0,
            precision = 0.002,
        ),
    ),

    b2 = device('nicos_mlz.refsans.devices.nok_support.DoubleMotorNOK',
        description = 'aperture at sample position',
        nok_start = 11049.5,
        nok_end = 11064.5,
        nok_length = 13.,
        nok_gap = 1.,
        inclinationlimits = (-1000, 1000),
        masks = dict(
            k1 = [0, -85, -2.81, -0.24],
            slit = [0, 0, -2.734, -2.15],
        ),
        motor_r = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.VirtualMotor',
                abslimits = (-294, 222),
                speed = 5,
                unit = 'mm',
            ),
            backlash = 0,
            precision = 0.05,
        ),
        motor_s = device('nicos.devices.generic.Axis',
            motor = device('nicos.devices.generic.VirtualMotor',
                abslimits = (-296, 213),
                speed = 5,
                unit = 'mm',
            ),
            backlash = 0,
            precision = 0.05,
        ),
        nok_motor = [11049.5, 11064.5],
        backlash = 0,
        precision = 0.05,
    ),

    h2_width = device('nicos.devices.generic.VirtualMotor',
        description = 'Horizontal slit system: opening of the slit',
        unit = 'mm',
        speed = 5,
        abslimits = (-69.5, 69.5),
    ),
    h2_center = device('nicos.devices.generic.VirtualMotor',
        description = 'Horizontal slit system: offset of the slit-center to the beam',
        unit = 'mm',
        speed = 5,
        abslimits = (0.05, 69.5),
    ),

    theta = device('nicos.devices.generic.Axis',
        description = 'Theta axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-2, 10),
            unit = 'deg',
        ),
        precision = 0.01,
    ),
    phi = device('nicos.devices.generic.Axis',
        description = 'Phi axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-9.75, 9.5),
            unit = 'deg',
        ),
        precision = 0.01,
    ),
    chi = device('nicos.devices.generic.Axis',
        description = 'Chi axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-2.5, 2.5),
            unit = 'deg',
        ),
        precision = 0.01,
    ),
    y = device('nicos.devices.generic.Axis',
        description = 'Y axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-78.0, 75.0),
            unit = 'mm',
        ),
        precision = 0.01,
    ),
    z = device('nicos.devices.generic.Axis',
        description = 'Z axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-300.0, 188.0),
            unit = 'mm',
        ),
        precision = 0.01,
    ),
    probenwechsler = device('nicos.devices.generic.Axis',
        description = 'Samplechanger axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-.5, 400.5),
            unit = 'mm',
        ),
        precision = 0.01,
    ),
    bg = device('nicos.devices.generic.VirtualMotor',
        description = 'Backgard axis motor',
        abslimits = (-0.5, 31.0),
        unit = 'mm',
    ),
    monitor = device('nicos.devices.generic.VirtualMotor',
        description = 'Monitor axis motor',
        abslimits = (10, 300),
        unit = 'mm',
    ),
    top_theta = device('nicos.devices.generic.VirtualMotor',
        description = 'Top Theta axis motor',
        abslimits = (-9.5, 10.5),
        unit = 'deg',
    ),
    top_z = device('nicos.devices.generic.VirtualMotor',
        description = 'Top Z axis motor',
        abslimits = (-0.05, 15),
        unit = 'mm',
    ),
    top_phi = device('nicos.devices.generic.VirtualMotor',
        description = 'Top Phi axis motor',
        abslimits = (-10.5, 10.5),
        unit = 'deg',
    ),
    optic = device('nicos_mlz.refsans.devices.optic.Optic',
        description = 'Beam optic',
    ),
)

startupcode = '''
SetDetectors(det)
printinfo("============================================================")
printinfo("Welcome to the NICOS REFSANS demo setup.")
printinfo("Run count(1) to collect an image.")
printinfo("============================================================")
'''
