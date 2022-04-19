# -*- coding: utf-8 -*-

description = 'WMI microwave generator'

group = 'optional'

devices = dict(
#    fg1_modulation_io = device('nicos.devices.entangle.DigitalOutput',
#        description = 'Tango device for the modulation switch',
#        visibility = (),
#    ),
#    fg1_swmodulation = device('nicos.devices.generic.Switcher',
#        description = 'Modulation switch',
#        moveable = 'fg1_modulation_io',
#        mapping = {'on': 1,
#                   'off': 0},
#        fallback = '<undefined>',
#        precision = 0,
#    ),
#    fg1_output_io = device('nicos.devices.entangle.DigitalOutput',
#        description = 'Tango device for the output switch',
#        visibility = (),
#    ),
#    fg1_swoutput = device('nicos.devices.generic.Switcher',
#        description = 'Output switch',
#        moveable = 'fg1_output_io',
#        mapping = {'on': 1,
#                   'off': 0},
#        fallback = '<undefined>',
#        precision = 0,
#    ),
#    fg2_modulation_io = device('nicos.devices.entangle.DigitalOutput',
#        description = 'Tango device for the modulation switch',
#        visibility = (),
#    ),
#    fg2_swmodulation = device('nicos.devices.generic.Switcher',
#        description = 'Modulation switch',
#        moveable = 'fg2_modulation_io',
#        mapping = {'on': 1,
#                   'off': 0},
#        fallback = '<undefined>',
#        precision = 0,
#    ),
#    fg2_output_io = device('nicos.devices.entangle.DigitalOutput',
#        description = 'Tango device for the output switch',
#        visibility = (),
#    ),
#    fg2_swoutput = device('nicos.devices.generic.Switcher',
#        description = 'Output switch',
#        moveable = 'fg2_output_io',
#        mapping = {'on': 1,
#                   'off': 0},
#        fallback = '<undefined>',
#        precision = 0,
#    ),
#    fg1_frequency = device('nicos_mlz.devices.wmirfgen.Frequency',
#        description = 'Device the frequency and frequency modulation',
#        abslimits = (0.1, 40000)
#    ),
#    fg1_frequency_rf1 = device('nicos.devices.entangle.AnalogOutput',
#        description = 'Tango device for the first '
#        'internal frequency generator '
#        '(for modulation)',
#        abslimits = (0.0, 40000)
#    ),
#    fg1_power = device('nicos.devices.entangle.AnalogOutput',
#        description = 'Tango device for the power level',
#        abslimits = (-130, 30)
#    ),
#    fg2_frequency = device('nicos_mlz.devices.wmirfgen.Frequency',
#        description = 'Device the frequency and frequency modulation',
#        abslimits = (0.1, 40000)
#    ),
#    fg2_frequency_rf1 = device('nicos.devices.entangle.AnalogOutput',
#        description = 'Tango device for the first '
#        'internal frequency generator '
#        '(for modulation)',
#        abslimits = (0.0, 40000)
#    ),
#    fg2_power = device('nicos.devices.entangle.AnalogOutput',
#        description = 'Tango device for the power level',
#        abslimits = (-130, 30)
#    ),
#    lockin_x = device('nicos.devices.entangle.AnalogInput',
#        description = 'Lockin x',
#        fmtstr = '%g',
#    ),
#    lockin_y = device('nicos.devices.entangle.AnalogInput',
#        description = 'Lockin y',
#        fmtstr = '%g',
#    ),
    #lockin_vi = device('nicos.devices.entangle.ReadableChannel',
    #    description = 'Measurable tango device for x/y, measured by the lockin',
    #    valuenames = ['x', 'y'],
    #    visibility = (),
    #),
    #lockin = device('nicos.devices.generic.Detector',
    #    description = 'Lockin x/y',
    #    others = ['lockin_vi'],
    #    maxage = 8,
    #    pollinterval = 3,
    #),
)
