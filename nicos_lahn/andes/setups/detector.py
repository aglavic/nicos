description = 'detector setup'

group = 'lowlevel'

devices = dict(
    monitor = device('nicos.devices.generic.VirtualCounter',
        description = 'simulated monitor',
        fmtstr = '%d',
        type = 'monitor',
        visibility = (),
    ),
    timer = device('nicos.devices.generic.VirtualTimer',
        description = 'simulated timer',
        fmtstr = '%.2f',
        visibility = (),
    ),
    image = device('nicos.devices.generic.VirtualImage',
        description = 'Image data device',
        fmtstr = '%d',
        size = (256, 256),
        visibility = (),
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
            curvalue = 900,
        ),
        precision = 0.01,
        fmtstr = "%.2f",
    ),
)
