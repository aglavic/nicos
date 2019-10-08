description = 'Slits'

group = 'lowlevel'

devices = dict(
    s1_left = device('nicos.devices.generic.VirtualMotor',
        description = 'Left blade of slit 1',
        abslimits = (-17.2, 24.799),
        unit = 'mm',
        precision = 0.01,
        fmtstr = '%.2f',
        lowlevel = False,
    ),
    s1_right = device('nicos.devices.generic.VirtualMotor',
        description = 'Right blade of slit 1',
        abslimits = (-28.702, 15.298),
        unit = 'mm',
        precision = 0.01,
        fmtstr = '%.2f',
        lowlevel = False,
    ),
    s1_bottom = device('nicos.devices.generic.VirtualMotor',
        description = 'Bottom blade of slit 1',
        abslimits = (-41.25, 58.75),
        unit = 'mm',
        precision = 0.01,
        fmtstr = '%.2f',
        lowlevel = False,
    ),
    s1_top = device('nicos.devices.generic.VirtualMotor',
        description = 'Left blade of slit 1',
        abslimits = (-57.702, 42.298),
        unit = 'mm',
        precision = 0.01,
        fmtstr = '%.2f',
        lowlevel = False,
    ),
    s1 = device('nicos.devices.generic.Slit',
        description = 'Slit 1',
        left = 's1_left',
        right = 's1_right',
        bottom = 's1_bottom',
        top = 's1_top',
        opmode = 'centered',
        coordinates = 'opposite',
    ),
    s2_left = device('nicos.devices.generic.VirtualMotor',
        description = 'Left blade of slit 2',
        abslimits = (-18.346, 18.754),
        unit = 'mm',
        precision = 0.01,
        fmtstr = '%.2f',
        lowlevel = False,
    ),
    s2_right = device('nicos.devices.generic.VirtualMotor',
        description = 'Right blade of slit 2',
        abslimits = (-16.69, 20.745),
        unit = 'mm',
        precision = 0.01,
        fmtstr = '%.2f',
        lowlevel = False,
    ),
    s2_bottom = device('nicos.devices.generic.VirtualMotor',
        description = 'Bottom blade of slit 2',
        abslimits = (-25.75, 37.25),
        unit = 'mm',
        precision = 0.01,
        fmtstr = '%.2f',
        lowlevel = False,
    ),
    s2_top = device('nicos.devices.generic.VirtualMotor',
        description = 'Top blade of slit 2',
        abslimits = (-35.949, 26.451),
        unit = 'mm',
        precision = 0.01,
        fmtstr = '%.2f',
        lowlevel = False,
    ),
    s2 = device('nicos.devices.generic.Slit',
        description = 'Slit 2',
        left = 's2_left',
        right = 's2_right',
        bottom = 's2_bottom',
        top = 's2_top',
        opmode = 'centered',
        coordinates = 'opposite',
    ),
)
