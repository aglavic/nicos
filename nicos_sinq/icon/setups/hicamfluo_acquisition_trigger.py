description = 'Keysight 33510A Function Generator'
group = 'optional'

includes = []

excludes = [
    'trigger',
]

tango_base = 'tango://172.28.77.84:10000/antares/funcgen_burst/'

devices = dict(
    ch1_burst = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Keysight Function Generator Channel 1 Burst Mode',
        tangodevice = tango_base + 'ch1_burst',
    ),
    ch2_burst = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Keysight Function Generator Channel 2 Burst Mode',
        tangodevice = tango_base + 'ch2_burst',
    ),
    trigger_hw = device('nicos.devices.entangle.DigitalOutput',
        description = 'I/O for triggering the camera',
        tangodevice = 'tango://172.28.77.78:10000/box/piface/out_1',
    ),
    trigger = device('nicos.devices.generic.Pulse',
        description = 'Camera trigger',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        moveable = 'trigger_hw',
        visibility = (),
    ),
)
