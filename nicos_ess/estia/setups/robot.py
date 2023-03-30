description = 'Motors for the robot adjuster'

pvprefix = 'PSI-ESTIARND:MC-MCU-01:'

devices = dict(
    robot_pos=device(
        'nicos_ess.devices.epics.motor.EpicsMotor',
        description='M6 Robot1 Position',
        motorpv=f'{pvprefix}m6',
        errormsgpv=f'{pvprefix}m6-MsgTxt',
        errorbitpv=f'{pvprefix}m6-Err',
        reseterrorpv=f'{pvprefix}m6-ErrRst',
    ),
    robot_vert=device(
        'nicos_ess.devices.epics.motor.EpicsMotor',
        description='M7 Robot1 Vertical',
        motorpv=f'{pvprefix}m7',
        errormsgpv=f'{pvprefix}m7-MsgTxt',
        errorbitpv=f'{pvprefix}m7-Err',
        reseterrorpv=f'{pvprefix}m7-ErrRst',
    ),
    robot_y=device(
        'nicos_ess.devices.epics.motor.EpicsMotor',
        description='M14 Selene1 Mover Y',
        motorpv=f'{pvprefix}m14',
        errormsgpv=f'{pvprefix}m14-MsgTxt',
        errorbitpv=f'{pvprefix}m14-Err',
        reseterrorpv=f'{pvprefix}m14-ErrRst',
        unit='mm',
    ),
    robot_z=device(
        'nicos_ess.devices.epics.motor.EpicsMotor',
        description='M15 Selene1 Mover Z',
        motorpv=f'{pvprefix}m15',
        errormsgpv=f'{pvprefix}m15-MsgTxt',
        errorbitpv=f'{pvprefix}m15-Err',
        reseterrorpv=f'{pvprefix}m15-ErrRst',
        unit='mm',
    ),
    robot_rx=device(
        'nicos_ess.devices.epics.motor.EpicsMotor',
        description='M16 Selene1 Mover Rx',
        motorpv=f'{pvprefix}m16',
        errormsgpv=f'{pvprefix}m16-MsgTxt',
        errorbitpv=f'{pvprefix}m16-Err',
        reseterrorpv=f'{pvprefix}m16-ErrRst',
        unit='deg',
    ),
    robot_ry=device(
        'nicos_ess.devices.epics.motor.EpicsMotor',
        description='M17 Selene1 Mover Ry',
        motorpv=f'{pvprefix}m17',
        errormsgpv=f'{pvprefix}m17-MsgTxt',
        errorbitpv=f'{pvprefix}m17-Err',
        reseterrorpv=f'{pvprefix}m17-ErrRst',
        unit='deg',
    ),
    robot_rz=device(
        'nicos_ess.devices.epics.motor.EpicsMotor',
        description='M18 Selene1 Mover Rz',
        motorpv=f'{pvprefix}m18',
        errormsgpv=f'{pvprefix}m18-MsgTxt',
        errorbitpv=f'{pvprefix}m18-Err',
        reseterrorpv=f'{pvprefix}m18-ErrRst',
        unit='deg',
    ),
    clutch1=device(
        'nicos.devices.epics.EpicsStringReadable',
        description='Clutch 1',
        readpv=f'{pvprefix}m6-OpenClutch',
    ),
    clutch2=device(
        'nicos.devices.epics.EpicsStringReadable',
        description='Clutch 2',
        readpv=f'{pvprefix}m12-OpenClutch',
    ),
)
