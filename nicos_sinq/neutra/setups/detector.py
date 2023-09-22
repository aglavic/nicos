description = 'Camini Camera Synchronisation Detector'

pvprefix = 'SQ:NEUTRA:CAMINI:'
pvprefix_sumi = 'SQ:NEUTRA:sumi:'
pvprefix_ai = 'SQ:NEUTRA:B5ADC:'

includes = ['shutters']

display_order = 70

devices = dict(
    cam_shut = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Camera shutter open',
        readpv = pvprefix + 'SHUTTER',
        visibility = set(),
    ),
    cam_arm = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Camera ready for acquisition',
        readpv = pvprefix + 'ARM',
        visibility = set(),
    ),
    cam_trig = device('nicos.devices.epics.pyepics.EpicsDigitalMoveable',
        description = 'Camera trigger signal',
        readpv = pvprefix + 'TRIG',
        writepv = pvprefix + 'TRIG',
        visibility = set(),
    ),
    cam_aux = device('nicos.devices.epics.pyepics.EpicsDigitalMoveable',
        description = 'Exposure valid signal',
        readpv = pvprefix + 'AUX',
        writepv = pvprefix + 'AUX',
        visibility = set(),
    ),
    cam_valid = device('nicos.devices.epics.pyepics.EpicsDigitalMoveable',
        description = 'Metadata valid signal',
        readpv = pvprefix + 'VALID',
        writepv = pvprefix + 'VALID',
        visibility = set(),
    ),
    camini = device('nicos_sinq.devices.camini.CaminiDetector',
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
        visibility = set()
    ),
    exp_threshold = device('nicos.devices.epics.pyepics.EpicsAnalogMoveable',
        description = 'Exposure threshold',
        readpv = pvprefix_sumi + 'THRES',
        writepv = pvprefix_sumi + 'THRES',
        abslimits = (-100, 2000),
    ),
    exp_ok = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Exposure sufficient',
        readpv = pvprefix + 'AUX',
    ),
    exp_avg = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Average exposure',
        readpv = pvprefix_sumi + 'BEAMAVG',
    ),
    beam_current = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Beam current',
        readpv = pvprefix_ai + 'V4',
    ),
    exp_time = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Exposure time',
        readpv = pvprefix_sumi + 'EXPTIME',
    ),
    oracle = device('nicos_sinq.devices.beamoracle.BeamOracle',
        description = 'Device to sum proton count',
        pvprefix = pvprefix_sumi,
        visibility = set(),
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
