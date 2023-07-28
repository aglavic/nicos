description = 'CAMEA basic devices: motors, counters and such'

display_order = 20

pvmcu1 = 'SQ:CAMEA:mcu1:'
pvmcu2 = 'SQ:CAMEA:mcu2:'
pvmcu3 = 'SQ:CAMEA:mcu3:'
pvmcu4 = 'SQ:CAMEA:mcu4:'

devices = dict(
    s2t = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample two theta',
        motorpv = pvmcu1 + '2t',
        errormsgpv = pvmcu1 + '2t-MsgTxt',
        precision = 0.02,
        can_disable = True,
        auto_enable = True,
    ),
    m2t = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Monochromator two theta',
        motorpv = pvmcu1 + '2tm',
        errormsgpv = pvmcu1 + '2tm-MsgTxt',
        precision = 0.02,
        can_disable = True,
        auto_enable = True,
    ),
    som = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample rotation',
        motorpv = pvmcu1 + 'som',
        errormsgpv = pvmcu1 + 'som-MsgTxt',
        precision = 0.02,
        can_disable = True,
        auto_enable = True,
    ),
    tl_sim = device('nicos.devices.generic.ManualMove',
        description = 'Simulated tl motor',
        abslimits = (-15, 15),
        default = 0,
        unit = 'mm',
    ),
    tu_sim = device('nicos.devices.generic.ManualMove',
        description = 'Simulated tu motor',
        abslimits = (-15, 15),
        default = 0,
        unit = 'mm',
    ),
    gl_sim = device('nicos.devices.generic.ManualMove',
        description = 'Simulated gl motor',
        abslimits = (-15, 15),
        default = 0,
        unit = 'degree',
    ),
    gu_sim = device('nicos.devices.generic.ManualMove',
        description = 'Simulated gu motor',
        abslimits = (-15, 15),
        default = 0,
        unit = 'degree',
    ),
    sgl = device('nicos.core.device.DeviceAlias',
        description = 'Alias goniometer lower',
        alias = 'gl_sim',
    ),
    sgu = device('nicos.core.device.DeviceAlias',
        description = 'Alias goniometer upper',
        alias = 'gu_sim',
    ),
    gm = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Monochromator goniometer',
        motorpv = pvmcu3 + 'gm',
        errormsgpv = pvmcu3 + 'gm-MsgTxt',
        precision = 0.02,
        can_disable = True,
        auto_enable = True,
    ),
    mcv = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Monochromator curvature',
        motorpv = pvmcu3 + 'mcv',
        errormsgpv = pvmcu3 + 'mcv-MsgTxt',
        precision = 5,
        can_disable = True,
        auto_enable = True,
    ),
    mch = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Monochromator curvature',
        motorpv = pvmcu3 + 'mch',
        errormsgpv = pvmcu3 + 'mch-MsgTxt',
        precision = 5,
        can_disable = True,
        auto_enable = True,
    ),
    omm = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Monochromator rotation',
        motorpv = pvmcu3 + 'omm',
        errormsgpv = pvmcu3 + 'omm-MsgTxt',
        precision = 0.05,
        can_disable = True,
        auto_enable = True,
    ),
    tlm = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Monochromator lower translation',
        motorpv = pvmcu3 + 'tlm',
        errormsgpv = pvmcu3 + 'tlm-MsgTxt',
        precision = 0.02,
        can_disable = True,
        auto_enable = True,
    ),
    tum = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Monochromator upper translation',
        motorpv = pvmcu3 + 'tum',
        errormsgpv = pvmcu3 + 'tum-MsgTxt',
        precision = 0.02,
        can_disable = True,
        auto_enable = True,
    ),
    vsl = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Virtual slit left',
        motorpv = pvmcu4 + 'vsl',
        errormsgpv = pvmcu4 + 'vsl-MsgTxt',
        precision = 0.02,
        can_disable = True,
        auto_enable = True,
    ),
    vsr = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Virtual slit rright',
        motorpv = pvmcu4 + 'vsr',
        errormsgpv = pvmcu4 + 'vsr-MsgTxt',
        precision = 0.02,
        can_disable = True,
        auto_enable = True,
    ),
    mono = device('nicos_sinq.camea.devices.cameamono.CameaMono',
        description = 'Camea monochromator',
        theta = 'omm',
        twotheta = 'm2t',
        dvalue = 3.354,
        scatteringsense = 1,
        crystalside = 1,
        unit = 'meV',
        focmode = 'vertical',
        vfocuspars = [3.72, 102.79],
        abslimits = [2.75, 17],
        focusv = 'mcv',
        focush = 'mch',
        hfocuspars = [10.06, 271.57],
        upper_trans = [0.0, 0.0],
        lower_trans = [0.0, 0.0],
        lower = 'tlm',
        upper = 'tum',
    ),
    a5 = device('nicos.devices.generic.virtual.VirtualMotor',
        description = 'Virtual a5 motor for analyser',
        speed = 10000,
        unit = 'deg',
        precision = .02,
        abslimits = (-180., 180.)
    ),
    a6 = device('nicos.devices.generic.virtual.VirtualMotor',
        description = 'Virtual a6 motor for analyser',
        speed = 10000,
        unit = 'deg',
        precision = .02,
        abslimits = (-360., 360.)
    ),
    ana = device('nicos_sinq.devices.mono.SinqMonochromator',
        description = 'Camea analyser',
        theta = 'a5',
        twotheta = 'a6',
        dvalue = 3.354,
        scatteringsense = 1,
        crystalside = 1,
        unit = 'meV',
        focmode = 'flat',
        abslimits = (2.75, 20),
    ),
    ei = device('nicos.core.device.DeviceAlias',
        description = 'Alias for driving the monochromator',
        alias = 'mono',
    ),
    ef = device('nicos.core.device.DeviceAlias',
        description = 'Alias for driving the analyser',
        alias = 'ana',
    ),
    a1 = device('nicos.core.device.DeviceAlias',
        description = 'Alias monochromator theta',
        alias = 'omm',
    ),
    a2 = device('nicos.core.device.DeviceAlias',
        description = 'Alias monochromator two theta',
        alias = 'm2t',
    ),
    a3 = device('nicos.core.device.DeviceAlias',
        description = 'Alias sample rotation',
        alias = 'som',
    ),
    a4 = device('nicos_sinq.camea.devices.a4motor.CameaA4Motor',
        description = 'Real A4 with special offset',
        rawa4 = 's2t',
        unit = 'deg',
    ),
    calib1 = device('nicos_sinq.camea.devices.calibration.CalibrationData',
        description = 'Data class for calibration data'
    ),
    calib2 = device('nicos_sinq.camea.devices.calibration.CalibrationData',
        description = 'Data class for calibration data'
    ),
    calib3 = device('nicos_sinq.camea.devices.calibration.CalibrationData',
        description = 'Data class for calibration data'
    ),
    calib4 = device('nicos_sinq.camea.devices.calibration.CalibrationData',
        description = 'Data class for calibration data'
    ),
    calib5 = device('nicos_sinq.camea.devices.calibration.CalibrationData',
        description = 'Data class for calibration data'
    ),
    calib6 = device('nicos_sinq.camea.devices.calibration.CalibrationData',
        description = 'Data class for calibration data'
    ),
    calib7 = device('nicos_sinq.camea.devices.calibration.CalibrationData',
        description = 'Data class for calibration data'
    ),
    calib8 = device('nicos_sinq.camea.devices.calibration.CalibrationData',
        description = 'Data class for calibration data'
    ),
    detNo = device('nicos.devices.generic.manual.ManualMove',
        description = 'Number of detector selected for summing',
        unit = 'number',
        abslimits = (0, 104)
    ),
    anaNo = device('nicos.devices.generic.manual.ManualMove',
        description = 'Number of analyser selected for summing',
        unit = 'number',
        abslimits = (0, 8)
    ),
)

# when se_om (the sample stick rotation) is present, use this for a3
alias_config = {'a3': {'som': 10, }}

startupcode = """
sgl.alias = 'gl_sim'
sgu.alias = 'gu_sim'
"""
