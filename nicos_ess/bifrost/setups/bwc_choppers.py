description = 'The choppers for BIFROST'

pv_root_1 = 'BIFRO-ChpSy2:Chop-BWC-101:'
pv_root_2 = 'BIFRO-ChpSy2:Chop-BWC-102:'
chic_root = 'BIFRO-ChpSy2:Chop-CHIC-001:'

devices = dict(
    bwc1_chopper_status=device(
        'nicos.devices.epics.pva.EpicsMappedReadable',
        description='The chopper status.',
        readpv='{}ChopState_R'.format(pv_root_1),
        visibility=(),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc1_chopper_control=device(
        'nicos.devices.epics.pva.EpicsMappedMoveable',
        description='Used to start and stop the chopper.',
        readpv='{}C_Execute'.format(pv_root_1),
        writepv='{}C_Execute'.format(pv_root_1),
        requires={'level': 'admin'},
        visibility=set(),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc1_chopper_speed=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The current speed.',
        readpv='{}Spd_R'.format(pv_root_1),
        writepv='{}Spd_S'.format(pv_root_1),
        abslimits=(0.0, 0.0),
        precision=0.1,
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc1_chopper_delay=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The current delay.',
        readpv='{}ChopDly-S'.format(pv_root_1),
        writepv='{}ChopDly-S'.format(pv_root_1),
        abslimits=(0.0, 0.0),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc1_chopper_phased=device(
        'nicos.devices.epics.pva.EpicsMappedReadable',
        description='The chopper is in phase.',
        readpv='{}InPhs_R'.format(pv_root_1),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc1_chopper_park_angle=device(
        'nicos.devices.epics.pva.EpicsReadable',
        description='The chopper\'s park angle.',
        readpv='{}Pos_R'.format(pv_root_1),
        visibility=(),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc1_chopper_chic=device(
        'nicos.devices.epics.pva.EpicsMappedReadable',
        description='The status of the CHIC connection.',
        readpv='{}ConnectedR'.format(chic_root),
        visibility=set(),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc1_chopper=device(
        'nicos_ess.devices.epics.chopper.EssChopperController',
        description='The chopper controller',
        state='bwc1_chopper_status',
        command='bwc1_chopper_control',
        speed='bwc1_chopper_speed',
        chic_conn='bwc1_chopper_chic',
    ),
    bwc2_chopper_status=device(
        'nicos.devices.epics.pva.EpicsMappedReadable',
        description='The chopper status.',
        readpv='{}ChopState_R'.format(pv_root_2),
        visibility=(),
        monitor=True,
        pollinterval=None,
        pva=False,
    ),
    bwc2_chopper_control=device(
        'nicos.devices.epics.pva.EpicsMappedMoveable',
        description='Used to start and stop the chopper.',
        readpv='{}C_Execute'.format(pv_root_2),
        writepv='{}C_Execute'.format(pv_root_2),
        requires={'level': 'admin'},
        visibility=set(),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc2_chopper_speed=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The current speed.',
        readpv='{}Spd_R'.format(pv_root_2),
        writepv='{}Spd_S'.format(pv_root_2),
        abslimits=(0.0, 0.0),
        precision=0.1,
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc2_chopper_delay=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The current delay.',
        readpv='{}ChopDly-S'.format(pv_root_2),
        writepv='{}ChopDly-S'.format(pv_root_2),
        abslimits=(0.0, 0.0),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc2_chopper_phased=device(
        'nicos.devices.epics.pva.EpicsMappedReadable',
        description='The chopper is in phase.',
        readpv='{}InPhs_R'.format(pv_root_2),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc2_chopper_park_angle=device(
        'nicos.devices.epics.pva.EpicsReadable',
        description='The chopper\'s park angle.',
        readpv='{}Pos_R'.format(pv_root_2),
        visibility=(),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc2_chopper_chic=device(
        'nicos.devices.epics.pva.EpicsMappedReadable',
        description='The status of the CHIC connection.',
        readpv='{}ConnectedR'.format(chic_root),
        visibility=set(),
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    bwc2_chopper=device(
        'nicos_ess.devices.epics.chopper.EssChopperController',
        description='The chopper controller',
        state='bwc2_chopper_status',
        command='bwc2_chopper_control',
        speed='bwc2_chopper_speed',
        chic_conn='bwc2_chopper_chic',
    ),
)
