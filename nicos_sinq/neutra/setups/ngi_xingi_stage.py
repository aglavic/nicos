description = 'nGI XinGI setup: Sample stage'

group = 'lowlevel'

pvprefix = 'SQ:NEUTRA:ngiX:'

display_order = 36

devices = dict(
    xs_ry = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        description = 'XinGI Sample Stage, Rotation Y',
        motorpv = pvprefix + 'sgry',
        errormsgpv = pvprefix + 'sgry-MsgTxt',
        precision = 0.01,
    ),
    xs_tx = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        description = 'XinGI Sample Stage, Translation X',
        motorpv = pvprefix + 'sgtx',
        errormsgpv = pvprefix + 'sgtx-MsgTxt',
        precision = 0.01,
        reference_direction = 'reverse',
    ),
    xs_ty = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        description = 'XinGI Sample Stage, Translation Y',
        motorpv = pvprefix + 'sgty',
        errormsgpv = pvprefix + 'sgty-MsgTxt',
        precision = 0.01,
        reference_direction = 'reverse',
    ),
    xs_tz = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        description = 'XinGI Sample Stage, Translation Z',
        motorpv = pvprefix + 'sgtz',
        errormsgpv = pvprefix + 'sgtz-MsgTxt',
        precision = 0.01,
        reference_direction = 'reverse',
    ),
)
