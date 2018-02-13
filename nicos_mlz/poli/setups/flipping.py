description = 'Flipping ratio detector and flipper alias'

group = 'optional'

includes = ['detector']

devices = dict(
    adet = device('nicos_mlz.poli.devices.detector.AsymDetector',
        description = 'detector that automatically counts up and down states',
        detector = 'det',
        flipper = 'flipper',
        flipvalues = ('off', 'on'),
        counter = 'ctr1',
    ),

    flipper = device('nicos.devices.generic.DeviceAlias',
        devclass = 'nicos.core.device.Moveable',
    ),
)
