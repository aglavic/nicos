description = 'BOA Slit 2'

pvprefix = 'SQ:BOA:sl2:'

devices = dict(
    sbl = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 2 left motor',
        motorpv = pvprefix + 'SBL',
        errormsgpv = pvprefix + 'SBL-MsgTxt',
    ),
    sbr = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 2 right motor',
        motorpv = pvprefix + 'SBR',
        errormsgpv = pvprefix + 'SBR-MsgTxt',
    ),
    sbb = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 2 bottom motor',
        motorpv = pvprefix + 'SBB',
        errormsgpv = pvprefix + 'SBB-MsgTxt',
    ),
    sbt = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 2 top motor',
        motorpv = pvprefix + 'SBT',
        errormsgpv = pvprefix + 'SBT-MsgTxt',
    ),
    slit2 = device('nicos.devices.generic.slit.Slit',
        description = 'Slit 1 with left, right, bottom and top motors',
        opmode = '4blades',
        left = 'sbl',
        right = 'sbr',
        top = 'sbt',
        bottom = 'sbb',
        visibility = (),
    ),
    slit2_height = device('nicos_sinq.amor.devices.slit.SlitOpening',
        description = 'Slit 2 height controller',
        slit = 'slit2'
    ),
    slit2_width = device('nicos.devices.generic.slit.WidthSlitAxis',
        description = 'Slit 2 width controller',
        slit = 'slit2',
        unit = 'mm',
    ),
)
