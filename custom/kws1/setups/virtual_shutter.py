# -*- coding: utf-8 -*-

description = "Virtual beam shutter setup"
group = "lowlevel"
display_order = 5

devices = dict(
    shutter    = device('devices.generic.ManualSwitch',
                        description = 'shutter control',
                        states = ['open', 'closed'],
                       ),
    sixfold_shutter = device('devices.generic.ManualSwitch',
                        description = 'Sixfold shutter status',
                        states = ['open', 'closed'],
                       ),
)
