description = 'CCR with sapphire windows, with LS336 controller'

group = 'plugplay'

includes = ['alias_T']

tango_base = 'tango://%s:10000/box/' % setupname

devices = {
    'T_%s' % setupname : device('nicos_mlz.devices.ccr.CCRControl',
        description = 'The main temperature control device of the CCR',
        stick = 'T_%s_stick' % setupname,
        tube = 'T_%s_tube' % setupname,
        unit = 'K',
        fmtstr = '%.3f',
    ),
    'T_%s_stick' % setupname : device('nicos.devices.entangle.TemperatureController',
        description = 'The control device of the sample (stick)',
        tangodevice = tango_base + 'stick/control1',
        unit = 'K',
        fmtstr = '%.3f',
    ),
    'T_%s_tube' % setupname : device('nicos.devices.entangle.TemperatureController',
        description = 'The control device of the tube',
        tangodevice = tango_base + 'tube/control2',
        warnlimits = (0, 300),
        unit = 'K',
        fmtstr = '%.3f',
    ),
    'T_%s_stick_range' % setupname : device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Heater range',
        tangodevice = tango_base + 'stick/range1',
        warnlimits = ('high', 'medium'),
        mapping = {'off': 0, 'low': 1, 'medium': 2, 'high': 3},
        unit = '',
    ),
    'T_%s_tube_range' % setupname : device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Heater range',
        tangodevice = tango_base + 'tube/range2',
        warnlimits = ('high', 'medium'),
        mapping = {'off': 0, 'low': 1, 'medium': 2, 'high': 3},
        unit = '',
    ),
    'T_%s_A' % setupname : device('nicos.devices.entangle.Sensor',
        description = '(regulation) Sample temperature',
        tangodevice = tango_base + 'sample/sensora',
        unit = 'K',
        fmtstr = '%.3f',
    ),
    'T_%s_B' % setupname : device('nicos.devices.entangle.Sensor',
        description = 'Temperature at the stick',
        tangodevice = tango_base + 'stick/sensorb',
        unit = 'K',
        fmtstr = '%.3f',
    ),
    'T_%s_C' % setupname : device('nicos.devices.entangle.Sensor',
        description = 'Coldhead temperature',
        tangodevice = tango_base + 'coldhead/sensorc',
        unit = 'K',
        fmtstr = '%.3f',
    ),
    'T_%s_D' % setupname : device('nicos.devices.entangle.Sensor',
        description = '(regulation) Temperature at '
        'thermal coupling to the tube',
        tangodevice = tango_base + 'tube/sensord',
        warnlimits = (0, 300),
        unit = 'K',
        fmtstr = '%.3f',
    ),
    'p_%s' % setupname : device('nicos.devices.entangle.Sensor',
        description = 'Pressure in sample tube',
        tangodevice = tango_base + 'pressure/ch1',
        unit = 'mbar',
        fmtstr = '%.3f',
    ),
#    '%s_gas_switch' % setupname : device('nicos.devices.entangle.NamedDigitalOutput',
#        description = 'Switch for the gas valve',
#        tangodevice = tango_base + 'plc/gas',
#        mapping = {'on': 1, 'off': 0},
#    ),
#    '%s_vacuum_switch' % setupname : device('nicos.devices.entangle.NamedDigitalOutput',
#        description = 'Switch for the vacuum valve',
#        tangodevice = tango_base + 'plc/vacuum',
#        mapping = {'on': 1, 'off': 0},
#    ),
}

alias_config = {
    'T':  {'T_%s_tube' % setupname: 200, 'T_%s_stick' % setupname: 150},
    'Ts': {'T_%s_A' % setupname: 100, 'T_%s_B' % setupname: 90, 'T_%s_D' % setupname: 20},
}
