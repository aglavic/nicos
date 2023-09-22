description = 'Devices for the normal SANS sample holder'

pvprefix = 'SQ:SANS:mcu1:'

excludes = ['emagnet_sample']

devices = dict(
    z = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Sample Table Height',
        motorpv = pvprefix + 'z',
        errormsgpv = pvprefix + 'z-MsgTxt',
        precision = 0.01,
    ),
    xo = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Sample Table X Translation',
        motorpv = pvprefix + 'xo',
        errormsgpv = pvprefix + 'xo-MsgTxt',
        precision = 0.01,
    ),
    yo = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Sample Table Y Translation',
        motorpv = pvprefix + 'yo',
        errormsgpv = pvprefix + 'yo-MsgTxt',
        precision = 0.01,
    ),
    a3 = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Sample table Rotation',
        motorpv = pvprefix + 'a3',
        errormsgpv = pvprefix + 'a3-MsgTxt',
        precision = 0.01,
    ),
    xu = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Sample Upper X Translation',
        motorpv = pvprefix + 'xu',
        errormsgpv = pvprefix + 'xu-MsgTxt',
        precision = 0.01,
    ),
    sg = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample table Rotation',
        motorpv = pvprefix + 'sg',
        errormsgpv = pvprefix + 'sg-MsgTxt',
        precision = 0.01,
    ),
    spos = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Sample Position',
        motorpv = 'SQ:SANS:mota:spos',
        errormsgpv = 'SQ:SANS:mota:spos-MsgTxt',
        precision = 0.01,
    )
)
