description = 'XYZ-Omega sample table'

group = 'lowlevel'

excludes = ['samplechanger']

tango_base = 'tango://pgaahw.pgaa.frm2.tum.de:10000/pgaa/huber/'

devices = dict(
    x_m = device('nicos.devices.entangle.Motor',
        description = 'X axis sample table motor',
        tangodevice = tango_base + 'mx',
        abslimits = (0, 200),
        userlimits = (0, 200),
        visibility = (),
    ),
    x_e = device('nicos.devices.entangle.Sensor',
        description = 'X axis sample table encoder',
        tangodevice = tango_base + 'ex',
        visibility = (),
    ),
    x = device('nicos.devices.generic.Axis',
        description = 'X translation of the sample table',
        motor = 'x_m',
        coder = 'x_m',
        precision = 0.01,
        abslimits = (0, 200),
        pollinterval = 11,
        maxage = 13,
    ),
    y_m = device('nicos.devices.entangle.Motor',
        description = 'Y axis sample table motor',
        tangodevice = tango_base + 'my',
        abslimits = (0, 200),
        userlimits = (0, 200),
        visibility = (),
    ),
    y_e = device('nicos.devices.entangle.Sensor',
        description = 'Y axis sample table encoder',
        tangodevice = tango_base + 'ey',
        visibility = (),
    ),
    y = device('nicos.devices.generic.Axis',
        description = 'Y translation of the sample table',
        motor = 'y_m',
        coder = 'y_m',
        precision = 0.01,
        abslimits = (0, 200),
        pollinterval = 11,
        maxage = 13,
    ),
    z_m = device('nicos.devices.entangle.Motor',
        description = 'Z axis sample table motor',
        tangodevice = tango_base + 'mz',
        abslimits = (0, 200),
        userlimits = (0, 200),
        visibility = (),
    ),
    z_e = device('nicos.devices.entangle.Sensor',
        description = 'Z axis sample table encoder',
        tangodevice = tango_base + 'ez',
        visibility = (),
    ),
    z = device('nicos.devices.generic.Axis',
        description = 'Z translation of the sample table',
        motor = 'z_m',
        coder = 'z_m',
        precision = 0.01,
        abslimits = (0, 200),
        pollinterval = 11,
        maxage = 13,
    ),
    omega_m = device('nicos.devices.entangle.Motor',
        description = 'Omega axis sample table motor',
        tangodevice = tango_base + 'mw',
        abslimits = (0, 361),
        userlimits = (0, 361),
        visibility = (),
    ),
    omega_e = device('nicos.devices.entangle.Sensor',
        description = 'Omega axis sample table encoder',
        tangodevice = tango_base + 'ew',
        visibility = (),
    ),
    omega = device('nicos.devices.generic.Axis',
        description = 'Rotation of the sample table',
        motor = 'omega_m',
        coder = 'omega_m',
        precision = 0.01,
        abslimits = (0, 361),
        pollinterval = 11,
        maxage = 13,
    ),
)
