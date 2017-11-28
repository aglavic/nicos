description = 'Neutron guide focussing devices'

group = 'lowlevel'

tango_base = 'tango://kompasshw.kompass.frm2:10000/kompass/'

devices = dict(
    lguide_m = device('nicos.devices.tango.Motor',
                      description = 'Long table motor',
                      tangodevice = tango_base + 'ltable/motor',
                      abslimits = (-0.5, 209.5),
                      fmtstr = '%.2f',
                      lowlevel = True,
                     ),
    lguide_c = device('nicos.devices.tango.Sensor',
                      description = 'Long table coder',
                      tangodevice = tango_base + 'ltable/coder',
                      fmtstr = '%.2f',
                      lowlevel = True,
                     ),
    lguide = device('nicos.devices.generic.Axis',
                    description = 'Long table position',
                    motor = 'lguide_m',
                    coder = 'lguide_c',
                    fmtstr = '%.2f',
                    precision = 0.01,
                   ),
    sguide_m = device('nicos.devices.tango.Motor',
                      description = 'Short table motor',
                      tangodevice = tango_base + 'stable/motor',
                      abslimits = (-0.5, 206.5),
                      fmtstr = '%.2f',
                      lowlevel = True,
                     ),
    sguide_c = device('nicos.devices.tango.Sensor',
                      description = 'Short table coder',
                      tangodevice = tango_base + 'stable/coder',
                      fmtstr = '%.2f',
                      lowlevel = True,
                     ),
    sguide = device('nicos.devices.generic.Axis',
                    description = 'Short table position',
                    motor = 'sguide_m',
                    coder = 'sguide_c',
                    fmtstr = '%.2f',
                    precision = 0.02,
                   ),
    guide = device('nicos.devices.generic.MultiSwitcher',
                   description = 'Neutron guide selector',
                   moveables = ['sguide', 'lguide'],
                   mapping = {'straight': [205.037, 208.8216],
                              'focussing': [0., 0.],
                              },
                   fallback = 'undefined',
                   fmtstr = '%s',
                   precision = [0.05, 0.05],
                   blockingmove = False,
                   lowlevel = False,
                   unit = '',
                  ),
)
