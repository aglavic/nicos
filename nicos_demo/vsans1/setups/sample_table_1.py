description = 'bottom sample table devices'

group = 'lowlevel'

devices = dict(
    st1_omg = device('nicos.devices.generic.Axis',
        description = 'table 1 omega axis',
        pollinterval = 15,
        maxage = 60,
        fmtstr = '%.2f',
        abslimits = (-180, 180),
        precision = 0.01,
        motor = 'st1_omgmot',
    ),
    st1_omgmot = device('nicos.devices.generic.VirtualMotor',
        description = 'table 1 omega motor',
        fmtstr = '%.2f',
        abslimits = (-180, 180),
        visibility = (),
        unit = 'deg',
    ),
    st1_chi = device('nicos.devices.generic.Axis',
        description = 'table 1 chi axis',
        pollinterval = 15,
        maxage = 60,
        fmtstr = '%.2f',
        abslimits = (-5, 5),
        precision = 0.01,
        motor = 'st1_chimot',
    ),
    st1_chimot = device('nicos.devices.generic.VirtualMotor',
        description = 'table 1 chi motor',
        fmtstr = '%.2f',
        abslimits = (-5, 5),
        visibility = (),
        unit = 'deg',
    ),
    st1_phi = device('nicos.devices.generic.Axis',
        description = 'table 1 phi axis',
        pollinterval = 15,
        maxage = 60,
        fmtstr = '%.2f',
        abslimits = (-5, 5),
        precision = 0.01,
        motor = 'st1_phimot',
    ),
    st1_phimot = device('nicos.devices.generic.VirtualMotor',
        description = 'table 1 phi motor',
        fmtstr = '%.2f',
        abslimits = (-5, 5),
        visibility = (),
        unit = 'deg',
    ),
    st1_y = device('nicos.devices.generic.Axis',
        description = 'table 1 y axis',
        pollinterval = 15,
        maxage = 60,
        fmtstr = '%.2f',
        abslimits = (-99, 99),
        precision = 0.01,
        motor = 'st1_ymot',
    ),
    st1_ymot = device('nicos.devices.generic.VirtualMotor',
        description = 'table 1 y motor',
        fmtstr = '%.2f',
        abslimits = (-99, 99),
        visibility = (),
        unit = 'mm',
    ),
    st1_z = device('nicos.devices.generic.Axis',
        description = 'table 1 z axis',
        pollinterval = 15,
        maxage = 60,
        fmtstr = '%.2f',
        abslimits = (-50, 50),
        precision = 0.01,
        motor = 'st1_zmot',
    ),
    st1_zmot = device('nicos.devices.generic.VirtualMotor',
        description = 'table 1 z motor',
        fmtstr = '%.2f',
        abslimits = (-50, 50),
        visibility = (),
        curvalue = -31,
        unit = 'mm',
    ),
    st1_x = device('nicos.devices.generic.Axis',
        description = 'table 1 x axis',
        pollinterval = 15,
        maxage = 60,
        fmtstr = '%.2f',
        abslimits = (-500.9, 110.65),
        precision = 0.01,
        motor = 'st1_xmot',
    ),
    st1_xmot = device('nicos.devices.generic.VirtualMotor',
        description = 'table 1 x motor',
        fmtstr = '%.2f',
        abslimits = (-750, 150),
        visibility = (),
        unit = 'mm',
    ),
)
