description = 'all values for detector positon'

group = 'lowlevel'

instrument_values = configdata('instrument.values')
showcase_values = configdata('cf_showcase.showcase_values')

tango_base = instrument_values['tango_base']
code_base = instrument_values['code_base']

devices = dict(
    primary_beam = device('nicos.devices.generic.ManualMove',
        description = 'Number of primary beam measurement for analysis',
        abslimits = (0, 100000000),
        default = 0,
        fmtstr = 'Nr %d',
        unit = '',
    ),
    det_drift = device('nicos.devices.generic.ManualSwitch',
        description = 'depth of detector drift1=40mm drift2=65mm',
        states = ['off','drift1', 'drift2'],
    ),
    hv_anode = device('nicos.devices.tango.PowerSupply',
        description = 'HV detector anode',
        tangodevice = tango_base + 'detector/anode/voltage',
        requires = {'level': 'admin'},
    ),
    hv_drift1 = device('nicos.devices.tango.PowerSupply',
        description = 'HV detector drift1',
        tangodevice = tango_base + 'detector/drift/voltage',
        requires = {'level': 'admin'},
    ),
    hv_drift2 = device('nicos.devices.tango.PowerSupply',
        description = 'HV detector drift1',
        tangodevice = tango_base + 'detector/drift2/voltage',
        requires = {'level': 'admin'},
    ),
    det_pivot = device(code_base + 'pivot.PivotPoint',
        description = 'Pivot point at floor of samplechamber',
        states = list(range(1, 15)),
        fmtstr = 'Point %d',
        unit = '',
    ),
    det_yoke_motor = device('nicos.devices.tango.Motor',
        description = 'yoke Motor',
        tangodevice = tango_base + 'test/tube/servostar',
        lowlevel = True,
    ),
    det_yoke = device('nicos.devices.generic.Axis',
        description = 'yoke height, refmove only in expertmode!',
        motor = 'det_yoke_motor',
        precision = 0.05,
        dragerror = 10.,
        fmtstr = '%.0f',
        lowlevel = False,
    ),
    det_yoke_enc_io = device('nicos.devices.tango.StringIO',
        description = 'Yoke big red: communication device',
        tangodevice = tango_base  + 'test/tube_enc/io',
        lowlevel = True,
    ),
    det_yoke_enc1 = device(code_base + 'det_yoke_enc.BasePos',
        description = 'one side',
        comm = 'det_yoke_enc_io',
        index = 1,
        lowlevel = True,
        unit = 'foo',
    ),
    det_yoke_enc2 = device(code_base + 'det_yoke_enc.BasePos',
        description = 'other side',
        comm = 'det_yoke_enc_io',
        index = 2,
        lowlevel = True,
        unit = 'foo',
    ),
    det_yoke_skew = device(code_base + 'skew_motor.SkewRead',
        description = 'SkewRead',
        motor_1 = 'det_yoke_enc1',
        motor_2 = 'det_yoke_enc2',
        lowlevel = True,
        unit = 'foo',
    ),
    det_yoke_enc = device(code_base + 'analogencoder.AnalogEncoder',
        description = 'Yoke big red: Encoder to validate position',
        device = 'det_yoke_skew',
        poly = [0, 1/(400.0*1.02543)],
        unit = 'mm',
        lowlevel = False,
    ),
    det_table_motor = device(code_base + 'beckhoff.nok.BeckhoffMotorDetector',
        description = 'table inside scatteringtube',
        tangodevice = tango_base + 'det_table/io/modbus',
        address = 0x3020 + 0 * 10,  # word address
        slope = 100,
        unit = 'mm',
        # 2020-07-27 13:50:54  abslimits = (1000, 10984.0137),  # because of Beamstop
        abslimits = (1000, 11025),  # real test, because of Beamstop
        precision = 10,
        maxtemp = 40,
        waittime = 40,
        lowlevel = True,
    ),
    det_table_poti = device(code_base + 'beckhoff.nok.BeckhoffCoderDetector',
        description = 'Coder of detector table inside scatteringtube',
        tangodevice = tango_base + 'det_table/io/modbus',
        address = 0x3020 + 1 * 10,  # word address
        slope = 100,
        unit = 'mm',
        lowlevel = True,
    ),
    # det_table_a = device('nicos.devices.generic.Axis',
    #     description = 'detector table inside scatteringtube. absmin is for beamstop',
    #     motor = 'det_table_motor',
    #     obs = ['det_table_analog'],
    #     precision = 1,
    #     dragerror = 15.,
    #     lowlevel = True,
    # ),
    det_table = device(code_base + 'focuspoint.FocusPoint',
        description = 'detector table inside scatteringtube. with pivot',
        unit = 'mm',
        table = 'det_table_motor',
        pivot = 'det_pivot',
    ),
    dix_laser_acc = device(code_base + 'nok_support.MotorEncoderDifference',
        description = 'laser measurement of table accuracy',
        motor = 'det_table',
        analog = 'dix_laser_analog',
        unit = 'mm',
        lowlevel = True,
    ),
    dix_laser_analog = device('nicos.devices.tango.Sensor',
        description = 'laser measurement of table',
        tangodevice = tango_base + 'test/laser/value',
        unit = 'mm',
        lowlevel = True,
    ),
    dix_laser_temperature = device('nicos.devices.tango.Sensor',
        description = 'laser measurement system temperature',
        tangodevice = tango_base + 'test/laser/temperature',
        unit = 'degC',
        lowlevel = True,
    ),
    tube_angle = device(code_base + 'tube.TubeAngle',
        description = 'Angle between flight tube and ground',
        yoke = 'det_yoke',
    ),
)
