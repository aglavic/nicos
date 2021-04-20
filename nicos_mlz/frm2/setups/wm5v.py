description = 'Wet vertical 5T magnet'

group = 'plugplay'
includes = ['alias_T']

tango_base = 'tango://%s:10000/box/' % setupname

devices = {
    '%s_piso' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'Isolation vacuum pressure',
        tangodevice = tango_base + 'pressure/ch1',
        fmtstr = '%.3e',
    ),
    '%s_pvti' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'VTI pressure',
        tangodevice = tango_base + 'pressure/ch2',
        fmtstr = '%.3g',
    ),
    '%s_psample' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'Sample space pressure',
        tangodevice = tango_base + 'pressure/ch3',
        fmtstr = '%.3g',
    ),
    '%s_lhe' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'Liquid helium level',
        tangodevice = tango_base + 'levelmeter/level',
        fmtstr = '%.0f',
        warnlimits = (120, 700),
        unit = 'mm',
    ),
    '%s_lhe_mode' % setupname: device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Readout mode of the levelmeter',
        tangodevice = tango_base + 'levelmeter/mode',
        mapping = {'standby': 0, 'slow': 1, 'fast': 2, 'continuous': 3},
        warnlimits = ('slow', 'slow'),
    ),
    'T_%s_magnet' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'Coil temperature',
        tangodevice = tango_base + 'ls336/sensora',
        unit = 'K',
    ),
    'T_%s_vti' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'VTI temperature',
        tangodevice = tango_base + 'ls336/control2',
        unit = 'K',
    ),
    'T_%s_sample' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'Sample thermometer temperature',
        tangodevice = tango_base + 'ls336/control1',
        unit = 'K',
    ),
    '%s_vti_heater' % setupname: device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Heater range for VTI',
        tangodevice = tango_base + 'ls336/range2',
        warnlimits = ('high', 'medium'),
        mapping = {'off': 0, 'low': 1, 'medium': 2, 'high': 3},
        unit = '',
    ),
    '%s_sample_heater' % setupname: device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Heater range for sample temperature',
        tangodevice = tango_base + 'ls336/range1',
        warnlimits = ('high', 'medium'),
        mapping = {'off': 0, 'low': 1, 'medium': 2, 'high': 3},
        unit = '',
    ),
    '%s_nv_reg' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'Needle valve regulation setpoint',
        tangodevice = tango_base + 'nv/regulation',
        unit = 'mbar',
    ),
    '%s_nv_manual' % setupname: device('nicos.devices.entangle.AnalogOutput',
        description = 'Needle valve opening',
        tangodevice = tango_base + 'ls336/control3mout',
    ),
    'I_%s' % setupname: device('nicos.devices.entangle.RampActuator',
        description = 'Current in the magnet',
        tangodevice = tango_base + 'supply/field',
        precision = 60,
    ),
    'I_%s_supply' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'Current output of the power supply',
        tangodevice = tango_base + 'supply/actual',
    ),
}

alias_config = {
    'T':  {'T_%s_vti' % setupname: 200, 'T_%s_sample' % setupname: 190},
    'Ts': {'T_%s_sample' % setupname: 200, 'T_%s_vti' % setupname: 190},
}

extended = dict(
    representative = 'I_%s' % setupname,
)
