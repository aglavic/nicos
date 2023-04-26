description = 'Motors for the metrology cart'

pvprefix = 'PSI-ESTIARND:MC-MCU-01:'

devices = dict(
    mpos=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Cart positioning',
        motorpv=f'{pvprefix}Mtr12',
        errormsgpv=f'{pvprefix}Mtr12-MsgTxt',
        errorbitpv=f'{pvprefix}Mtr12-Err',
        reseterrorpv=f'{pvprefix}Mtr12-ErrRst',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    mapproach=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Rotator for approach',
        motorpv=f'{pvprefix}Mtr13',
        errormsgpv=f'{pvprefix}Mtr13-MsgTxt',
        errorbitpv=f'{pvprefix}Mtr13-Err',
        reseterrorpv=f'{pvprefix}Mtr13-ErrRst',
        unit='deg',
        fmtstr='%.1f',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
    mcart=device(
        'nicos.devices.generic.sequence.LockedDevice',
        description='Metrology Cart device',
        device='mpos',
        lock='mapproach',
        unlockvalue=60.,
        lockvalue=180.,
    ),
)
