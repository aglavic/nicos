description = 'all values for detector positon'

group = 'lowlevel'

instrument_values = configdata('instrument.values')
showcase_values = configdata('cf_showcase.showcase_values')

tango_base = instrument_values['tango_base']
code_base = instrument_values['code_base']

devices = dict(
    det_type = device('nicos.devices.generic.ManualSwitch',
        description = 'type of detector',
        states = ['DNX-700 TN'],
    ),
    det_pixsize = device('nicos.devices.generic.ManualSwitch',
        description = 'type of detector',
        states = ['(2.072, 2.093)'],
    ),
    primary_beam = device('nicos.devices.generic.ManualMove',
        description = 'Number of primary beam measurement for analysis',
        abslimits = (0, 100000000),
        default = 0,
        fmtstr = 'Nr %d',
        unit = '',
    ),
    hv_anode = device('nicos.devices.entangle.PowerSupply',
        description = 'HV detector anode',
        tangodevice = tango_base + 'detector/anode/voltage',
        requires = {'level': 'admin'},
        precision = 1.0,
    ),
    hv_drift1 = device('nicos.devices.entangle.PowerSupply',
        description = 'HV detector drift1',
        tangodevice = tango_base + 'detector/drift/voltage',
        requires = {'level': 'admin'},
        precision = 1.0,
    ),
    hv_drift2 = device('nicos.devices.entangle.PowerSupply',
        description = 'HV detector drift1',
        tangodevice = tango_base + 'detector/drift2/voltage',
        requires = {'level': 'admin'},
        precision = 4.0,
    ),
    det_pivot = device(code_base + 'pivot.PivotPoint',
        description = 'Pivot point at floor of samplechamber',
        states = list(range(1, 15)),
        fmtstr = 'Point %d',
        unit = '',
    ),
    det_yoke_motor = device('nicos.devices.entangle.Motor',
        description = 'yoke Motor',
        tangodevice = tango_base + 'test/tube/servostar',
        visibility = (),
    ),
    det_yoke = device('nicos.devices.generic.Axis',
        description = 'yoke height, refmove only in expertmode!',
        motor = 'det_yoke_motor',
        precision = 0.05,
        dragerror = 10.,
        fmtstr = '%.0f',
        visibility = ('devlist', 'metadata', 'namespace'),
    ),
    det_yoke_acc = device(code_base + 'accuracy.Accuracy',
        description = 'error Motor and Encoder',
        motor = 'det_yoke_motor',
        analog = 'det_yoke_enc',
        visibility = showcase_values['hide_acc'],
        unit = 'mm'
    ),
    det_yoke_enc_io = device('nicos.devices.entangle.StringIO',
        description = 'Yoke big red: communication device',
        tangodevice = tango_base  + 'test/tube_enc/io',
        visibility = (),
    ),
    det_yoke_enc1 = device(code_base + 'det_yoke_enc.BasePos',
        description = 'one side',
        comm = 'det_yoke_enc_io',
        index = 1,
        visibility = (),
        unit = 'foo',
    ),
    det_yoke_enc2 = device(code_base + 'det_yoke_enc.BasePos',
        description = 'other side',
        comm = 'det_yoke_enc_io',
        index = 2,
        visibility = (),
        unit = 'foo',
    ),
    det_yoke_skew = device(code_base + 'skew_motor.SkewRead',
        description = 'SkewRead',
        one = 'det_yoke_enc1',
        two = 'det_yoke_enc2',
        visibility = (),
        unit = 'foo',
    ),
    det_yoke_enc = device(code_base + 'analogencoder.AnalogEncoder',
        description = 'Yoke big red: Encoder to validate position',
        device = 'det_yoke_skew',
        poly = [0, 1/(400.0*1.02543)],
        unit = 'mm',
        visibility = (),
    ),
    det_table_raw = device('nicos.devices.entangle.Actuator',
        description = 'table inside scatteringtube mit Pluto',
        tangodevice = tango_base + 'det_table/plc/_TablePosition',
        unit = 'mm',
        precision = 20000,
        userlimits = (1270, 11025), #for Cd (1140, 11025),
        visibility = (),
    ),
    det_table_poti = device('nicos.devices.entangle.Sensor',
        description = 'Coder of detector table inside scatteringtube',
        tangodevice = tango_base + 'det_table/plc/_input_SeilzugPosition',
        unit = 'mm',
    ),
    det_table_cab_temp = device('nicos.devices.entangle.Sensor',
        description = 'Temperature of Controller',
        tangodevice = tango_base + 'det_table/plc/_input_CabTemperature',
        unit = 'degC',
    ),
    det_table_motor_temp = device('nicos.devices.entangle.Sensor',
        description = 'Temperature of Motorcore raise 0.76Deg/min fall 2.78Deg/h',
        tangodevice = tango_base + 'det_table/plc/_input_MotorTemperature',
        unit = 'degC',
    ),
    det_table_motor = device(code_base + 'analogencoder.AnalogMove',
        description = 'correcting error',
        device = 'det_table_raw',
        unit = 'mm',
        poly = [-211.5,  1.00460], # 2021-03-23 09:08:58 GM Laser poly = [-513.0, 0.9955], #2021-03-15 06:58:01 MP QAD Pluto 30Grad
        # poly = [-513.0, 0.9955], # 2021-03-15 06:58:01 MP QAD Pluto 30Grad
        precision = 10,
        visibility = (),
    ),
    det_table_acc = device(code_base + 'accuracy.Accuracy',
        description = 'calc error Motor and poti',
        motor = 'det_table_raw',
        analog = 'det_table_poti',
        visibility = showcase_values['hide_acc'],
        unit = 'mm'
    ),
    det_table = device(code_base + 'focuspoint.FocusPoint',
        description = 'detector table inside scatteringtube with pivot',
        unit = 'mm',
        table = 'det_table_ctrl',
        pivot = 'det_pivot',
        abslimits = [1065, 10864],
    ),
    det_table_ctrl = device(code_base + 'controls.TemperatureControlled',
        description = 'MP only: to check for motor temp',
        device = 'det_table_motor',
        temperature = 'det_table_motor_temp',
        maxtemp = 40,
        timeout = 90,
        unit = 'mm',
        visibility = (),
    ),
    dix_laser_acc = device(code_base + 'accuracy.Accuracy',
        description = 'laser measurement of table accuracy',
        motor = 'det_table_motor',
        analog = 'dix_laser_analog',
        unit = 'mm',
    ),
    dix_laser_analog = device('nicos_mlz.refsans.devices.dimetix.DimetixLaser',
        description = 'laser measurement of table',
        signal = 'dix_laser_signalstrength',
        value = 'dix_laser_value',
        unit = 'mm',
        visibility = (),
    ),
    dix_laser_value = device('nicos.devices.entangle.Sensor',
        description = 'laser measurement system value',
        tangodevice = tango_base + 'test/laser/value',
        visibility = (),
    ),
    dix_laser_signalstrength = device('nicos.devices.entangle.Sensor',
        description = 'laser measurement system signal strength',
        tangodevice = tango_base + 'test/laser/signalstrength',
        unit = '',
        visibility = (),
    ),
    dix_laser_temperature = device('nicos.devices.entangle.Sensor',
        description = 'laser measurement system temperature',
        tangodevice = tango_base + 'test/laser/temperature',
        unit = 'degC',
        visibility = (),
    ),
    tube_angle = device(code_base + 'tube.TubeAngle',
        description = 'Angle between flight tube and ground',
        yoke = 'det_yoke',
    ),
)
