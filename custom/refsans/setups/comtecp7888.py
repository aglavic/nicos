description = 'devices for fast detector using comtec p7888 for REFSANS'

# to be included by refsans?
group = 'optional'

excludes = ['detector']

nethost = 'refsanssrv.refsans.frm2'
tacodev = '//%s/test/fast' % nethost

devices = dict(
    RawFileSaver  = device('devices.fileformats.raw.SingleRAWFileFormat',
                           description = 'Saves image data in RAW format',
                           filenametemplate = ['%(proposal)s_%(counter)s.raw',
                                      '%(proposal)s_%(session.experiment.lastscan)s'
                                      '_%(counter)s_%(scanpoint)s.raw'],
                           lowlevel = True,
                          ),
    #~ LiveViewSink = device('devices.fileformats.LiveViewSink',
                          #~ description = 'Sends image data to LiveViewWidget',
                          #~ filenametemplate=[],
                          #~ lowlevel = True,
                         #~ ),
    fastctr_a = device('devices.taco.detector.FRMCounterChannel',
                       description = "Channel A of Comtep P7888 Fast Counter",
                       tacodevice = '%s/rate_a' % tacodev,
                       type = 'counter',
                       mode = 'normal',
                      ),
    fastctr_b = device('devices.taco.detector.FRMCounterChannel',
                       description = "Channel B of Comtep P7888 Fast Counter",
                       tacodevice = '%s/rate_b' % tacodev,
                       type = 'counter',
                       mode = 'normal',
                      ),
    fastctr_c = device('devices.taco.detector.FRMCounterChannel',
                       description = "Channel C of Comtep P7888 Fast Counter",
                       tacodevice = '%s/rate_c' % tacodev,
                       type = 'counter',
                       mode = 'normal',
                      ),
    fastctr_d = device('devices.taco.detector.FRMCounterChannel',
                       description = "Channel D of Comtep P7888 Fast Counter",
                       tacodevice = '%s/rate_d' % tacodev,
                       type = 'counter',
                       mode = 'normal',
                      ),
    fastctr_e = device('devices.taco.detector.FRMCounterChannel',
                       description = "Channel E of Comtep P7888 Fast Counter",
                       tacodevice = '%s/rate_e' % tacodev,
                       type = 'counter',
                       mode = 'normal',
                      ),
    fastctr_f = device('devices.taco.detector.FRMCounterChannel',
                       description = "Channel F of Comtep P7888 Fast Counter",
                       tacodevice = '%s/rate_f' % tacodev,
                       type = 'counter',
                       mode = 'normal',
                      ),
    fastctr_g = device('devices.taco.detector.FRMCounterChannel',
                       description = "Channel G of Comtep P7888 Fast Counter",
                       tacodevice = '%s/rate_g' % tacodev,
                       type = 'counter',
                       mode = 'normal',
                      ),
    fastctr_h = device('devices.taco.detector.FRMCounterChannel',
                       description = "Channel H of Comtep P7888 Fast Counter",
                       tacodevice = '%s/rate_h' % tacodev,
                       type = 'counter',
                       mode = 'normal',
                      ),
    # the following may not work as expected ! (or at all!)
    #~ comtec    = device('devices.vendor.qmesydaq.QMesyDAQImage',
                       #~ description = 'Comtep P7888 Fast Counter Main detector device',
                       #~ tacodevice = '%s/detector' % tacodev,
                       #~ events = None,
                       #~ timer = None,
                       #~ counters = ['fastctr_a','fastctr_b','fastctr_c','fastctr_d',
                                   #~ 'fastctr_e','fastctr_f','fastctr_g','fastctr_h'],
                       #~ monitors = None,
                       #~ fileformats = ['RawFileSaver'],
                       #~ subdir = 'fast',
                      #~ ),
)

startupcode = """
# SetDetectors(comtec)
"""
