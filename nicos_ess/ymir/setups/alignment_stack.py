description = 'The motors for alignment in the YMIR cave'

devices = dict(
    mX=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Single axis positioner',
        motorpv='YMIR-SpScn:MC-X-01:m',
        errormsgpv='YMIR-SpScn:MC-X-01:m-MsgTxt',
        errorbitpv='YMIR-SpScn:MC-X-01:m-Err',
        reseterrorpv='YMIR-SpScn:MC-X-01:m-ErrRst',
        monitor=True,
    ),
    mY=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Single axis positioner',
        motorpv='YMIR-SpScn:MC-Y-01:m',
        errormsgpv='YMIR-SpScn:MC-Y-01:m-MsgTxt',
        errorbitpv='YMIR-SpScn:MC-Y-01:m-Err',
        reseterrorpv='YMIR-SpScn:MC-Y-01:m-ErrRst',
        monitor=True,
    ),
    mZ=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Single axis positioner',
        motorpv='YMIR-SpScn:MC-Z-01:m',
        errormsgpv='YMIR-SpScn:MC-Z-01:m-MsgTxt',
        errorbitpv='YMIR-SpScn:MC-Z-01:m-Err',
        reseterrorpv='YMIR-SpScn:MC-Z-01:m-ErrRst',
        monitor=True,
    ),
)
