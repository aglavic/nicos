description = 'External ILL camera'

group = 'optional'

excludes = ['detector_neo']

devices = dict(
    fastshutter_io = device('nicos.devices.generic.manual.ManualSwitch',
        description = 'fake fast shutter',
        states = [1, 2,],
    ),
    fastshutter = device('nicos.devices.generic.Switcher',
        description = 'Fast shutter',
        moveable = 'fastshutter_io',
        mapping = dict(open = 1, closed = 2),
        fallback = '<undefined>',
        precision = 0,
        unit = '',
    ),
    trigger_hw = device('nicos.devices.entangle.DigitalOutput',
        tangodevice = 'tango://192.168.20.65:10000/box/piface/out_0',
        visibility = (),
    ),
    trigger = device('nicos.devices.generic.Pulse',
        description = 'Camera trigger',
        onvalue = 0,
        offvalue = 1,
        ontime = 0.1,
        moveable = 'trigger_hw',
        visibility = (),
    ),
    timer_ill = device('nicos_mlz.antares.devices.TriggerTimer',
        description = 'Software timer',
        trigger = 'trigger',
    ),
    det_ill = device('nicos.devices.generic.Detector',
        description = 'The ILL detector',
        timers = ['timer_ill'],
    ),
)
