description = 'Gas pump for the DMC detector.'

group = 'lowlevel'

prefix = 'SQ:DMC:gaspump'

devices = dict(
    ch1_active = device('nicos.devices.epics.EpicsStringReadable',
        description = 'Amplitude of channel 1',
        readpv = f'{prefix}:Ch1:Status_RBV',
        visibility = ('namespace',),
    ),
    ch1_amplitude = device('nicos.devices.epics.EpicsDigitalMoveable',
        description = 'Amplitude of channel 1',
        readpv = f'{prefix}:Ch1:Amplitude_RBV',
        writepv = f'{prefix}:Ch1:Amplitude',
        unit = 'mV',
        fmtstr = '%d',
        requires = {'level': 'admin'},
        visibility = ('namespace',),
    ),
    ch1_frequency = device('nicos.devices.epics.EpicsDigitalMoveable',
        description = 'Frequency of channel 1',
        readpv = f'{prefix}:Ch1:Frequency_RBV',
        writepv = f'{prefix}:Ch1:Frequency',
        unit = 'Hz',
        fmtstr = '%d',
        requires = {'level': 'admin'},
        visibility = ('namespace',),
    ),
    ch1_phase = device('nicos.devices.epics.EpicsDigitalMoveable',
        description = 'Phase of channel 1',
        readpv = f'{prefix}:Ch1:Phase_RBV',
        writepv = f'{prefix}:Ch1:Phase',
        unit = 'degree',
        fmtstr = '%d',
        requires = {'level': 'admin'},
        visibility = ('namespace',),
    ),
    ch1_error = device('nicos.devices.epics.EpicsStringReadable',
        description = 'Error on channel 1',
        readpv = f'{prefix}:Ch1:Error',
    ),
    ch1_mode = device('nicos.devices.epics.EpicsStringReadable',
        description = 'Mode of channel 1',
        readpv = f'{prefix}:Ch1:Mode_RBV',
        visibility = ('namespace',),
    ),
    ch1_feedback = device('nicos.devices.epics.EpicsStringReadable',
        description = 'Feedback from hardware on channel 1',
        readpv = f'{prefix}:Ch1:Feedback_RBV',
        visibility = ('namespace',),
    ),
    ch2_active=device('nicos.devices.epics.EpicsStringReadable',
                      description='Amplitude of channel 2',
                      readpv=f'{prefix}:Ch2:Status_RBV',
        visibility = ('namespace',),
                      ),
    ch2_amplitude = device('nicos.devices.epics.EpicsDigitalMoveable',
        description = 'Amplitude of channel 2',
        readpv = f'{prefix}:Ch2:Amplitude_RBV',
        writepv = f'{prefix}:Ch2:Amplitude',
        unit = 'mV',
        fmtstr = '%d',
        requires = {'level': 'admin'},
        visibility = ('namespace',),
    ),
    ch2_frequency = device('nicos.devices.epics.EpicsDigitalMoveable',
        description = 'Frequency of channel 2',
        readpv = f'{prefix}:Ch2:Frequency_RBV',
        writepv = f'{prefix}:Ch2:Frequency',
        unit = 'Hz',
        fmtstr = '%d',
        requires = {'level': 'admin'},
        visibility = ('namespace',),
    ),
    ch2_phase = device('nicos.devices.epics.EpicsDigitalMoveable',
        description = 'Phase of channel 2',
        readpv = f'{prefix}:Ch2:Phase_RBV',
        writepv = f'{prefix}:Ch2:Phase',
        unit = 'degree',
        fmtstr = '%d',
        requires = {'level': 'admin'},
        visibility = ('namespace',),
    ),
    ch2_error = device('nicos.devices.epics.EpicsStringReadable',
        description = 'Error on channel 2',
        readpv = f'{prefix}:Ch2:Error',
    ),
    ch2_mode = device('nicos.devices.epics.EpicsStringReadable',
        description = 'Mode of channel 2',
        readpv = f'{prefix}:Ch2:Mode_RBV',
        visibility = ('namespace',),
    ),
    ch2_feedblack = device('nicos.devices.epics.EpicsStringReadable',
        description = 'Feedback from hardware on channel 2',
        readpv = f'{prefix}:Ch2:Feedback_RBV',
        visibility = ('namespace',),
    ),
    gaspump_command = device('nicos.devices.epics.EpicsStringMoveable',
        description = 'Direct access to command interface',
        readpv = f'{prefix}:Command',
        writepv = f'{prefix}:Command',
        requires = {'level': 'admin'},
        visibility = ('namespace',),
    )
)
