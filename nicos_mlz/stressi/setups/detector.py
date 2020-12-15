description = 'Detector CARESS HWB Devices'

group = 'lowlevel'

tango_host = 'tango://ps01.stressi.frm2:10000/stressi/det/'
detector_base = 'tango://mesydaq.stressi.frm2.tum.de:10000/qm/qmesydaq/'

devices = dict(
    mon = device('nicos.devices.tango.CounterChannel',
        description = 'HWB MON',
        tangodevice = detector_base + 'counter0',
        fmtstr = '%d',
        type = 'monitor',
        lowlevel = True,
    ),
    t_mon = device('nicos.devices.tango.CounterChannel',
        description = 'HWB MON Transmission Monitor',
        tangodevice = detector_base + 'counter4',
        fmtstr = '%d',
        type = 'monitor',
        lowlevel = True,
    ),
    tim1 = device('nicos.devices.tango.TimerChannel',
        description = 'HWB TIM1',
        tangodevice = detector_base + 'timer',
        fmtstr = '%.2f',
        unit = 's',
        lowlevel = True,
    ),
    # events = device('nicos.devices.tango.CounterChannel',
    #     description = 'All over detector events',
    #     tangodevice = detector_base + 'events',
    #     fmtstr = '%d',
    #     unit = 'cts',
    #     type = 'counter',
    #     lowlevel = True,
    # ),
    image = device('nicos.devices.vendor.qmesydaq.tango.ImageChannel',
        description = 'Image data device',
        tangodevice = detector_base + 'image',
        fmtstr = '%d',
        pollinterval = None,
        lowlevel = True,
    ),
    # histogram = device('nicos_mlz.devices.qmesydaqsinks.HistogramSink',
    #     description = 'Histogram data written via QMesyDAQ',
    #     image = 'image',
    # ),
    listmode = device('nicos_mlz.devices.qmesydaqsinks.ListmodeSink',
        description = 'Listmode data written via QMesyDAQ',
        image = 'image',
    ),
    roi = device('nicos.devices.generic.RectROIChannel',
        description = 'ROI',
        roi = (122, 50, 12, 140),
    ),
    adet = device('nicos.devices.generic.Detector',
        description = 'Classical detector with single channels',
        timers = ['tim1'],
        monitors = ['mon'],
        counters = ['t_mon', 'roi',],  # 'events', ],
        images = ['image'],
        pollinterval = None,
        liveinterval = 1.,
        postprocess = [
            ('roi', 'image'),
        ],
    ),
    ysd = device('nicos.devices.generic.ManualMove',
        description = 'Distance detector to sample',
        fmtstr = '%.1f',
        default = 1035,
        unit = 'mm',
        abslimits = (700, 1700),
        requires = {'level': 'admin'},
    ),
    hv1 = device('nicos.devices.tango.PowerSupply',
        description = 'HV power supply anode',
        requires = {'level': 'admin'},
        tangodevice = tango_host + 'hv1',
        abslimits = (0, 3200),
    ),
    hv1_current = device('nicos.devices.generic.ReadonlyParamDevice',
        description = 'HV power supply anode current',
        device = 'hv1',
        parameter = 'current',
    ),
    hv2 = device('nicos.devices.tango.PowerSupply',
        description = 'HV power supply drift',
        requires = {'level': 'admin'},
        tangodevice = tango_host + 'hv2',
        abslimits = (-2500, 0),
    ),
    hv2_current = device('nicos.devices.generic.ReadonlyParamDevice',
        description = 'HV power supply drift current',
        device = 'hv2',
        parameter = 'current',
    ),
)

startupcode = '''
SetDetectors(adet)
'''
