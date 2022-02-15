description = 'BOA Slit 1'

pvprefix = 'SQ:BOA:sl1:'

devices = dict(
    sal = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Slit 1 left motor',
        motorpv = pvprefix + 'SAL',
        errormsgpv = pvprefix + 'SAL-MsgTxt',
    ),
    sar = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Slit 1 right motor',
        motorpv = pvprefix + 'SAR',
        errormsgpv = pvprefix + 'SAR-MsgTxt',
    ),
    sab = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Slit 1 bottom motor',
        motorpv = pvprefix + 'SAB',
        errormsgpv = pvprefix + 'SAB-MsgTxt',
    ),
    sat = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Slit 1 top motor',
        motorpv = pvprefix + 'SAT',
        errormsgpv = pvprefix + 'SAT-MsgTxt',
    ),
    slit1 = device('nicos.devices.generic.slit.Slit',
        description = 'Slit 1 with left, right, bottom and top motors',
        opmode = '4blades',
        left = 'sal',
        right = 'sar',
        top = 'sat',
        bottom = 'sab',
        lowlevel = True
    ),
    slit1_height = device('nicos_sinq.amor.devices.slit.SlitOpening',
        description = 'Slit 1 height controller',
        slit = 'slit1'
    ),
    slit1_width = device('nicos.devices.generic.slit.WidthSlitAxis',
        description = 'Slit 1 width controller',
        slit = 'slit1',
        unit = 'mm',
    ),
)
