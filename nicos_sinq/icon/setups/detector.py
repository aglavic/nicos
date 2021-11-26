description = 'Camini Camera Synchronisation Detector'

pvprefix = 'SQ:ICON:CAMINI:'
pvprefix_sumi = 'SQ:ICON:sumi:'
pvprefix_ai = 'SQ:ICON:B5ADC:'

includes = ['shutters']
excludes = ['detector_phys']

display_order = 90

devices = dict(
    cam_shut = device('nicos_sinq.devices.epics.EpicsReadable',
        epicstimeout = 3.0,
        description = 'Camera shutter open',
        readpv = pvprefix + 'SHUTTER',
        lowlevel = True,
    ),
    cam_arm = device('nicos_sinq.devices.epics.EpicsReadable',
        epicstimeout = 3.0,
        description = 'Camera ready for acquisition',
        readpv = pvprefix + 'ARM',
        lowlevel = True,
    ),
    cam_trig = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        epicstimeout = 3.0,
        description = 'Camera trigger signal',
        readpv = pvprefix + 'TRIG',
        writepv = pvprefix + 'TRIG',
        lowlevel = True,
    ),
    cam_aux = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        epicstimeout = 3.0,
        description = 'Exposure valid signal',
        readpv = pvprefix + 'AUX',
        writepv = pvprefix + 'AUX',
        lowlevel = True,
    ),
    cam_valid = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        epicstimeout = 3.0,
        description = 'Metadata valid signal',
        readpv = pvprefix + 'VALID',
        writepv = pvprefix + 'VALID',
        lowlevel = True,
    ),
    camini = device('nicos_sinq.devices.camini.CaminiDetector',
        epicstimeout = 3.0,
        description = 'Synchronization with the CAMINI camera '
        'software',
        trigpv = pvprefix + 'TRIG',
        validpv = pvprefix + 'VALID',
        metapv = pvprefix + 'META',
        shutpv = pvprefix + 'SHUTTER',
        armpv = pvprefix + 'ARM',
        filepv = pvprefix + 'FILE',
        shutter = 'exp_shutter',
        auto = 'exp_auto',
        beam_current = 'beam_current',
        rate_threshold = 'exp_threshold',
        arm_timeout = 5.0,
        shutter_timeout = 5.0,
        exposure_timeout = 300.0,
        lowlevel = False
    ),
    exp_threshold = device('nicos_sinq.devices.epics.generic.WindowMoveable',
        description = 'Exposure threshold',
        readpv = pvprefix_sumi + 'THRES',
        writepv = pvprefix_sumi + 'THRES',
        window = 10,
        abslimits = (-100, 2000),
        epicstimeout = 3.0
    ),
    exp_ok = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'Exposure sufficient',
        readpv = pvprefix + 'AUX',
        epicstimeout = 3.0
    ),
    exp_avg = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'Average exposure',
        readpv = pvprefix_sumi + 'BEAMAVG',
        epicstimeout = 3.0
    ),
    beam_current = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'Beam current',
        readpv = pvprefix_ai + 'V4',
        epicstimeout = 3.0
    ),
    exp_time = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'Exposure time',
        readpv = pvprefix_sumi + 'EXPTIME',
        epicstimeout = 3.0
    ),
    oracle = device('nicos_sinq.devices.beamoracle.BeamOracle',
        description = 'Device to sum proton count',
        pvprefix = pvprefix_sumi,
        lowlevel = True,
        epicstimeout = 3.0
    ),
    camera = device('nicos_sinq.devices.ccdcontrol.NIAGControl',
        description = 'Count control for NIAG CCD detectors',
        trigger = 'camini',
        followers = ['oracle'],
        rate_monitor = 'oracle',
        rate_threshold = 'exp_threshold',
        exp_ok = 'exp_ok',
    )
)
startupcode = '''
SetDetectors(camera)
'''
