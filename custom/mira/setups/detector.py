description = 'standard detector and counter card'
group = 'lowlevel'

includes = ['base']

tango_base = 'tango://mira1.mira.frm2:10000/mira/'

devices = dict(
    timer    = device('devices.tango.TimerChannel',
                      tangodevice = tango_base + 'frmctr/timer',
                      fmtstr = '%.2f',
                      lowlevel = True,
                     ),
    mon1     = device('devices.tango.CounterChannel',
                      tangodevice = tango_base + 'frmctr/ctr0',
                      type = 'monitor',
                      fmtstr = '%d',
                      lowlevel = True,
                     ),
    mon2     = device('devices.tango.CounterChannel',
                      tangodevice = tango_base + 'frmctr/ctr1',
                      type = 'monitor',
                      fmtstr = '%d',
                      lowlevel = True,
                     ),
    ctr1     = device('devices.tango.CounterChannel',
                      tangodevice = tango_base + 'frmctr/ctr2',
                      type = 'counter',
                      fmtstr = '%d',
                      lowlevel = True,
                     ),

    det      = device('devices.generic.Detector',
                      description = 'FRM II multichannel counter card',
                      timers = ['timer'],
                      monitors = ['mon1', 'mon2'],
                      counters = ['ctr1'],
                      fmtstr = 'timer %s, mon1 %s, mon2 %s, ctr1 %s',
                      maxage = 2,
                      pollinterval = 0.5,
                     ),

    det_fore = device('devices.generic.DetectorForecast',
                      description = 'forecast for det values',
                      pollinterval = 0.5,
                      maxage = 2,
                      unit = '',
                      det = 'det',
                     ),

    DetHV     = device('devices.tango.Actuator',
                       description = 'HV supply for single tube detector (usual value 850 V)',
                       tangodevice = tango_base + 'detectorhv/voltage',
                       warnlimits = (840, 860),
                       pollinterval = 10,
                       maxage = 20,
                       fmtstr = '%d',
                      ),

    MonHV     = device('devices.tango.Actuator',
                       description = 'HV supply for monitor counter (usual value 500 V)',
                       tangodevice = tango_base + 'monitorhv/voltage',
                       warnlimits = (490, 510),
                       pollinterval = 10,
                       maxage = 30,
                       fmtstr = '%d',
                      ),
)
