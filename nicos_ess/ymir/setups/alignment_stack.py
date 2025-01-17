description = 'The motors for alignment in the YMIR cave'

devices = dict(
    mX=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Single axis positioner',
        motorpv='YMIR-SpScn:MC-X-01:Mtr',
        powerautopv='YMIR-SpScn:MC-X-01:Mtr-PwrAuto',
        errormsgpv='YMIR-SpScn:MC-X-01:Mtr-MsgTxt',
        errorbitpv='YMIR-SpScn:MC-X-01:Mtr-Err',
        reseterrorpv='YMIR-SpScn:MC-X-01:Mtr-ErrRst',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    mY=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Single axis positioner',
        motorpv='YMIR-SpScn:MC-Y-01:Mtr',
        powerautopv='YMIR-SpScn:MC-Y-01:Mtr-PwrAuto',
        errormsgpv='YMIR-SpScn:MC-Y-01:Mtr-MsgTxt',
        errorbitpv='YMIR-SpScn:MC-Y-01:Mtr-Err',
        reseterrorpv='YMIR-SpScn:MC-Y-01:Mtr-ErrRst',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    mZ=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Single axis positioner',
        motorpv='YMIR-SpScn:MC-Z-01:Mtr',
        powerautopv='YMIR-SpScn:MC-Z-01:Mtr-PwrAuto',
        errormsgpv='YMIR-SpScn:MC-Z-01:Mtr-MsgTxt',
        errorbitpv='YMIR-SpScn:MC-Z-01:Mtr-Err',
        reseterrorpv='YMIR-SpScn:MC-Z-01:Mtr-ErrRst',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
)
