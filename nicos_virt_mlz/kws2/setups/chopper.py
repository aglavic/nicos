#  -*- coding: utf-8 -*-

description = 'setup for the choppers'
group = 'lowlevel'
display_order = 65

devices = dict(
    chopper = device('nicos_mlz.kws1.devices.chopper.Chopper',
        description = 'high-level chopper/TOF presets',
        resolutions = [1, 2.5, 5, 10],
        fmtstr = '%.2f Hz, %.0f deg',
        selector = 'selector',
        det_pos = 'detector',
        params = 'chopper_params',
        daq = 'det',
    ),
    chopper_params = device('nicos_mlz.kws1.devices.chopper.ChopperParams',
        description = 'Chopper frequency and opening',
        freq1 = 'chopper1_freq',
        freq2 = 'chopper2_freq',
        phase1 = 'chopper1_phase',
        phase2 = 'chopper2_phase',
        fmtstr = '%.2f Hz, %.0f deg',
    ),
    chopper1_phase = device('nicos.devices.generic.VirtualMotor',
        description = 'Phase of the first chopper',
        lowlevel = True,
        unit = 'deg',
        abslimits = (-360, 360),
    ),
    chopper1_freq = device('nicos.devices.generic.VirtualMotor',
        description = 'Frequency of the first chopper',
        lowlevel = True,
        unit = 'Hz',
        abslimits = (0, 100),
    ),
    chopper2_phase = device('nicos.devices.generic.VirtualMotor',
        description = 'Phase of the second chopper',
        lowlevel = True,
        unit = 'deg',
        abslimits = (-360, 360),
    ),
    chopper2_freq = device('nicos.devices.generic.VirtualMotor',
        description = 'Frequency of the second chopper',
        lowlevel = True,
        unit = 'Hz',
        abslimits = (0, 100),
    ),
)

extended = dict(
    poller_cache_reader = ['detector', 'selector', 'det'],
    representative = 'chopper',
)
