description = '3He/4He dilution unit from FRM II Sample environment group'

group = 'plugplay'

includes = ['alias_T']

nethost = setupname

tango_base = "tango://%s:10000/box/" % setupname

devices = {
    'T_%s_pot' % setupname: device('nicos.devices.tango.TemperatureController',
        description = 'The control device of the 3He-pot',
        tangodevice = tango_base + 'lakeshore/control',
        abslimits = (0, 300),
        unit = 'K',
        fmtstr = '%.3f',
        pollinterval = 5,
        maxage = 6,
    ),
    'T_%s_pot_heaterrange' % setupname: device('nicos.devices.generic.Switcher',
        description = 'Heater range of 3He-pot',
        moveable = device('nicos.devices.tango.AnalogOutput',
            tangodevice = tango_base + 'lakeshore/heaterrange',
            description = '',
            lowlevel = True,
            unit = '',),
        precision = 0.5,
        mapping = {'off': 0, '1 mW': 1, '10 mW': 2, '100 mW': 3,
                  # '1 W': 4, '10 W': 5
                  },
    ),
    'T_%s_sample' % setupname: device('nicos.devices.tango.Sensor',
        description = 'The sample temperature (if installed)',
        tangodevice = tango_base + 'lakeshore/sensorb',
        unit = 'K',
        fmtstr = '%.3f',
        pollinterval = 5,
        maxage = 6,
    ),
    'T_%s_sample2' % setupname: device('nicos.devices.tango.Sensor',
        description = 'The 2(nd) sample temperature (if installed)',
        tangodevice = tango_base + 'lakeshore/sensorc',
        unit = 'K',
        fmtstr = '%.3f',
        pollinterval = 5,
        maxage = 6,
    ),
    '%s_p_pot' % setupname: device('nicos.devices.tango.AnalogInput',
        description = 'Pressure at 3He-pot, also at turbo pump inlet',
        tangodevice = tango_base + 'i7000/p_still',
        fmtstr = '%.4g',
        pollinterval = 15,
        maxage = 20,
    ),
    '%s_p_inlet' % setupname: device('nicos.devices.tango.AnalogInput',
        description = 'Pressure forepump inlet, also at turbo pup outlet',
        tangodevice = tango_base + 'i7000/p_inlet',
        fmtstr = '%.4g',
        pollinterval = 15,
        maxage = 20,
    ),
    '%s_p_outlet' % setupname: device('nicos.devices.tango.AnalogInput',
        description = 'Pressure forepump outlet, also at compressor inlet',
        tangodevice = tango_base + 'i7000/p_outlet',
        fmtstr = '%.4g',
        pollinterval = 15,
        maxage = 20,
    ),
    '%s_p_cond' % setupname: device('nicos.devices.tango.AnalogInput',
        description = 'Condensing pressure, also at compressor outlet',
        tangodevice = tango_base + 'i7000/p_cond',
        fmtstr = '%.4g',
        pollinterval = 15,
        maxage = 20,
    ),
    '%s_p_tank' % setupname: device('nicos.devices.tango.AnalogInput',
        description = 'Pressure in 3He-gas reservoir',
        tangodevice = tango_base + 'i7000/p_dump',
        fmtstr = '%.4g',
        pollinterval = 15,
        maxage = 20,
    ),
    '%s_p_vac' % setupname: device('nicos.devices.tango.AnalogInput',
        description = 'Pressure in vacuum dewar',
        tangodevice = tango_base + 'i7000/p_vac',
        fmtstr = '%.4g',
        pollinterval = 15,
        maxage = 20,
    ),
    '%s_flow' % setupname: device('nicos.devices.tango.AnalogInput',
        description = 'Gas flow',
        tangodevice = tango_base + 'i7000/flow',
        fmtstr = '%.4g',
        unit = 'ml/min',
        pollinterval = 15,
        maxage = 20,
    ),
    '%s_p_v15' % setupname: device('nicos.devices.tango.AnalogInput',
        description = 'Pressure at pumping side of V15',
        tangodevice = tango_base + 'i7000/p_v15',
        fmtstr = '%.4g',
        pollinterval = 15,
        maxage = 20,
    ),
}

alias_config = {
    'T':  {'T_%s_pot' % setupname: 300},
    'Ts': {'T_%s_pot' % setupname: 280, 'T_%s_sample' % setupname: 300,
           'T_%s_sample2' % setupname: 290},
}
