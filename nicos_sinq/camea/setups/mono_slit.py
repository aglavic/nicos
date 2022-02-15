description = 'Monochromator slit devices'

pvmcu = 'SQ:CAMEA:mcu2:'

devices = dict(
    mst = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator slit top',
        motorpv = pvmcu + 'mst',
        errormsgpv = pvmcu + 'mst-MsgTxt',
        precision = 0.02,
    ),
    msb = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator slit bottom',
        motorpv = pvmcu + 'msb',
        errormsgpv = pvmcu + 'msb-MsgTxt',
        precision = 0.02,
    ),
    msr = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator slit right',
        motorpv = pvmcu + 'msr',
        errormsgpv = pvmcu + 'msr-MsgTxt',
        precision = 0.02,
    ),
    msl = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator slit left',
        motorpv = pvmcu + 'msl',
        errormsgpv = pvmcu + 'msl-MsgTxt',
        precision = 0.02,
    ),
    mslit = device('nicos.devices.generic.slit.Slit',
        description = 'Monochromator slit with left, right, bottom and '
        'top motors',
        opmode = '4blades',
        left = 'msl',
        right = 'msr',
        top = 'mst',
        bottom = 'msb',
        lowlevel = True
    ),
    mslit_height = device('nicos_sinq.amor.devices.slit.SlitOpening',
        description = 'Detector Slit opening controller',
        slit = 'mslit'
    ),
    mslit_width = device('nicos.devices.generic.slit.WidthSlitAxis',
        description = 'Detector Slit width controller',
        slit = 'mslit',
        unit = 'mm',
    ),
)
