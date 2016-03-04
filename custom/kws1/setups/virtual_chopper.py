#  -*- coding: utf-8 -*-

description = 'Virtual setup for the choppers'
group = 'lowlevel'

devices = dict(
    chopper1_phase  = device('devices.generic.VirtualMotor',
                             description = 'Phase of the first chopper',
                             unit = 'deg',
                             fmtstr = '%.1f',
                             abslimits = (0, 360),
                             precision = 1.0,
                             lowlevel = True,
                            ),
    chopper1_freq   = device('devices.generic.VirtualMotor',
                             description = 'Frequency of the first chopper',
                             unit = 'Hz',
                             fmtstr = '%.1f',
                             abslimits = (0, 75),
                             precision = 0.1,
                             lowlevel = True,
                            ),
    chopper2_phase  = device('devices.generic.VirtualMotor',
                             description = 'Phase of the second chopper',
                             unit = 'deg',
                             fmtstr = '%.1f',
                             abslimits = (0, 360),
                             precision = 1.0,
                             lowlevel = True,
                            ),
    chopper2_freq   = device('devices.generic.VirtualMotor',
                             description = 'Frequency of the second chopper',
                             unit = 'Hz',
                             fmtstr = '%.1f',
                             abslimits = (0, 75),
                             precision = 0.1,
                             lowlevel = True,
                            ),
    chopper1_motor  = device('devices.generic.VirtualMotor',
                             description = 'Motor switch of the first chopper',
                             lowlevel = True,
                             abslimits = (0, 1),
                             unit = '',
                            ),
    chopper2_motor  = device('devices.generic.VirtualMotor',
                             description = 'Motor switch of the second chopper',
                             lowlevel = True,
                             abslimits = (0, 1),
                             unit = '',
                            ),

    chopper_params  = device('kws1.chopper.Chopper',
                             description = 'Chopper frequency and phase',
                             motor1 = 'chopper1_motor',
                             motor2 = 'chopper2_motor',
                             freq1 = 'chopper1_freq',
                             freq2 = 'chopper2_freq',
                             phase1 = 'chopper1_phase',
                             phase2 = 'chopper2_phase',
                            ),
)
