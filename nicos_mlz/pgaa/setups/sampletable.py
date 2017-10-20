description = 'XYZ-Omega sample table'

group = 'lowlevel'

excludes = ['sample']

nethost = 'pgaasrv.pgaa.frm2'

devices = dict(
    x_m = device('nicos.devices.taco.Motor',
        description = 'X axis sample table motor',
        tacodevice = '//%s/pgaa/huber/mx' % nethost,
        abslimits = (0, 200),
        userlimits = (0, 200),
        lowlevel = True,
    ),
    x_e = device('nicos.devices.taco.Coder',
        description = 'X axis sample table encoder',
        tacodevice = '//%s/pgaa/huber/ex' % nethost,
        lowlevel = True,
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
    y_m = device('nicos.devices.taco.Motor',
        description = 'Y axis sample table motor',
        tacodevice = '//%s/pgaa/huber/my' % nethost,
        abslimits = (0, 200),
        userlimits = (0, 200),
        lowlevel = True,
    ),
    y_e = device('nicos.devices.taco.Coder',
        description = 'Y axis sample table encoder',
        tacodevice = '//%s/pgaa/huber/ey' % nethost,
        lowlevel = True,
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
    z_m = device('nicos.devices.taco.Motor',
        description = 'Z axis sample table motor',
        tacodevice = '//%s/pgaa/huber/mz' % nethost,
        abslimits = (0, 200),
        userlimits = (0, 200),
        lowlevel = True,
    ),
    z_e = device('nicos.devices.taco.Coder',
        description = 'Z axis sample table encoder',
        tacodevice = '//%s/pgaa/huber/ez' % nethost,
        lowlevel = True,
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
    omega_m = device('nicos.devices.taco.Motor',
        description = 'Omega axis sample table motor',
        tacodevice = '//%s/pgaa/huber/mw' % nethost,
        abslimits = (0, 361),
        userlimits = (0, 361),
        lowlevel = True,
    ),
    omega_e = device('nicos.devices.taco.Coder',
        description = 'Z axis sample table encoder',
        tacodevice = '//%s/pgaa/huber/ew' % nethost,
        lowlevel = True,
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
