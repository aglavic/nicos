description = 'Setup for the source grating for fraing interferometry'

pvprefix = 'SQ:BOA:mcu3:'

devices = dict(
    ngit = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Grating translation',
        motorpv = pvprefix + 'NGIT',
        errormsgpv = pvprefix + 'NGIT-MsgTxt',
    ),
    ngir = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Grating rotation',
        motorpv = pvprefix + 'NGIR',
        errormsgpv = pvprefix + 'NGIR-MsgTxt',
    ),
)
