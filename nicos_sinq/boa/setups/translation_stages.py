description = 'BOA Translations stages'

pvprefix = 'SQ:BOA:mcu2:'

devices = dict(
    translation_300mm_a = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Translation 1',
        motorpv = pvprefix + 'TVA',
        errormsgpv = pvprefix + 'TVA-MsgTxt',
    ),
    translation_300mm_b = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Translation 2',
        motorpv = pvprefix + 'TVB',
        errormsgpv = pvprefix + 'TVB-MsgTxt',
    ),
)
