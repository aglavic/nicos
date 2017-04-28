# -*- coding: utf-8 -*-

description = 'WMI microwave generator'

group = 'optional'

includes = []

tango_base = 'tango://%s:10000/box/' % setupname

devices = dict(
    fg1_modulation_io = device('devices.tango.DigitalOutput',
        description = 'Tango device for the modulation switch',
        tangodevice = tango_base + 'rfgen1/modulation',
        lowlevel = True,
    ),
    fg1_swmodulation = device('devices.generic.Switcher',
        description = 'Modulation switch',
        moveable = 'fg1_modulation_io',
        mapping = {'on': 1,
                   'off': 0},
        fallback = '<undefined>',
        precision = 0,
    ),
    fg1_output_io = device('devices.tango.DigitalOutput',
        description = 'Tango device for the output switch',
        tangodevice = tango_base + 'rfgen1/output',
        lowlevel = True,
    ),
    fg1_swoutput = device('devices.generic.Switcher',
        description = 'Output switch',
        moveable = 'fg1_output_io',
        mapping = {'on': 1,
                   'off': 0},
        fallback = '<undefined>',
        precision = 0,
    ),
    fg2_modulation_io = device('devices.tango.DigitalOutput',
        description = 'Tango device for the modulation switch',
        tangodevice = tango_base + 'rfgen2/modulation',
        lowlevel = True,
    ),
    fg2_swmodulation = device('devices.generic.Switcher',
        description = 'Modulation switch',
        moveable = 'fg2_modulation_io',
        mapping = {'on': 1,
                   'off': 0},
        fallback = '<undefined>',
        precision = 0,
    ),
    fg2_output_io = device('devices.tango.DigitalOutput',
        description = 'Tango device for the output switch',
        tangodevice = tango_base + 'rfgen2/output',
        lowlevel = True,
    ),
    fg2_swoutput = device('devices.generic.Switcher',
        description = 'Output switch',
        moveable = 'fg2_output_io',
        mapping = {'on': 1,
                   'off': 0},
        fallback = '<undefined>',
        precision = 0,
    ),

    fg1_frequency = device('sans1.wmirfgen.Frequency',
        description = 'Device the frequency and frequency modulation',
        tangodevice = tango_base + 'rfgen1/frequency',
        abslimits = (0.1, 40000)
    ),
    fg1_frequency_rf1 = device('devices.tango.AnalogOutput',
        description = 'Tango device for the first '
        'internal frequency generator '
        '(for modulation)',
        tangodevice = tango_base + 'rfgen1/mod_rf1',
        abslimits = (0.0, 40000)
    ),
    fg1_power = device('devices.tango.AnalogOutput',
        description = 'Tango device for the power level',
        tangodevice = tango_base + 'rfgen1/power',
        abslimits = (-130, 30)
    ),
    fg2_frequency = device('sans1.wmirfgen.Frequency',
        description = 'Device the frequency and frequency modulation',
        tangodevice = tango_base + 'rfgen2/frequency',
        abslimits = (0.1, 40000)
    ),
    fg2_frequency_rf1 = device('devices.tango.AnalogOutput',
        description = 'Tango device for the first '
        'internal frequency generator '
        '(for modulation)',
        tangodevice = tango_base + 'rfgen2/mod_rf1',
        abslimits = (0.0, 40000)
    ),
    fg2_power = device('devices.tango.AnalogOutput',
        description = 'Tango device for the power level',
        tangodevice = tango_base + 'rfgen2/power',
        abslimits = (-130, 30)
    ),
    lockin_x = device('devices.tango.AnalogInput',
        description = 'Lockin x',
        tangodevice = tango_base + 'lockin/x',
        lowlevel = False,
        fmtstr = '%g',
    ),
    lockin_y = device('devices.tango.AnalogInput',
        description = 'Lockin y',
        tangodevice = tango_base + 'lockin/y',
        lowlevel = False,
        fmtstr = '%g',
    ),
    #lockin_vi = device('devices.tango.ReadableChannel',
    #    description = 'Measurable tango device for x/y, measured by the lockin',
    #    tangodevice = tango_base + 'lockin/xy',
    #    valuenames = ['x', 'y'],
    #    lowlevel = True,
    #),
    #lockin = device('devices.generic.Detector',
    #    description = 'Lockin x/y',
    #    others = ['lockin_vi'],
    #    maxage = 8,
    #    pollinterval = 3,
    #),
)
