description = 'Neutron Grating Interferometer'

group = 'optional'

excludes = ['ngi']

tango_base_phy1 = 'tango://phytron1.antares.frm2.tum.de:10000/box/'
tango_base_phy3 = 'tango://phytron2.antares.frm2.tum.de:10000/box/'

devices = dict(
    G0rz = device('nicos.devices.entangle.Motor',
        speed = 1,
        unit = 'deg',
        description = 'Rotation of G0 grating around beam direction',
        tangodevice = tango_base_phy1 + 'phytron3/mot',
        abslimits = (-400, 400),
        maxage = 5,
        pollinterval = 3,
        precision = 0.01,
    ),
    G0ry = device('nicos.devices.entangle.Motor',
        speed = 1,
        unit = 'deg',
        description = 'Rotation of G0 grating around vertical axis',
        tangodevice = tango_base_phy1 + 'phytron2/mot',
        abslimits = (-1, 400),
        maxage = 5,
        pollinterval = 3,
        precision = 0.01,
    ),
    G0tz = device('nicos.devices.entangle.Motor',
        speed = 0.5,
        unit = 'mm',
        description = 'Stepping of G0 perpendicular to the beam direction',
        tangodevice = tango_base_phy1 + 'phytron1/mot',
        abslimits = (-2, 25),
        maxage = 5,
        pollinterval = 3,
        precision = 0.01,
    ),
    G1tx = device('nicos.devices.entangle.Motor',
        speed = 50,
        unit = 'mum',
        description = 'Stepping of G1 perpendicular to the beam direction',
        tangodevice = tango_base_phy1 + 'phytron8/mot',
        abslimits = (-12500, 12500),
        userlimits = (-12500, 12500),
        maxage = 5,
        pollinterval = 3,
        precision = 0.1,
    ),
    G1tz = device('nicos.devices.entangle.Motor',
        speed = 5,
        unit = 'mm',
        description = 'Translation of G1 parallel to the beam direction',
        tangodevice = tango_base_phy1 + 'phytron4/mot',
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
        tangodevice = tango_base_phy1 + 'phytron7/mot',
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
        tangodevice = tango_base_phy1 + 'phytron5/mot',
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
        tangodevice = tango_base_phy1 + 'phytron6/mot',
        abslimits = (-20, 20),
        userlimits = (-20, 20),
        maxage = 5,
        pollinterval = 3,
        precision = 0.001,
    ),

    G2tz = device('nicos.devices.entangle.Motor',
        speed = 1,
        unit = 'mm',
        description = 'Translation of G1 in beam direction. (Talbot distance)',
        tangodevice = tango_base_phy3 + 'phytron4/mot',
        abslimits = (0, 20),
        maxage = 5,
        pollinterval = 3,
        precision = 0.05,
    ),

    G2rz_mot = device('nicos.devices.entangle.Motor',
        description = 'G2rz motor',
        tangodevice = tango_base_phy3 + 'phytron1/mot',
        lowlevel = True,
    ),
    G2rz_enc = device('nicos.devices.entangle.Sensor',
        description = 'G2rz encoder',
        tangodevice = tango_base_phy3 + 'phytron1/enc',
        lowlevel = True,
    ),
    G2rz = device('nicos.devices.generic.Axis',
        description = 'Rotation of G2 around beam axis',
        speed = 1,
        unit = 'deg',
        pollinterval = 5,
        maxage = 10,
        precision = 0.01,
        abslimits = (-60, 50),
        userlimits = (-60, 50),
        fmtstr = '%.2f',
        motor = 'G2rz_mot',
        coder = 'G2rz_enc',
        backlash = -1,
    ),
    G2rz_p_mot = device('nicos.devices.entangle.Motor',
        description = 'G2rz_p motor',
        tangodevice = tango_base_phy3 + 'phytron3/mot',
        lowlevel = True,
    ),
    G2rz_p_enc = device('nicos.devices.entangle.Sensor',
        description = 'G2rz_p encoder',
        tangodevice = tango_base_phy3 + 'phytron3/enc',
        lowlevel = True,
    ),
    G2rz_p = device('nicos.devices.generic.Axis',
        description = 'Precise rotation of G2 around beam axis',
        speed = 0.1,
        unit = 'deg',
        pollinterval = 5,
        maxage = 10,
        precision = 0.0005,
        abslimits = (-30, 30),
        userlimits = (-30, 30),
        fmtstr = '%.2f',
        motor = 'G2rz_p_mot',
        coder = 'G2rz_p_enc',
        backlash = -1,
    ),
)
