description = 'Static flippers'
group = 'lowlevel'

display_order = 22

#abslimits are defined in .res file!

devices = dict(
    sf_0a = device('nicos.devices.generic.ManualMove',
        description = 'Static flipper arm 0 - A',
        fmtstr = '%.3f',
        pollinterval = 60,
        maxage = 120,
        abslimits = (0, 5),
        # precision = 0.01,
        unit = 'A',
    ),
    sf_0b = device('nicos.devices.generic.ManualMove',
        description = 'Static flipper arm 0 - B',
        fmtstr = '%.3f',
        pollinterval = 60,
        maxage = 120,
        abslimits = (0, 5),
        # precision = 0.01,
        unit = 'A',
    ),
    sf_1 = device('nicos.devices.generic.ManualMove',
        description = 'Static flipper arm 1',
        fmtstr = '%.3f',
        pollinterval = 60,
        maxage = 120,
        abslimits = (0, 5),
        # precision = 0.01,
        unit = 'A',
    ),
    hsf_0a = device('nicos.devices.generic.ManualMove',
        description = 'Helmholtz mezei flipper arm 0 - A',
        fmtstr = '%.3f',
        pollinterval = 60,
        maxage = 120,
        abslimits = (0, 5),
        # precision = 0.01,
        unit = 'A',
    ),
    hsf_0b = device('nicos.devices.generic.ManualMove',
        description = 'Helmholtz mezei flipper arm 0 - B',
        fmtstr = '%.3f',
        pollinterval = 60,
        maxage = 120,
        abslimits = (0, 5),
        # precision = 0.01,
        unit = 'A',
    ),
    hsf_1 = device('nicos.devices.generic.ManualMove',
        description = 'Helmholtz mezei flipper arm 1',
        fmtstr = '%.3f',
        pollinterval = 60,
        maxage = 120,
        abslimits = (0, 5),
        # precision = 0.01,
        unit = 'A',
    ),
)
