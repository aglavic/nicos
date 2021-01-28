description = 'Neutron Grating Interferometer'

group = 'optional'

tango_base = 'tango://192.168.20.64:10000/box/'

devices = dict(
    G0rz = device('nicos.devices.entangle.Motor',
        speed = 1,
        unit = 'deg',
        description = 'Rotation of G0 grating around beam direction',
        tangodevice = tango_base + 'phytron3/mot',
        abslimits = (-400, 400),
        maxage = 5,
        pollinterval = 3,
        precision = 0.01,
    ),
    G0ry = device('nicos.devices.entangle.Motor',
        speed = 1,
        description = 'Rotation of G0 grating around vertical axis',
        tangodevice = tango_base + 'phytron2/mot',
        abslimits = (-1, 400),
        maxage = 5,
        pollinterval = 3,
        precision = 0.01,
        unit = 'deg',
    ),
    G0tz = device('nicos.devices.entangle.Motor',
        speed = 0.5,
        unit = 'mm',
        description = 'Stepping of G0 perpendicular to the beam direction',
        tangodevice = tango_base + 'phytron1/mot',
        abslimits = (-2, 25),
        maxage = 5,
        pollinterval = 3,
        precision = 0.01,
    ),
    G1tx = device('nicos.devices.entangle.Motor',
        speed = 50,
        unit = 'mum',
        description = 'Stepping of G1 perpendicular to the beam direction',
        tangodevice = tango_base + 'phytron8/mot',
        abslimits = (0, 25000),
        userlimits = (0, 25000),
        maxage = 5,
        pollinterval = 3,
        precision = 0.1,
    ),
    G1tz = device('nicos.devices.entangle.Motor',
        speed = 5,
        unit = 'mm',
        description = 'Translation of G1 parallel to the beam direction',
        tangodevice = tango_base + 'phytron4/mot',
        abslimits = (-1, 101),
        userlimits = (0, 100),
        maxage = 5,
        pollinterval = 3,
        precision = 0.001,
    ),
    G1rz = device('nicos.devices.entangle.Motor',
        speed = 5,
        unit = 'deg',
        description = 'Rotation of G1 around the beam axis',
        tangodevice = tango_base + 'phytron7/mot',
        abslimits = (-400, 400),
        userlimits = (-400, 400),
        maxage = 5,
        pollinterval = 3,
        precision = 0.001,
    ),
    G1ry = device('nicos.devices.entangle.Motor',
        speed = 5,
        unit = 'deg',
        description = 'Rotation of G1 around the y-axis',
        tangodevice = tango_base + 'phytron5/mot',
        abslimits = (-400,400),
        userlimits = (-400,400),
        maxage = 5,
        pollinterval = 3,
        precision = 0.001,
    ),
    G1gx = device('nicos.devices.entangle.Motor',
        speed = 5,
        unit = 'deg',
        description = 'Rotation of G1 around the x-axis',
        tangodevice = tango_base + 'phytron6/mot',
        abslimits = (-20, 20),
        userlimits = (-20, 20),
        maxage = 5,
        pollinterval = 3,
        precision = 0.001,
    ),
)
'''
    G2rz_p = device('nicos.devices.entangle.Motor',
        speed = 0.2,
        unit = 'deg',
        description = 'Rotation of G1 grating around beam direction',
        tangodevice = tango_base + 'fzjs7/G1rz',
        abslimits = (-400, 400),
        maxage = 5,
        pollinterval = 3,
        precision = 0.0005,
    ),
    G2tz = device('nicos.devices.entangle.Motor',
        speed = 1,
        unit = 'mm',
        description = 'Translation of G1 in beam direction. (Talbot distance)',
        tangodevice = tango_base + 'fzjs7/G1tz',
        abslimits = (0, 20),
        maxage = 5,
        pollinterval = 3,
        precision = 0.05,
    ),
    G2rz = device('nicos.devices.entangle.Motor',
        speed = 1,
        unit = 'deg',
        description = 'Rotation of G2 and G1 around beam axis',
        tangodevice = tango_base + 'fzjs7/G12rz',
        abslimits = (-400, 400),
        userlimits = (-250, 250),
        maxage = 5,
        pollinterval = 3,
        precision = 0.01,
    ),
'''
