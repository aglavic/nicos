description = 'Camini Camera Synchronisation Detector'

pvprefix = 'SQ:ICON:CAMINI:'
pvprefix_sumi = 'SQ:ICON:sumi:'

excludes = ['andor', 'andorccd', 'embl']

includes = ['single_el737']

devices = dict(
    cam_shut = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = 3.0,
        description = 'Camera shutter open',
        readpv = pvprefix + 'SHUTTER',
        lowlevel = True,
    ),
    cam_arm = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = 3.0,
        description = 'Camera ready for acquisition',
        readpv = pvprefix + 'ARM',
        lowlevel = True,
    ),
    cam_trig = device('nicos_sinq.devices.camini.CaminiTrigger',
        epicstimeout = 3.0,
        description = 'Camera trigger signal',
        readpv = pvprefix + 'TRIG',
        writepv = pvprefix + 'TRIG',
        lowlevel = True,
    ),
    cam_aux = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = 3.0,
        description = 'Exposure valid signal',
        readpv = pvprefix + 'AUX',
        lowlevel = True,
    ),
    cam_valid = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = 3.0,
        description = 'Metadata valid signal',
        readpv = pvprefix + 'VALID',
        writepv = pvprefix + 'VALID',
        lowlevel = True,
    ),
    beam_current = device('nicos.devices.epics.EpicsReadable',
        description = 'Beam current',
        readpv = 'SQ:ICON:sumi:BEAMCOPY',
        epicstimeout = 3.0
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
        shutter = 'shutter',
        auto = 'shutterauto',
        beam_current = 'beam_current',
        rate_threshold = 'exp_threshold',
        arm_timeout = 5.0,
        shutter_timeout = 5.0,
        exposure_timeout = 300.0,
        lowlevel = False
    ),
    exp_threshold = device('nicos.devices.epics.EpicsAnalogMoveable',
        description = 'Exposure threshold',
        readpv = pvprefix_sumi + 'THRES',
        writepv = pvprefix_sumi + 'THRES',
        abslimits = (-100, 2000),
        epicstimeout = 3.0
    ),
    exp_ok = device('nicos.devices.epics.EpicsReadable',
        description = 'Exposure sufficient',
        readpv = pvprefix + 'AUX',
        epicstimeout = 3.0
    ),
    exp_avg = device('nicos.devices.epics.EpicsReadable',
        description = 'Average exposure',
        readpv = pvprefix_sumi + 'BEAMAVG',
        epicstimeout = 3.0
    ),
    exp_time = device('nicos.devices.epics.EpicsReadable',
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
