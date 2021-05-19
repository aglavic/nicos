# -*- coding: utf-8 -*-

description = 'Shutter setup'
group = 'lowlevel'
display_order = 5

tango_base = 'tango://phys.kws3.frm2:10000/kws3/'
tango_base_mlz = 'tango://ictrlfs.ictrl.frm2:10000/mlz/'

devices = dict(
    # currently not enabled:
    # shutter = device('nicos_mlz.jcns.devices.shutter.Shutter',
    #     description = 'Experiment shutter',
    #     tangodevice = tango_base + 'FZJDP_digital/ExpShutter',
    #     mapping = {'closed': 2,
    #                'open': 1},
    # ),
    nl3a_shutter = device('nicos.devices.tango.NamedDigitalInput',
        description = 'NL3a shutter status',
        tangodevice = tango_base_mlz + 'shutter/nl3a',
        mapping = {'closed': 0,
                   'open': 1},
        pollinterval = 60,
        maxage = 120,
    ),
    sixfold_shutter = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Sixfold shutter status',
        tangodevice = tango_base_mlz + 'shutter/sixfold',
        mapping = {'closed': 0,
                   'open': 1},
        pollinterval = 60,
        maxage = 120,
    ),
)

extended = dict(
    representative = 'nl3a_shutter',
)
