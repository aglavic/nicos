description = 'These are the devices for the EIGER monochromator'

mcu1prefix = 'SQ:EIGER:mcu1:'
mcu2prefix = 'SQ:EIGER:mcu2:'

devices = dict(
    a1 = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator omega',
        motorpv = mcu1prefix + 'a1',
        errormsgpv = mcu1prefix + 'a1-MsgTxt',
        precision = 0.02,
    ),
    a2rot = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator two theta',
        motorpv = mcu1prefix + 'a2rot',
        errormsgpv = mcu1prefix + 'a2rot-MsgTxt',
        precision = 0.02,
    ),
    mch = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator horizontal curvature',
        motorpv = mcu1prefix + 'mch',
        errormsgpv = mcu1prefix + 'mch-MsgTxt',
        precision = 0.02,
    ),
    mcv = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator vertical curvature',
        motorpv = mcu1prefix + 'mcv',
        errormsgpv = mcu1prefix + 'mcv-MsgTxt',
        precision = 0.02,
    ),
    mt = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator translation',
        motorpv = mcu1prefix + 'mt',
        errormsgpv = mcu1prefix + 'mt-MsgTxt',
        precision = 0.02,
    ),
    mg = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator goniometer',
        motorpv = mcu1prefix + 'mg',
        errormsgpv = mcu1prefix + 'mg-MsgTxt',
        precision = 0.02,
    ),
    d2l = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator out left slit blade',
        motorpv = mcu2prefix + 'd2l',
        errormsgpv = mcu2prefix + 'd2l-MsgTxt',
        precision = 0.02,
    ),
    d2r = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator out right slit blade',
        motorpv = mcu2prefix + 'd2r',
        errormsgpv = mcu2prefix + 'd2r-MsgTxt',
        precision = 0.02,
    ),
    a2controller = device('nicos_sinq.eiger.devices.eigermono.EigerA2Controller',
        description = 'Controller for aligning A2 and A2 slits',
        reala2 = 'a2rot',
        left = 'd2l',
        right = 'd2r',
        visibility = (),
    ),
    a2 = device('nicos_sinq.devices.logical_motor.LogicalMotor',
        description = 'Logical A2 motor',
        controller = 'a2controller',
        abslimits = (16, 90.14)
    ),
    a2w = device('nicos_sinq.devices.logical_motor.LogicalMotor',
        description = 'Logical out slit width',
        controller = 'a2controller',
        abslimits = (0, 20.)
    ),
    mono = device('nicos_sinq.eiger.devices.eigermono.EigerMonochromator',
        description = 'EIGER monochromator',
        theta = 'a1',
        twotheta = 'a2',
        dvalue = 3.354,
        scatteringsense = 1,
        crystalside = 1,
        unit = 'meV',
        focmode = 'double',
        vfocuspars = [-0.08, 1.04],
        hfocuspars = [78.03, 190.3],
        abslimits = [1.5, 80],
        focusv = 'mcv',
        focush = 'mch',
        mt = 'mt'
    ),
    ei = device('nicos.core.device.DeviceAlias',
        description = 'Alias for driving the monochromator',
        alias = 'mono',
    ),
)
