description = 'Devices for the Detector'

pvdprefix = 'SQ:FOCUS:counter'
devices = dict(
    timepreset = device('nicos_ess.devices.epics.detector.EpicsTimerActiveChannel',
        epicstimeout = 3.0,
        description = 'Used to set and view time preset',
        unit = 'sec',
        readpv = pvdprefix + '.TP',
        presetpv = pvdprefix + '.TP',
    ),
    elapsedtime = device('nicos_ess.devices.epics.detector.EpicsTimerPassiveChannel',
        epicstimeout = 3.0,
        description = 'Used to view elapsed time while counting',
        unit = 'sec',
        readpv = pvdprefix + '.T',
    ),
    monitorpreset = device('nicos_ess.devices.epics.detector.EpicsCounterActiveChannel',
        epicstimeout = 3.0,
        description = 'Used to set and view monitor preset',
        type = 'monitor',
        readpv = pvdprefix + '.PR2',
        presetpv = pvdprefix + '.PR2',
    ),
    monitor1 = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        epicstimeout = 3.0,
        description = 'First scalar counter channel',
        type = 'monitor',
        readpv = pvdprefix + '.S4',
    ),
    beam_monitor = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        epicstimeout = 3.0,
        description = 'Second scalar counter channel',
        type = 'monitor',
        readpv = pvdprefix + '.S3',
    ),
    tof_sum = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        epicstimeout = 3.0,
        description = 'Third scalar counter channel',
        type = 'monitor',
        readpv = pvdprefix + '.S4',
    ),
    protoncount = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        epicstimeout = 3.0,
        description = 'Fourth scalar counter channel',
        type = 'monitor',
        readpv = pvdprefix + '.S6',
    ),
    # As all banks use the same time binning, this axis is shared
    hm_tof_array = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfTofArray',
        description = 'TOF Array for histogramming',
        lowlevel = True,
        tag = 'tof',
        dim = [
            5,
        ],
        data = [10, 20, 30, 40, 50],
        formatter = '%9d',
    ),
    middle_theta = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfArray',
        description = 'Middle bank two-theta',
        dim = [2],
        data = [0, 0],
        lowlevel = True,
        tag = 'mtheta'
    ),
    lower_theta = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfArray',
        description = 'lower bank two-theta',
        dim = [2],
        data = [0, 0],
        lowlevel = True,
        tag = 'ltheta'
    ),
    upper_theta = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfArray',
        description = 'Upper bank two-theta',
        dim = [2],
        data = [0, 0],
        lowlevel = True,
        tag = 'utheta'
    ),
    merged_theta = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfArray',
        description = 'Merged bank two-theta',
        dim = [2],
        data = [0, 0],
        lowlevel = True,
        tag = 'metheta'
    ),
    hm_ax_tof = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfAxis',
        description = 'TOF axis',
        lowlevel = True,
        mapping = 'boundary',
        array = 'hm_tof_array',
        label = 'TOF',
        unit = 'ms'
    ),
    delay = device('nicos.devices.generic.manual.ManualMove',
        description = 'A place to keep the delay value',
        abslimits = (0, 10000),
        unit = 'ms'
    ),
    merged_image = device('nicos_sinq.focus.devices.detector.MergedImageChannel',
        description = 'Image merged from middle, upper and lower banks',
        tof = 'hm_tof_array',
        mergefile = 'nicos_sinq/focus/focusmerge.dat'
    ),
    el737 = device('nicos_sinq.devices.detector.SinqDetector',
        epicstimeout = 3.0,
        description = 'EL737 counter box that counts neutrons and '
        'starts streaming events',
        startpv = pvdprefix + '.CNT',
        pausepv = pvdprefix + ':Pause',
        statuspv = pvdprefix + ':Status',
        errormsgpv = pvdprefix + ':MsgTxt',
        thresholdpv = pvdprefix + ':Threshold',
        thresholdcounterpv = pvdprefix + ':ThresholdCounter',
        monitorpreset = 'monitorpreset',
        timepreset = 'timepreset',
        timers = ['elapsedtime'],
        monitors = [
            'monitor1',
            'protoncount',
            'beam_monitor',
            'tof_sum',
        ],
        images = [
            'merged_image',
        ],
        liveinterval = 7,
        saveintervals = [60]
    ),
    focusdet = device('nicos_sinq.focus.devices.detector.FocusDetector',
        description = 'FOCUS detector control',
        trigger = 'el737',
        followers = [],
        liveinterval = 120,
        saveintervals = [0, 900, 900],
    ),
    em_td = device('nicos_sinq.devices.epics.generic.WindowMoveable',
        description = 'Emmenegger time delay',
        readpv = 'SQ:FOCUS:EMMI:TD_RBV',
        writepv = 'SQ:FOCUS:EMMI:TD',
        window = 10,
        abslimits = (0, 100000)
    ),
    em_aw = device('nicos_sinq.devices.epics.generic.WindowMoveable',
        description = 'Emmenegger acceptance window',
        readpv = 'SQ:FOCUS:EMMI:AW_RBV',
        writepv = 'SQ:FOCUS:EMMI:AW',
        window = 5,
        abslimits = (0, 5000)
    ),
)
startupcode = """
LoadThetaArrays()
SetDetectors(focusdet)
"""
