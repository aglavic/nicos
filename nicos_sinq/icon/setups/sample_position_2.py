description = 'Sample position 2 devices in the SINQ ICON.'

group = 'lowlevel'

includes = [
    'neutron_aperture', 'shutters', 'beam_limiter_1', 'beam_limiter_2',
    'sensors'
]

display_order = 40

devices = dict(
    sp2_tx = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Sample Position 2, Translation X',
        motorpv = 'SQ:ICON:board3:SP2TX',
        errormsgpv = 'SQ:ICON:board3:SP2TX-MsgTxt',
        precision = 0.01,
    ),
    sp2_ty_axis = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Sample Position 2, Translation Y axis',
        motorpv = 'SQ:ICON:board5:SP2TY',
        errormsgpv = 'SQ:ICON:board5:SP2TY-MsgTxt',
        precision = 0.01,
        lowlevel = True,
    ),
    sp2_ty_brake = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = 3.0,
        description = 'Sample Position 2, Translation Y brake',
        readpv = 'SQ:ICON:b4io4:BrakeSP2TY',
        writepv = 'SQ:ICON:b4io4:BrakeSP2TY',
        lowlevel = True,
    ),
    sp2_ty = device('nicos.devices.generic.sequence.LockedDevice',
        description = 'Sample Position 2, Translation Y',
        device = 'sp2_ty_axis',
        lock = 'sp2_ty_brake',
        unlockvalue = 1,
        lockvalue = 0,
        unit = 'mm',
    ),
    sp2_tz = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Sample Position 2, Translation Z',
        motorpv = 'SQ:ICON:board3:SP2TZ',
        errormsgpv = 'SQ:ICON:board3:SP2TZ-MsgTxt',
        precision = 0.01,
    ),
    sp2_rx = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Sample Position 2, Rotation X',
        motorpv = 'SQ:ICON:board3:SP2RX',
        errormsgpv = 'SQ:ICON:board3:SP2RX-MsgTxt',
        precision = 0.01,
    ),
    sp2_ry = device('nicos_ess.devices.epics.motor.EpicsMotor',
        epicstimeout = 3.0,
        description = 'Sample Position 2, Rotation Y',
        motorpv = 'SQ:ICON:board5:SP2RY',
        errormsgpv = 'SQ:ICON:board5:SP2RY-MsgTxt',
        precision = 0.01,
    ),
    sp2_ry_brake_digital = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = 3.0,
        description = 'Sample Position 2, Rotation Y brake digital IO',
        readpv = 'SQ:ICON:b2io2:BrakeSP2RYRBV',
        writepv = 'SQ:ICON:b2io4:BrakeSP2RY',
        lowlevel = True,
    ),
    sp2_ry_brake = device('nicos.devices.generic.Switcher',
        description = 'Sample Position 2, Rotation Y brake',
        moveable = 'sp2_ry_brake_digital',
        mapping = {
            'open': 1,
            'closed': 0,
        },
        precision = 0.1,
    ),
    sp2_rz = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Sample Position 2, Rotation Z',
        motorpv = 'SQ:ICON:board3:SP2RZ',
        errormsgpv = 'SQ:ICON:board3:SP2RZ-MsgTxt',
        precision = 0.01,
    ),
)
