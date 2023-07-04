description = 'qmesydaq devices for REFSANS'

group = 'lowlevel'

sysconfig = dict(
    datasinks = ['LiveViewSink'],
)

devices = dict(
    LiveViewSink = device('nicos.devices.datasinks.LiveViewSink',
        description = 'Sends image data to LiveViewWidget',
    ),
    mon1 = device('nicos.devices.generic.VirtualCounter',
        description = 'QMesyDAQ monitor 2',
        fmtstr = '%d',
        type = 'monitor',
        countrate = 100,
    ),
    mon2 = device('nicos.devices.generic.VirtualCounter',
        description = 'QMesyDAQ monitor 1',
        fmtstr = '%d',
        type = 'monitor',
        countrate = 100,
    ),
    timer = device('nicos.devices.mcstas.McStasTimer',
        description = 'QMesyDAQ timer',
        mcstas = 'mcstas',
    ),
    mcstas = device('nicos_virt_mlz.refsans.devices.detector.McStasSimulation',
        description = 'McStas simulation',
        pollinterval = None,
        sample = 'Sample',
        nok2 = 'nok2',
        nok3 = 'nok3',
        nok4 = 'nok4',
        nok5a = 'nok5a',
        nok5b = 'nok5b',
        nok6 = 'nok6',
        nok7 = 'nok7',
        nok8 = 'nok8',
        nok9 = 'nok9',
        b1 = 'b1',
        b3 = 'b3',
        h3 = 'h3',
        bs1 = 'bs1',
        zb0 = 'zb0',
        zb1 = 'zb1',
        zb2 = 'zb2',
        zb3 = 'zb3',
        pivot = 'det_pivot',
        rpm = 'chopper_speed',
        disc2_pos = 'chopper2_pos',
        backguard = 'backguard',
        yoke = 'det_yoke',
        dettable = 'det_table',
        gonio_theta = 'gonio_theta',
        gonio_y = 'gonio_y',
        gonio_z = 'gonio_z',
        chopper2 = 'chopper2',
        chopper3 = 'chopper3',
        chopper4 = 'chopper4',
        chopper5 = 'chopper5',
        chopper6 = 'chopper6',
        d_b3_sample = 'd_last_slit_sample',
        visibility = (),
    ),
    image = device('nicos.devices.mcstas.McStasImage',
        description = 'Image data device',
        mcstas = 'mcstas',
        mcstasfile = 'Denex_PSD.dat',
        # size = (256, 256),
        size = (229, 234),
        fmtstr = '%d',
        unit = 'cts',
        pollinterval = None,
    ),
    det = device('nicos.devices.generic.Detector',
        description = 'QMesyDAQ Image type Detector1',
        timers = ['timer'],
        monitors = ['mon1', 'mon2'],
        images = ['image'],
    ),
)

startupcode = '''
SetDetectors(det)
'''
