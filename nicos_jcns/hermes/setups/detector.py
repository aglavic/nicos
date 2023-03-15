description = 'HERMES detector collimators'
group = 'optional'
display_order = 4

tango_base = 'tango://phys.hermes.jcns.fz-juelich.de:10000/hermes/'

devices = dict(
    detangle = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/detangle',
        description = 'Detector angle.',
    ),
    detz = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/detz',
        description = 'Detector vertical translation.',
    ),
    d0t = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/d0t',
        description = 'Detector collimator 1 top blade.',
    ),
    d0b = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/d1b',
        description = 'Detector collimator 0 bottom blade.',
    ),
    d0 = device('nicos.devices.generic.slit.VerticalGap',
        description = 'Detector collimator 0 slit.',
        bottom = 'd0b',
        top = 'd0t',
        coordinates = 'opposite',
        opmode = 'offcentered',
    ),
    d1t = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/d1t',
        description = 'Detector collimator 1 top blade.',
    ),
    d1b = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/d1b',
        description = 'Detector collimator 1 bottom blade.',
    ),
    d1 = device('nicos.devices.generic.slit.VerticalGap',
        description = 'Detector collimator 1 slit.',
        bottom = 'd1b',
        top = 'd1t',
        coordinates = 'opposite',
        opmode = 'offcentered',
    ),
    d2t = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/d2t',
        description = 'Detector collimator 2 top blade.',
    ),
    d2b = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/d2b',
        description = 'Detector collimator 2 bottom blade.',
    ),
    d2 = device('nicos.devices.generic.slit.VerticalGap',
        description = 'Detector collimator 2 slit.',
        bottom = 'd2b',
        top = 'd2t',
        coordinates = 'opposite',
        opmode = 'offcentered',
    ),
    d3t = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/d3t',
        description = 'Detector collimator 3 top blade.',
    ),
    d3b = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'euromove_motor/d3b',
        description = 'Detector collimator 3 bottom blade.',
    ),
    d3 = device('nicos.devices.generic.slit.VerticalGap',
        description = 'Detector collimator 3 slit.',
        bottom = 'd3b',
        top = 'd3t',
        coordinates = 'opposite',
        opmode = 'offcentered',
    ),
)
