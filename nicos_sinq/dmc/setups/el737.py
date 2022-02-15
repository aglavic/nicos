description = 'Old detector devices in the SINQ DMC.'

pvmprefix = 'SQ:DMC:mcu2:'
pvprefix = 'SQ:DMC:counter'

excludes = ['detector', 'andorccd']

devices = dict(
    s2t = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Detector Two Theta',
        motorpv = pvmprefix + 'S2T',
        errormsgpv = pvmprefix + 'S2T-MsgTxt',
    ),
    timepreset = device('nicos_ess.devices.epics.detector.EpicsTimerActiveChannel',
        description = 'Used to set and view time preset',
        unit = 'sec',
        readpv = pvprefix + '.TP',
        presetpv = pvprefix + '.TP',
    ),
    elapsedtime = device('nicos_ess.devices.epics.detector.EpicsTimerPassiveChannel',
        description = 'Used to view elapsed time while counting',
        unit = 'sec',
        readpv = pvprefix + '.T',
    ),
    monitorpreset = device('nicos_ess.devices.epics.detector.EpicsCounterActiveChannel',
        description = 'Used to set and view monitor preset',
        type = 'monitor',
        readpv = pvprefix + '.PR2',
        presetpv = pvprefix + '.PR2',
    ),
    c1 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'First scalar counter channel',
        type = 'monitor',
        lowlevel = True,
        readpv = pvprefix + '.S2',
    ),
    c2 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Second scalar counter channel',
        type = 'monitor',
        lowlevel = True,
        readpv = pvprefix + '.S3',
    ),
    c3 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Third scalar counter channel',
        type = 'monitor',
        lowlevel = True,
        readpv = pvprefix + '.S4',
    ),
    c4 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Fourth scalar counter channel',
        type = 'monitor',
        lowlevel = True,
        readpv = pvprefix + '.S5',
    ),
    c5 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Fifth scalar counter channel',
        type = 'monitor',
        lowlevel = True,
        readpv = pvprefix + '.S6',
    ),
    c6 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Sixth scalar counter channel',
        type = 'monitor',
        lowlevel = True,
        readpv = pvprefix + '.S7',
    ),
    c7 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Seventh scalar counter channel',
        type = 'monitor',
        lowlevel = True,
        readpv = pvprefix + '.S8',
    ),
    c8 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Eighth scalar counter channel',
        type = 'monitor',
        lowlevel = True,
        readpv = pvprefix + '.S9',
    ),
    proton_current = device('nicos.devices.epics.EpicsReadable',
        description = 'Proton current monitor',
        readpv = 'MHC6:IST:2',
        unit = 'uA',
        fmtstr = '%3.3f',
        pollinterval = 2,
    ),
    el737 = device('nicos_sinq.devices.detector.SinqDetector',
        description = 'EL737 counter box that counts neutrons and '
        'starts streaming events',
        startpv = pvprefix + '.CNT',
        pausepv = pvprefix + ':Pause',
        statuspv = pvprefix + ':Status',
        errormsgpv = pvprefix + ':MsgTxt',
        thresholdpv = pvprefix + ':Threshold',
        monitorpreset = 'monitorpreset',
        timepreset = 'timepreset',
        timers = ['elapsedtime'],
        monitors = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'],
        liveinterval = 30,
        saveintervals = [60]
    ),
   jubit_image = device('nicos_sinq.dmc.devices.dmcbinner.DMCBinner',
       description = 'Histogrammer for event data',
       hist_topic = configdata('config.JUST_BIN_IT_HISTOGRAMS_TOPIC'),
       data_topic =configdata('config.JUST_BIN_IT_DATA_TOPIC'),
       brokers = configdata('config.KAFKA_BROKERS'),
       unit = 'evts',
       hist_type = '2-D DET',
       tof_range = [0, 1000000000],
       det_range = [0, 12000],
       det_width = 200,
       det_height = 60,
   ),
   jubit=device('nicos_ess.devices.datasources.just_bin_it.JustBinItDetector',
       description = 'The just-bin-it histogrammer',
       brokers = configdata('config.KAFKA_BROKERS'),
       unit = '',
       command_topic = configdata('config.JUST_BIN_IT_COMMANDS_TOPIC'),
       response_topic = configdata('config.JUST_BIN_IT_RESPONSES_TOPIC'),
       images=['jubit_image'],
   ),
    dmcdet = device('nicos_sinq.devices.detector.ControlDetector',
        description = 'DMC detector coordination',
        trigger = 'el737',
        followers = ['jubit'],
    )
)
startupcode = '''
SetDetectors(dmcdet)
'''
