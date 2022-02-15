description = 'Setup for the ANDOR CCD camera at BOA using the CCDWWW server'

counterprefix = 'SQ:DMC:counter'

excludes = ['detector', 'el737']

devices = dict(
    el737_preset = device('nicos_ess.devices.epics.detector.EpicsTimerActiveChannel',
        description = 'Used to set and view time preset',
        unit = 'sec',
        readpv = f'{counterprefix}.TP',
        presetpv = f'{counterprefix}.TP',
    ),
    elapsedtime = device('nicos_ess.devices.epics.detector.EpicsTimerPassiveChannel',
        description = 'Used to view elapsed time while counting',
        unit = 'sec',
        readpv = f'{counterprefix}.T',
    ),
    monitorpreset = device('nicos_ess.devices.epics.detector.EpicsCounterActiveChannel',
        description = 'Used to set and view monitor preset',
        type = 'monitor',
        readpv = f'{counterprefix}.PR2',
        presetpv = f'{counterprefix}.PR2',
    ),
    monitorval = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Monitor for neutron beam',
        type = 'monitor',
        readpv = f'{counterprefix}.S2',
    ),
    protoncurr = device('nicos_ess.devices.epics.detector.EpicsCounterPassiveChannel',
        description = 'Monitor for proton current',
        type = 'monitor',
        readpv = f'{counterprefix}.S4',
    ),
    ccdwww_connector = device('nicos_sinq.boa.devices.ccdwww.CCDWWWConnector',
        description = 'Connector for CCDWWW',
        baseurl = 'http://mpc2704:8080/ccd',
        base64auth = 'xxx',
        byteorder = 'big',
        comdelay = 1.,
        comtries = 5,
    ),
    ccdwww = device('nicos_sinq.boa.devices.ccdwww.AndorCCD',
        description = 'CCDWWW image channel',
        iscontroller = True,
        connector = 'ccdwww_connector',
        shape = (1024, 1024),
        pollinterval = 30,
        maxage = 30,
    ),
    ccd_cooler = device('nicos_sinq.boa.devices.ccdwww.CCDCooler',
        description = 'CCD sensor cooler',
        connector = 'ccdwww_connector',
        unit = 'state',
        pollinterval = 30,
        maxage = 30,
        fmtstr = '%s'
    ),
    cooler_temperature = device('nicos.devices.generic.paramdev.ReadonlyParamDevice',
        description = 'Actual temperature reading',
        device = 'ccd_cooler',
        parameter = 'temperature',
    ),
    andorccd = device('nicos.devices.generic.detector.Detector',
        description = 'Dummy detector to encapsulate ccdwww',
        monitors = [
            'ccdwww',
        ],
        timers = [
            'ccdwww',
        ],
        images = [
            'ccdwww',
        ],
        lowlevel = True
    ),
    el737 = device('nicos_sinq.devices.detector.SinqDetector',
        description = 'EL737 counter box that counts neutrons and '
        'starts streaming events',
        startpv =    f'{counterprefix}.CNT',
        pausepv =    f'{counterprefix}:Pause',
        statuspv =   f'{counterprefix}:Status',
        errormsgpv = f'{counterprefix}:MsgTxt',
        monitorpreset = [
            'monitorpreset',
        ],
        timepreset = ['el737_preset'],
        thresholdpv = f'{counterprefix}:Threshold',
        thresholdcounterpv = f'{counterprefix}:ThresholdCounter',
    ),
    dmccontrol = device('nicos_sinq.boa.devices.ccdcontrol.BoaControlDetector',
        description = 'DMC CCD control',
        trigger = 'el737',
        followers = ['andorccd'],
        liveinterval = 5,
        minimum_rate = 0,
        rate_monitor = 'monitorval',
        elapsed_time = 'elapsedtime'
    ),
)

startupcode = '''
SetDetectors(dmccontrol)
'''
