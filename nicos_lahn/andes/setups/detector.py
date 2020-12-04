description = 'detector setup'

group = 'lowlevel'

sysconfig = dict(
    datasinks = ['tifformat'],
)

devices = dict(
    monitor = device('nicos.devices.generic.VirtualCounter',
        description = 'simulated monitor',
        fmtstr = '%d',
        type = 'monitor',
        lowlevel = True,
    ),
    timer = device('nicos.devices.generic.VirtualTimer',
        description = 'simulated timer',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    image = device('nicos.devices.generic.VirtualImage',
        description = 'Image data device',
        fmtstr = '%d',
        sizes = (256, 256),
        lowlevel = True,
    ),
    cam = device('nicos.devices.generic.Detector',
        description = 'classical detector',
        timers = ['timer'],
        monitors = ['monitor'],
        images = ['image'],
    ),
    lsd = device("nicos.devices.generic.Axis",
        description = "detector arm translation",
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (900, 1500),
            unit = 'mm',
            speed = 1,
        ),
        precision = 0.01,
        fmtstr = "%.2f",
    ),
    lsd_opMode = device('nicos.devices.generic.Switcher',
        description = 'detector arm operation modes',
        moveable = 'lsd',
        mapping = {
            'min': 900,
            'lsd': 1100,
        },
        precision = 0.01,
        unit = '',
        lowlevel = True,
    ),
)
