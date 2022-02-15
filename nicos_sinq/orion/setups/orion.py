description = 'Base setup file for ORION devices'

pvmcu1 = 'SQ:ORION:mcu1:'
pvmcu2 = 'SQ:ORION:mcu2:'
pvdet = 'SQ:ORION:counter'

devices = dict(
    mom1 = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator 1 rotation',
        motorpv = pvmcu2 + 'mom1',
        errormsgpv = pvmcu2 + 'mom1-MsgTxt',
        precision = 0.5,
        fmtstr = '%8.3f',
    ),
    gml = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator lower goniometer',
        motorpv = pvmcu2 + 'gml',
        errormsgpv = pvmcu2 + 'gml-MsgTxt',
        precision = 0.02,
        fmtstr = '%8.3f',
    ),
    gmu = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator upper goniometer',
        motorpv = pvmcu2 + 'gmu',
        errormsgpv = pvmcu2 + 'gmu-MsgTxt',
        precision = 0.02,
        fmtstr = '%8.3f',
    ),
    som = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample rotation',
        motorpv = pvmcu1 + 'som',
        errormsgpv = pvmcu1 + 'som-MsgTxt',
        precision = 0.5,
        fmtstr = '%8.3f',
    ),
    stt = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Two Theta rotation',
        motorpv = pvmcu1 + 'stt',
        errormsgpv = pvmcu1 + 'stt-MsgTxt',
        precision = 0.5,
        fmtstr = '%8.3f',
    ),
    sgl = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample lower tilt',
        motorpv = pvmcu1 + 'sgl',
        errormsgpv = pvmcu1 + 'sgl-MsgTxt',
        fmtstr = '%8.3f',
        precision = 0.5,
    ),
    sgu = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Sample upper tilt',
        motorpv = pvmcu1 + 'sgu',
        errormsgpv = pvmcu1 + 'sgu-MsgTxt',
        fmtstr = '%8.3f',
        precision = 0.5,
    ),
    chi = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Eulerian cradle chi rotation',
        motorpv = pvmcu1 + 'chi',
        errormsgpv = pvmcu1 + 'chi-MsgTxt',
        fmtstr = '%8.3f',
        precision = 0.5,
    ),
    phi = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Eulerian cradle phi rotation',
        motorpv = pvmcu1 + 'phi',
        errormsgpv = pvmcu1 + 'phi-MsgTxt',
        fmtstr = '%8.3f',
        precision = 0.5,
    ),
    mcv1 = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Monochromator vertical curvature',
        motorpv = pvmcu2 + 'mcv1',
        errormsgpv = pvmcu2 + 'mcv1-MsgTxt',
        precision = 0.5,
    ),
    mono = device('nicos.devices.generic.Switcher',
        description = 'monochromator',
        moveable = 'mom1',
        mapping = {
            3.3: 2.08,
            1.73: 31.49,
            1.32: 21.25,
        },
        precision = .1,
        unit = 'A'
    ),
    timepreset = device('nicos_ess.devices.epics.detector.EpicsTimerActiveChannel',
        description = 'Used to set and view time preset',
        unit = 'sec',
        readpv = pvdet + '.TP',
        presetpv = pvdet + '.TP',
    ),
    elapsedtime = device('nicos_ess.devices.epics.detector.EpicsTimerPassiveChannel',
        description = 'Used to view elapsed time while counting',
        unit = 'sec',
        readpv = pvdet + '.T',
    ),
    monitorpreset = device('nicos_ess.devices.epics.detector.EpicsCounterActiveChannel',
        description = 'Used to set and view monitor preset',
        type = 'monitor',
        readpv = pvdet + '.PR2',
        presetpv = pvdet + '.PR2',
    ),
    counts = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Actual counts',
        type = 'monitor',
        readpv = pvdet + '.S3',
    ),
    monitor1 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'First scalar counter channel',
        type = 'monitor',
        readpv = pvdet + '.S2',
    ),
    protoncount = device('nicos_ess.devices.epics.detector'
        '.EpicsCounterPassiveChannel',
        description = 'Proton counter channel',
        type = 'monitor',
        readpv = pvdet + '.S5',
    ),
    intensity = device('nicos_sinq.sxtal.commands.Intensity',
        description = 'Dummy to try to get stuff to work'
    ),
    oriondet = device('nicos_sinq.devices.detector.SinqDetector',
        description = 'EL737 counter box that counts neutrons',
        startpv = pvdet + '.CNT',
        pausepv = pvdet + ':Pause',
        statuspv = pvdet + ':Status',
        errormsgpv = pvdet + ':MsgTxt',
        thresholdpv = pvdet + '.PR4',
        thresholdcounterpv = pvdet + '.PR3',
        monitorpreset = 'monitorpreset',
        timepreset = 'timepreset',
        timers = ['elapsedtime'],
        monitors = ['counts', 'monitor1', 'protoncount'],
        images = [],
        others = [],
        liveinterval = 7,
        saveintervals = [60]
    )
)
startupcode = """
SetDetectors(oriondet)
"""
