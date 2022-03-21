description = 'detector related devices including beamstop'

# included by sans1
group = 'lowlevel'

tangohost = 'tango://sans1hw.sans1.frm2:10000'
detector_base = 'tango://mesydaq.sans1.frm2.tum.de:10000/qm/qmesydaq/'

BS1_X_OFS = -475.055  # from entangle

devices = dict(
    det1_t_ist = device('nicos.devices.entangle.TimerChannel',
        description = 'measured time of detector 1',
        tangodevice = detector_base + 'timer',
        fmtstr = '%.0f',
        visibility = (),
        maxage = 120,
        pollinterval = 15,
    ),
    # det1_t_ist = device('nicos.devices.entangle.TimerChannel',
    #     tangodevice = detector_base + 'det',
    #     fmtstr = '%.1f',
    #     pollinterval = 1,
    #     maxage = 3,
    #     # visibility = (),
    # ),
    # det1_t_soll = device('nicos.devices.entangle.TimerChannel',
    #     tangodevice = detector_base + 'timer',
    #     fmtstr = '%.1f',
    #     pollinterval = 5,
    #     maxage = 13,
    #     # visibility = (),
    # ),
    det1_hv_interlock = device('nicos.devices.entangle.DigitalInput',
        description = 'interlock for detector 1 high voltage',
        tangodevice = '%s/sans1/interlock/hv' % (tangohost, ),
        visibility = (),
    ),
    det1_hv_discharge_mode = device('nicos.devices.entangle.DigitalInput',
        description = 'set discharge mode of detector 1',
        tangodevice = '%s/sans1/interlock/mode' % (tangohost, ),
        visibility = (),
    ),
    det1_hv_discharge = device('nicos.devices.entangle.DigitalOutput',
        description = 'enable and disable discharge of detector 1',
        tangodevice = '%s/sans1/interlock/discharge' % (tangohost, ),
        visibility = (),
    ),
    det1_hv_supply = device('nicos_mlz.sans1.devices.hv.VoltageSupply',
        description = 'high voltage power supply of detector 1',
        tangodevice = tangohost + '/sans1/detector/hv',
        abslimits = (0.0, 1501.0),
        maxage = 120,
        pollinterval = 15,
        fmtstr = '%d',
        visibility = (),
        precision = 3,
    ),
    det1_hv_ax = device('nicos_mlz.sans1.devices.hv.Sans1HV',
        description = 'high voltage of detector 1',
        unit = 'V',
        fmtstr = '%d',
        supply = 'det1_hv_supply',
        discharger = 'det1_hv_discharge',
        interlock = 'det1_hv_interlock',
        maxage = 120,
        pollinterval = 15,
        visibility = (),
    ),
    det1_hv_offtime = device('nicos_mlz.sans1.devices.hv.Sans1HVOffDuration',
        description = 'Duration below operating voltage',
        hv_supply = 'det1_hv_ax',
        maxage = 120,
        pollinterval = 15,
    ),
    det1_hv = device('nicos_mlz.sans1.devices.hv.VoltageSwitcher',
        description = 'high voltage of detector 1 switcher',
        moveable = 'det1_hv_ax',
        mapping = {'ON': (1500, 1),
                   'LOW': (36, 33),
                   'OFF': (0, 2)},
        precision = 1,
        unit = '',
        fallback = 'unknown',
    ),
    hv_current = device('nicos.devices.generic.ReadonlyParamDevice',
        description = 'high voltage current of detector 1',
        device = 'det1_hv_supply',
        parameter = 'current',
        maxage = 120,
        pollinterval = 15,
        visibility = (),
    ),
    det1_x = device('nicos.devices.generic.Axis',
        description = 'detector 1 x axis',
        fmtstr = '%.0f',
        abslimits = (4, 570),
        maxage = 120,
        pollinterval = 5,
        requires = dict(level = 'admin'),
        precision = 0.3,
        motor = 'det1_xmot',
        coder = 'det1_xenc',
    ),
    det1_xmot = device('nicos.devices.entangle.Motor',
        description = 'detector 1 x motor',
        tangodevice = '%s/sans1/detector1/x_mot' % (tangohost, ),
        fmtstr = '%.1f',
        abslimits = (4, 570),
        visibility = (),
    ),
    det1_xenc = device('nicos.devices.entangle.Sensor',
        description = 'detector 1 x motor',
        tangodevice = '%s/sans1/detector1/x_enc' % (tangohost, ),
        fmtstr = '%.1f',
        visibility = (),
    ),
    det1_z = device('nicos_mlz.sans1.devices.detector.DetectorTranslation',
        description =
        'detector 1 z position interlocked with high voltage supply',
        device = 'det1_z_ax',
        lock = 'det1_hv',
        # lockvalue = None,     # go back to previous value
        unlockvalue = 'LOW',
        # keepfixed = False,    # do not fix supply voltage after movement
        fmtstr = '%.0f',
        maxage = 120,
        pollinterval = 15,
    ),
    det1_z_ax = device('nicos.devices.generic.Axis',
        description = 'detector 1 z axis',
        fmtstr = '%.0f',
        abslimits = (1100, 20000),
        maxage = 120,
        pollinterval = 5,
        visibility = (),
        precision = 1.0,
        dragerror = 150.0,
        motor = 'det1_zmot',
        coder = 'det1_zenc',
    ),
    det1_zmot = device('nicos_mlz.sans1.devices.hv.Sans1ZMotor',
        description = 'detector 1 z motor',
        tangodevice = '%s/sans1/detector1/z_mot' % (tangohost, ),
        fmtstr = '%.1f',
        abslimits = (1100, 20000),
        userlimits = (1111, 20000),
        visibility = (),
    ),
    det1_zenc = device('nicos.devices.entangle.Sensor',
        description = 'detector 1 z encoder',
        tangodevice = '%s/sans1/detector1/z_enc' % (tangohost, ),
        fmtstr = '%.1f',
        visibility = (),
    ),
    det1_omg = device('nicos.devices.generic.Axis',
        description = 'detector 1 omega axis',
        fmtstr = '%.0f',
        maxage = 120,
        pollinterval = 5,
        requires = dict(level = 'admin'),
        precision = 0.2,
        motor = 'det1_omegamot',
    ),
    det1_omegamot = device('nicos.devices.entangle.Motor',
        description = 'detector 1 omega motor',
        tangodevice = '%s/sans1/detector1/omg_mot' % (tangohost, ),
        fmtstr = '%.1f',
        # abslimits = (-0.2, 21),
        visibility = (),
    ),

    bs1_xmot = device('nicos.devices.entangle.Motor',
        description = 'beamstop 1 x motor',
        tangodevice = '%s/sans1/beamstop1/x_mot' % tangohost,
        fmtstr = '%.2f',
        # abslimits = (480, 868), # taken from entangle
        visibility = (),
    ),
    # bs1_xenc = device('nicos.devices.entangle.Sensor',
    bs1_xenc = device('nicos_mlz.sans1.devices.beamstop.FunnySensor',
        description = 'beamstop 1 x coder',
        tangodevice = '%s/sans1/beamstop1/x_enc' % (tangohost, ),
        fmtstr = '%.2f',
        visibility = (),
        limits = [0, 1000],
    ),
    bs1_ymot = device('nicos.devices.entangle.Motor',
        description = 'beamstop 1 y motor',
        tangodevice = '%s/sans1/beamstop1/y_mot' % tangohost,
        fmtstr = '%.1f',
        # abslimits = (60, 590), # taken from entangle
        visibility = (),
    ),
    # bs1_yenc = device('nicos.devices.entangle.Sensor',
    bs1_yenc = device('nicos_mlz.sans1.devices.beamstop.FunnySensor',
        description = 'beamstop 1 y coder',
        tangodevice = '%s/sans1/beamstop1/y_enc' % (tangohost, ),
        fmtstr = '%.1f',
        visibility = (),
        limits = [-100, 600],
    ),
    bs1_xax = device('nicos_mlz.sans1.devices.beamstop.BeamStopAxis',
        description = 'beamstop 1 x axis',
        motor = 'bs1_xmot',
        coder = 'bs1_xenc',
        precision = 0.1,
        fmtstr = '%.2f',
        visibility = (),
    ),
    bs1_yax = device('nicos_mlz.sans1.devices.beamstop.BeamStopAxis',
        description = 'beamstop 1 y axis',
        motor = 'bs1_ymot',
        coder = 'bs1_yenc',
        precision = 0.1,
        fmtstr = '%.2f',
        visibility = ()
    ),
    bs1 = device('nicos_mlz.sans1.devices.beamstop.BeamStop',
        description = 'selects the shape of the beamstop',
        xaxis = 'bs1_xax',
        yaxis = 'bs1_yax',
        ypassage = -99, # encoder value! # XXX!
        unit = 'mm',
        slots = { # in encoder values !
            '100x100' : (125.2 - BS1_X_OFS, (100, 100)),
            'd35'     : (197.0 - BS1_X_OFS, (35, 35)),
            '70x70'   : (253.4 - BS1_X_OFS, (70, 70)),
            '55x55'   : (317.4 - BS1_X_OFS, (55, 55)),
            'none'    : (348.0 - BS1_X_OFS, (0, 0)),  # no shapeholder!
            '85x85'   : (390.4 - BS1_X_OFS, (85, 85)),
        },
        # limits for free-move area (in encoder values!)
        xlimits = (480, 868), # XXX!
        ylimits = (100, 590), # XXX!
        # requires = dict(level='admin'),
    ),
    bs1_shape = device('nicos.devices.generic.ParamDevice',
        description = 'selected beam shape',
        device = 'bs1',
        parameter = 'shape',
        copy_status = True,
        requires = {'level': 'admin'},
    ),
)
