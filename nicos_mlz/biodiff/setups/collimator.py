# -*- coding: utf-8 -*-

description = 'Collimation hexapod setup'
group = 'lowlevel'

tango_base = 'tango://phys.biodiff.frm2:10000/biodiff/hexapod/'

devices = dict(
    collimator_x = device('nicos.devices.entangle.Motor',
        description = 'collimator hexapod X axis',
        tangodevice = tango_base + 'x',
        unit = 'mm',
        precision = 0.01,
    ),
    collimator_y = device('nicos.devices.entangle.Motor',
        description = 'collimator hexapod Y axis',
        tangodevice = tango_base + 'y',
        unit = 'mm',
        precision = 0.01,
    ),
    collimator_z = device('nicos.devices.entangle.Motor',
        description = 'collimator hexapod Z axis',
        tangodevice = tango_base + 'z',
        unit = 'mm',
        precision = 0.01,
    ),
    collimator_arc_x = device('nicos.devices.entangle.Motor',
        description = 'collimator hexapod rotation around X axis',
        tangodevice = tango_base + 'u',
        unit = 'deg',
        precision = 0.01,
    ),
    collimator_arc_y = device('nicos.devices.entangle.Motor',
        description = 'collimator hexapod rotation around Y axis',
        tangodevice = tango_base + 'v',
        unit = 'deg',
        precision = 0.01,
    ),
    collimator_arc_z = device('nicos.devices.entangle.Motor',
        description = 'collimator hexapod rotation around Z axis',
        tangodevice = tango_base + 'w',
        unit = 'deg',
        precision = 0.01,
    ),
)
