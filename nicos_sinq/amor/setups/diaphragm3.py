description = 'Slit 3 devices in the SINQ AMOR.'

pvprefix = 'SQ:AMOR:motc:'

includes = ['logical_motors']

devices = dict(
    d3t = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 3 top blade',
        motorpv = pvprefix + 'd3t',
        # errormsgpv = pvprefix + 'd3t-MsgTxt',
        visibility = (),
    ),
    d3b = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 3 bottom blade',
        motorpv = pvprefix + 'd3b',
        # errormsgpv = pvprefix + 'd3b-MsgTxt',
        visibility = (),
    ),
    d3l = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 3 left blade',
        motorpv = pvprefix + 'd3l',
        # errormsgpv = pvprefix + 'd3l-MsgTxt',
        visibility = (),
    ),
    d3r = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 3 right blade',
        motorpv = pvprefix + 'd3r',
        # errormsgpv = pvprefix + 'd3r-MsgTxt',
        visibility = (),
    ),
    d3z = device('nicos.devices.epics.pyepics.motor.EpicsMotor',
        description = 'Slit 3 vertical translation',
        motorpv = pvprefix + 'd3z',
        # errormsgpv = pvprefix + 'd3z-MsgTxt',
        visibility = (),
    ),
    slit3 = device('nicos.devices.generic.slit.Slit',
        description = 'Slit 3 with left, right, bottom and top motors',
        opmode = '4blades',
        left = 'd3l',
        right = 'd3r',
        top = 'd3t',
        bottom = 'd3b',
        visibility = ()
    ),
    d3v = device('nicos_sinq.amor.devices.slit.AmorSlitLogicalMotor',
        description = 'Vertical slit opening',
        motortype = 'd3v',
        controller = 'controller_slm',
        unit = 'mm'
    ),
    d3h = device('nicos_sinq.amor.devices.slit.AmorSlitLogicalMotor',
        description = 'Horizontal slit opening ',
        motortype = 'd3h',
        controller = 'controller_slm',
        unit = 'mm'
    ),
    d3d = device('nicos_sinq.amor.devices.slit.AmorSlitLogicalMotor',
        description = 'Vertical slit displacement',
        motortype = 'd3d',
        controller = 'controller_slm',
        unit = 'mm'
    ),
)
