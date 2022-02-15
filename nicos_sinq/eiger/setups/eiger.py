description = 'Standard EIGER devices minus the monochromator'

mcu2prefix = 'SQ:EIGER:mcu2:'
mcu3prefix = 'SQ:EIGER:mcu3:'
mcu4prefix = 'SQ:EIGER:mcu4:'
cterprefix = 'SQ:EIGER:counter'

devices = dict(
    d1l = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Slit 1 left',
        motorpv = mcu2prefix + 'd1l',
        errormsgpv = mcu2prefix + 'd1l-MsgTxt',
        precision = 0.02,
    ),
    d1r = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Slit 1 right',
        motorpv = mcu2prefix + 'd1r',
        errormsgpv = mcu2prefix + 'd1r-MsgTxt',
        precision = 0.02,
    ),
    vsl = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Virtual source left',
        motorpv = mcu2prefix + 'vsl',
        errormsgpv = mcu2prefix + 'vsr-MsgTxt',
        precision = 0.02,
    ),
    vsr = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Virtual source right',
        motorpv = mcu2prefix + 'vsr',
        errormsgpv = mcu2prefix + 'vsr-MsgTxt',
        precision = 0.02,
    ),
    msl = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample slit left',
        motorpv = mcu2prefix + 'msl',
        errormsgpv = mcu2prefix + 'msl-MsgTxt',
        precision = 0.02,
    ),
    msr = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample slit right',
        motorpv = mcu2prefix + 'msr',
        errormsgpv = mcu2prefix + 'msr-MsgTxt',
        precision = 0.02,
    ),
    msb = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample slit bottom',
        motorpv = mcu4prefix + 'msb',
        errormsgpv = mcu4prefix + 'msb-MsgTxt',
        precision = 0.02,
    ),
    mst = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample slit top',
        motorpv = mcu4prefix + 'mst',
        errormsgpv = mcu4prefix + 'mst-MsgTxt',
        precision = 0.02,
    ),
    a3 = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample rotation',
        motorpv = mcu3prefix + 'a3',
        errormsgpv = mcu3prefix + 'a3-MsgTxt',
        precision = 0.02,
    ),
    sslit = device('nicos.devices.generic.slit.Slit',
        description = 'Sample slilit with left, right, bottom and '
        'top motors',
        opmode = '4blades',
        left = 'msl',
        right = 'msr',
        top = 'mst',
        bottom = 'msb',
        lowlevel = True
    ),
    sslit_opening = device('nicos_sinq.amor.devices.slit.SlitOpening',
        description = 'Sample slit opening controller',
        slit = 'sslit'
    ),
    sslit_width = device('nicos.devices.generic.slit.WidthSlitAxis',
        description = 'Sample slit width controller',
        slit = 'sslit',
        unit = 'mm',
    ),
    a4 = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample two theta',
        motorpv = mcu3prefix + 'a4',
        errormsgpv = mcu3prefix + 'a4-MsgTxt',
        precision = 0.02,
    ),
    sgl = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample lower tilt',
        motorpv = mcu3prefix + 'sgl',
        errormsgpv = mcu3prefix + 'sgl-MsgTxt',
        precision = 0.02,
    ),
    sgu = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample upper tilt',
        motorpv = mcu3prefix + 'sgu',
        errormsgpv = mcu3prefix + 'sgu-MsgTxt',
        precision = 0.02,
    ),
    a5 = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Analyser rotation',
        motorpv = mcu4prefix + 'a5',
        errormsgpv = mcu4prefix + 'a5-MsgTxt',
        precision = 0.02,
    ),
    a6_raw = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Analyser rotation',
        motorpv = mcu4prefix + 'a6',
        errormsgpv = mcu4prefix + 'a6-MsgTxt',
        precision = 0.02,
        lowlevel = True,
    ),
    a6 = device('nicos_sinq.eiger.devices.a6motor.A6Motor',
        description = 'Analyser two theta',
        raw_motor = 'a6_raw',
        wait_period = 7,
        precision = .02,
    ),
    ach = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Analyser horizontal curvature',
        motorpv = mcu4prefix + 'ach',
        errormsgpv = mcu4prefix + 'ach-MsgTxt',
        precision = 0.02,
    ),
    atl = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Analyser lower translation',
        motorpv = mcu4prefix + 'atl',
        errormsgpv = mcu4prefix + 'atl-MsgTxt',
        precision = 0.02,
    ),
    atu = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Analyser upper translation',
        motorpv = mcu4prefix + 'atu',
        errormsgpv = mcu4prefix + 'atu-MsgTxt',
        precision = 0.02,
    ),
    ag = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Analyser goniometer',
        motorpv = mcu4prefix + 'ag',
        errormsgpv = mcu4prefix + 'ag-MsgTxt',
        precision = 0.02,
    ),
    timepreset = device('nicos_ess.devices.epics.detector.EpicsTimerActiveChannel',
        description = 'Used to set and view time preset',
        unit = 'sec',
        readpv = cterprefix + '.TP',
        presetpv = cterprefix + '.TP',
    ),
    elapsedtime = device('nicos_ess.devices.epics.detector.EpicsTimerPassiveChannel',
        description = 'Used to view elapsed time while counting',
        unit = 'sec',
        readpv = cterprefix + '.T',
    ),
    monitorpreset = device('nicos_ess.devices.epics.detector.EpicsCounterActiveChannel',
        description = 'Used to set and view monitor preset',
        type = 'monitor',
        readpv = cterprefix + '.PR2',
        presetpv = cterprefix + '.PR2',
    ),
    ctr1 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'The real neutron counter',
        type = 'monitor',
        readpv = cterprefix + '.S2',
    ),
    mon1 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'First scalar counter channel',
        type = 'monitor',
        readpv = cterprefix + '.S3',
    ),
    mon2 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Second scalar counter channel',
        type = 'monitor',
        readpv = cterprefix + '.S4',
    ),
    protoncount = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Fourth scalar counter channel',
        type = 'monitor',
        readpv = cterprefix + '.S5',
    ),
    counter = device('nicos_sinq.devices.detector.SinqDetector',
        description = 'EL737 counter box that counts neutrons and '
        'starts streaming events',
        startpv = cterprefix + '.CNT',
        pausepv = cterprefix + ':Pause',
        statuspv = cterprefix + ':Status',
        errormsgpv = cterprefix + ':MsgTxt',
        thresholdpv = cterprefix + ':Threshold',
        monitorpreset = 'monitorpreset',
        timepreset = 'timepreset',
        timers = ['elapsedtime'],
        monitors = [
            'ctr1',
            'mon1',
            'mon2',
            'protoncount',
        ],
        liveinterval = 7,
        saveintervals = [60]
    ),
    ana = device('nicos_sinq.eiger.devices.eigermono.EigerMonochromator',
        description = 'EIGER analyser',
        theta = 'a5',
        twotheta = 'a6',
        dvalue = 3.354,
        scatteringsense = 1,
        crystalside = 1,
        unit = 'meV',
        focmode = 'horizontal',
        hfocuspars = [0.21, 3.99],
        abslimits = [2.75, 80],
        focush = 'ach'
    ),
    ef = device('nicos.core.device.DeviceAlias',
        description = 'Alias for driving the analyser',
        alias = 'ana',
    ),
)
startupcode = """
SetDetectors(counter)
"""
