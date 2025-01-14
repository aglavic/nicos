description = 'Prototype actuator motors'

pvprefix = 'PSI-ESTIARND:MC-MCU-01:'

devices = dict(
    am1=device(
        'nicos_ess.devices.epics.pva.motor.EpicsMotor',
        description='Eksma Actuator',
        motorpv=pvprefix + 'm3',
        errormsgpv=pvprefix + 'm3-MsgTxt',
        errorbitpv=pvprefix + 'm3-Err',
        reseterrorpv=pvprefix + 'm3-ErrRst',
        pollinterval=None,
        monitor=True,
        pva=True,
    ),
)
