description = 'Motors for the robot adjuster for Selene 2'

pvprefix = 'ESTIA-Sel2:MC-MCU-01:'

group = 'lowlevel'

devices = dict(
    robot2_pos=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Mtr6 Robot1 Position',
        motorpv=f'{pvprefix}Mtr6',
        powerautopv=f'{pvprefix}Mtr6-PwrAuto',
        errormsgpv=f'{pvprefix}Mtr6-MsgTxt',
        errorbitpv=f'{pvprefix}Mtr6-Err',
        reseterrorpv=f'{pvprefix}Mtr6-ErrRst',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    robot2_vert=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Mtr7 Robot1 Vertical',
        motorpv=f'{pvprefix}Mtr7',
        powerautopv=f'{pvprefix}Mtr7-PwrAuto',
        errormsgpv=f'{pvprefix}Mtr7-MsgTxt',
        errorbitpv=f'{pvprefix}Mtr7-Err',
        reseterrorpv=f'{pvprefix}Mtr7-ErrRst',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    clutch2_1=device(
        'nicos.devices.epics.pva.EpicsStringReadable',
        description='Clutch 1',
        readpv=f'{pvprefix}Mtr6-OpenClutch',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    clutch2_2=device(
        'nicos.devices.epics.pva.EpicsStringReadable',
        description='Clutch 2',
        readpv=f'{pvprefix}Mtr12-OpenClutch',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    driver2_1_approach=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Mtr8 Driver1-1 Approach',
        motorpv=f'{pvprefix}Mtr8',
        powerautopv=f'{pvprefix}Mtr8-PwrAuto',
        errormsgpv=f'{pvprefix}Mtr8-MsgTxt',
        errorbitpv=f'{pvprefix}Mtr8-Err',
        reseterrorpv=f'{pvprefix}Mtr8-ErrRst',
        unit='mm',
        userlimits=(-28, 0),
        maxage=None,
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    driver2_2_approach=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Mtr9 Driver1-2 Approach',
        motorpv=f'{pvprefix}Mtr9',
        powerautopv=f'{pvprefix}Mtr9-PwrAuto',
        errormsgpv=f'{pvprefix}Mtr9-MsgTxt',
        errorbitpv=f'{pvprefix}Mtr9-Err',
        reseterrorpv=f'{pvprefix}Mtr9-ErrRst',
        unit='mm',
        userlimits=(-28, 0),
        maxage=None,
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    driver2_1_adjust=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Mtr10 Driver1-1 Adjust',
        motorpv=f'{pvprefix}Mtr10',
        powerautopv=f'{pvprefix}Mtr10-PwrAuto',
        errormsgpv=f'{pvprefix}Mtr10-MsgTxt',
        errorbitpv=f'{pvprefix}Mtr10-Err',
        reseterrorpv=f'{pvprefix}Mtr10-ErrRst',
        unit='degree',
        abslimits=(0, 0),
        userlimits=(-100000, 100000),
        maxage=None,
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    driver2_2_adjust=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Mtr11 Driver1-2 Adjust',
        motorpv=f'{pvprefix}Mtr11',
        powerautopv=f'{pvprefix}Mtr11-PwrAuto',
        errormsgpv=f'{pvprefix}Mtr11-MsgTxt',
        errorbitpv=f'{pvprefix}Mtr11-Err',
        reseterrorpv=f'{pvprefix}Mtr11-ErrRst',
        unit='degree',
        abslimits=(0, 0),
        userlimits=(-100000, 100000),
        maxage=None,
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    driver2_1_hex_state=device(
        'nicos.devices.epics.pva.EpicsMappedReadable',
        description='Hexscrew state',
        readpv=f'{pvprefix}Mtr8-HexScrew',
        maxage=None,
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
    driver2_2_hex_state=device(
        'nicos.devices.epics.pva.EpicsMappedReadable',
        description='Hexscrew state',
        readpv=f'{pvprefix}Mtr9-HexScrew',
        maxage=None,
        monitor=True,
        pollinterval=None,
        pva=True,
    ),
)
