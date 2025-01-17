description = 'JJ XRAY sample slits'
group = 'lowlevel'

tango_base = 'tango://kompasshw.kompass.frm2:10000/kompass/'

devices = dict(
    ss1r = device('nicos.devices.entangle.Motor',
        visibility = (),
        tangodevice = tango_base + 'sampleslit/ss1h2',
        precision = 0.1,
    ),
    ss1l = device('nicos.devices.entangle.Motor',
        visibility = (),
        tangodevice = tango_base + 'sampleslit/ss1h1',
        precision = 0.1,
    ),
    ss1b = device('nicos.devices.entangle.Motor',
        visibility = (),
        tangodevice = tango_base + 'sampleslit/ss1v2',
        precision = 0.1,
    ),
    ss1t = device('nicos.devices.entangle.Motor',
        visibility = (),
        tangodevice = tango_base + 'sampleslit/ss1v1',
        precision = 0.1,
    ),
    ss1 = device('nicos.devices.generic.Slit',
        description = 'First sample slit',
        left = 'ss1l',
        right = 'ss1r',
        bottom = 'ss1b',
        top = 'ss1t',
        opmode = 'offcentered',
        coordinates = 'opposite',
    ),
    ss2r = device('nicos.devices.entangle.Motor',
        visibility = (),
        tangodevice = tango_base + 'sampleslit/ss2h2',
        precision = 0.1,
    ),
    ss2l = device('nicos.devices.entangle.Motor',
        visibility = (),
        tangodevice = tango_base + 'sampleslit/ss2h1',
        precision = 0.1,
    ),
    ss2b = device('nicos.devices.entangle.Motor',
        visibility = (),
        tangodevice = tango_base + 'sampleslit/ss2v2',
        precision = 0.1,
    ),
    ss2t = device('nicos.devices.entangle.Motor',
        visibility = (),
        tangodevice = tango_base + 'sampleslit/ss2v1',
        precision = 0.1,
    ),
    ss2 = device('nicos.devices.generic.Slit',
        description = 'Second sample slit',
        left = 'ss2l',
        right = 'ss2r',
        bottom = 'ss2b',
        top = 'ss2t',
        opmode = 'offcentered',
        coordinates = 'opposite',
    ),
)
