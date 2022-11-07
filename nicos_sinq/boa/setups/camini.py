description = 'Camini Camera Synchronisation Detector'

pvprefix = 'SQ:ICON:CAMINI:'
pvprefix_sumi = 'SQ:ICON:sumi:'
motprefix = 'SQ:BOA:mcu1:DCCDATZ'

excludes = ['andor', 'andorccd', 'embl', 'fastcomtec']

includes = ['single_el737']

devices = dict(
    dccdatz = device('nicos_ess.devices.epics.motor.EpicsMotor',
        description = 'Andor focus motor',
        motorpv = motprefix,
        errormsgpv = motprefix + '-MsgTxt',
    ),
    cam_shut = device('nicos.devices.epics.EpicsReadable',
        description = 'Camera shutter open',
        readpv = pvprefix + 'SHUTTER',
        visibility = (),
    ),
    cam_arm = device('nicos.devices.epics.EpicsReadable',
        description = 'Camera ready for acquisition',
        readpv = pvprefix + 'ARM',
        visibility = (),
    ),
    cam_trig = device('nicos_sinq.devices.camini.CaminiTrigger',
        description = 'Camera trigger signal',
        readpv = pvprefix + 'TRIG',
        writepv = pvprefix + 'TRIG',
        visibility = (),
    ),
    cam_aux = device('nicos.devices.epics.EpicsReadable',
        description = 'Exposure valid signal',
        readpv = pvprefix + 'AUX',
        visibility = (),
    ),
    cam_valid = device('nicos.devices.epics.EpicsDigitalMoveable',
        description = 'Metadata valid signal',
        readpv = pvprefix + 'VALID',
        writepv = pvprefix + 'VALID',
        visibility = (),
    ),
    beam_current = device('nicos.devices.epics.EpicsReadable',
        description = 'Beam current',
        readpv = 'SQ:ICON:sumi:BEAMCOPY',
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
        shutter = 'shutter',
        auto = 'shutterauto',
        beam_current = 'beam_current',
        rate_threshold = 'exp_threshold',
        arm_timeout = 5.0,
        shutter_timeout = 5.0,
        exposure_timeout = 300.0,
        visibility = ()
    ),
    exp_threshold = device('nicos.devices.epics.EpicsAnalogMoveable',
        description = 'Exposure threshold',
        readpv = pvprefix_sumi + 'THRES',
        writepv = pvprefix_sumi + 'THRES',
        abslimits = (-100, 2000),
    ),
    exp_ok = device('nicos.devices.epics.EpicsReadable',
        description = 'Exposure sufficient',
        readpv = pvprefix + 'AUX',
    ),
    exp_avg = device('nicos.devices.epics.EpicsReadable',
        description = 'Average exposure',
        readpv = pvprefix_sumi + 'BEAMAVG',
    ),
    exp_time = device('nicos.devices.epics.EpicsReadable',
        description = 'Exposure time',
        readpv = pvprefix_sumi + 'EXPTIME',
    ),
    oracle = device('nicos_sinq.devices.beamoracle.BeamOracle',
        description = 'Device to sum proton count',
        pvprefix = pvprefix_sumi,
        visibility = (),
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
