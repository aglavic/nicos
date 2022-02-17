description = 'FRM II 5.5 T superconducting magnet'

group = 'plugplay'

includes = ['alias_B', 'alias_sth']

tango_base = 'tango://%s:10000/box/' % setupname

devices = {
    'B_%s' % setupname: device('nicos.devices.entangle.Actuator',
        description = 'The magnetic field',
        tangodevice = tango_base + 'magnet/field',
        abslimits = (-5.555, 5.555),
    ),
    'sth_%s' % setupname: device('nicos.devices.generic.Axis',
        description = 'Cryotstat tube rotation',
        abslimits = (-180, 180),
        motor = device('nicos.devices.entangle.Motor',
            tangodevice = tango_base + 'motor/motor',
            visibility = (),
            ),
        coder = device('nicos.devices.entangle.Sensor',
            tangodevice = tango_base + 'motor/encoder',
            visibility = (),
            ),
        precision = 0.001,
    ),
}

# Maximum temeratures for field operation above 80A taken from the manual
maxtemps = [None, 4.3, 4.3, 5.1, 4.7, None, None, None, 4.3]

for i in range(1, 9):
    dev = device('nicos.devices.entangle.Sensor',
        description = '5.5T magnet temperature sensor %d' % i,
        tangodevice = tango_base + 'lakeshore/sensor%d' % i,
        warnlimits = (0, maxtemps[i]),
        pollinterval = 30,
        maxage = 90,
        unit = 'K',
    )
    devices['%s_T%d' % (setupname, i)] = dev

alias_config = {
    'B':   {'B_%s' % setupname: 100},
    'sth': {'sth_%s' % setupname: 100},
}

extended = dict(
    representative = 'B_%s' % setupname,
)
