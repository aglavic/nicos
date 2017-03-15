# -*- coding: utf-8 -*-

description = "Virtual shutter setup"
group = "lowlevel"

devices = dict(
    shutter         = device("devices.generic.ManualSwitch",
                             description = "shutter control",
                             states = ["open", "closed"],
                            ),
    nl3a_shutter    = device("devices.generic.ManualSwitch",
                             description = "Neutron guide 3a shutter status",
                             states = ["open", "closed"],
                            ),
    sixfold_shutter = device("devices.generic.ManualSwitch",
                             description = "Sixfold shutter status",
                             states = ["open", "closed"],
                            ),
)
