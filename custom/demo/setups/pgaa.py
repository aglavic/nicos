description = 'virtual PGAA devices'
group = 'basic'

sysconfig = dict(
)

devices = dict(
    sample_motor = device('devices.generic.VirtualMotor',
                          description = 'Motor to change the sample position',
                          fmtstr = '%7.1f',
                          abslimits = (-5, 356),
                          speed = 10,
                          unit = 'mm',
                          lowlevel = False,
                         ),
    samplepos = device('devices.generic.Switcher',
                       description = 'Sample switcher',
                       moveable = 'sample_motor',
                       mapping  = {'0' : 4.00,
                                   '1' : 74.00,
                                   '2' : 144.00,
                                   '3' : 214.00,
                                   '4' : 284.00,
                                   '5' : 354.00,
                                  },
                       precision = 0.1,
                       blockingmove = False,
                       unit = '',
                      ),
    get_ready = device('devices.generic.ManualSwitch',
                       description = '',
                       lowlevel = True,
                       states = [0, 1,],
                       fmtstr = '%d',
                      ),
    set_ready = device('devices.generic.ManualSwitch',
                       description = '',
                       lowlevel = True,
                       states = [0, 1,],
                       fmtstr = '%d',
                      ),
    shutter = device('devices.generic.ManualSwitch',
                     description = 'secondary experiment shutter',
                     states = ['open', 'closed'],
                    ),
    att1 = device('devices.generic.ManualSwitch',
                  description = 'attenuator 1',
                  states = ['in', 'out',],
                 ),
    att2 = device('devices.generic.ManualSwitch',
                  description = 'attenuator 3',
                  states = ['in', 'out',],
                 ),
    att3 = device('devices.generic.ManualSwitch',
                  description = 'attenuator 3',
                  states = ['in', 'out',],
                 ),
    det = device('pgaa.dspec.DSPec',
                 description = 'DSpec detector device',
                 set_ready = 'set_ready',
                 get_ready = 'get_ready',
                ),
)

startupcode = '''
SetDetectors(det)
SetEnvironment()
printinfo("============================================================")
printinfo("Welcome to the NICOS PGAA demo setup.")
printinfo("============================================================")
'''
