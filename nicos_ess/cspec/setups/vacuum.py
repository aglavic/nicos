description = 'Vacuum gauges in the neutron guide'

devices = dict(
    vac1 = device('nicos.devices.generic.VirtualMotor',
        description = 'Vacuum sensor 1 in neutron guide',
        abslimits = (0, 1000),
        pollinterval = 10,
        maxage = 12,
        unit = 'mbar',
        curvalue = 1.1e-4,
        fmtstr = '%.2e',
        jitter = 1.e-5,
    ),
    vac2 = device('nicos.devices.generic.VirtualMotor',
        description = 'Vacuum sensor 2 in neutron guide',
        abslimits = (0, 1000),
        pollinterval = 10,
        maxage = 12,
        unit = 'mbar',
        curvalue = 1.2e-4,
        fmtstr = '%.2e',
        jitter = 1.e-5,
    ),
    vac3 = device('nicos.devices.generic.VirtualMotor',
        description = 'Vacuum sensor 3 in neutron guide',
        abslimits = (0, 1000),
        pollinterval = 10,
        maxage = 12,
        unit = 'mbar',
        curvalue = 1.5e-4,
        fmtstr = '%.2e',
        jitter = 1.e-5,
    ),
    vac4 = device('nicos.devices.generic.VirtualMotor',
        description = 'Vacuum sensor 4 in neutron guide',
        abslimits = (0, 1000),
        pollinterval = 10,
        maxage = 12,
        unit = 'mbar',
        curvalue = 1.1e-4,
        fmtstr = '%.2e',
        jitter = 1.e-5,
    ),
    vac5 = device('nicos.devices.generic.VirtualMotor',
        description = 'Vacuum sensor 5 in neutron guide',
        abslimits = (0, 1000),
        pollinterval = 10,
        maxage = 12,
        unit = 'mbar',
        curvalue = 1.3e-4,
        fmtstr = '%.2e',
        jitter = 1.e-5,
    ),
    vac6 = device('nicos.devices.generic.VirtualMotor',
        description = 'Vacuum sensor 6 in neutron guide',
        abslimits = (0, 1000),
        pollinterval = 10,
        maxage = 12,
        unit = 'mbar',
        curvalue = 1.2e-4,
        fmtstr = '%.2e',
        jitter = 1.e-5,
    ),
    vac7 = device('nicos.devices.generic.VirtualMotor',
        description = 'Vacuum sensor 7 in neutron guide',
        abslimits = (0, 1000),
        pollinterval = 10,
        maxage = 12,
        unit = 'mbar',
        curvalue = 1.1e-4,
        fmtstr = '%.2e',
        jitter = 1.e-5,
    ),
)
