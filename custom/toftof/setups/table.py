description = 'sample table and radial collimator'

group = 'basic'

includes = ['system']

nethost= 'toftofsrv.toftof.frm2'

devices = dict(
    gx    = device('devices.taco.motor.Motor',
                   tacodevice = '//%s/toftof/huber/gxm' % (nethost,),
                   fmtstr = "%7.3f",
                   abslimits = (-20.0, 20.),
                  ),
    gy    = device('devices.taco.motor.Motor',
                   tacodevice = '//%s/toftof/huber/gym' % (nethost,),
                   fmtstr = "%7.3f",
                   abslimits = (-20.0, 20.),
                  ),
    gz    = device('devices.taco.motor.Motor',
                   tacodevice = '//%s/toftof/huber/gzm' % (nethost,),
                   fmtstr = "%7.3f",
                   abslimits = (-14.8, 50.),
                  ),
    gcx   = device('devices.taco.motor.Motor',
                   tacodevice = '//%s/toftof/huber/gcxm' % (nethost,),
                   fmtstr = "%7.3f",
                   abslimits = (-20.0, 20.),
                  ),
    gcy   = device('devices.taco.motor.Motor',
                   tacodevice = '//%s/toftof/huber/gcym' % (nethost,),
                   fmtstr = "%7.3f",
                   abslimits = (-20.0, 20.),
                  ),
    gphi  = device('devices.taco.motor.Motor',
                   tacodevice = '//%s/toftof/huber/gphim' % (nethost,),
                   fmtstr = "%7.3f",
                   abslimits = (-20.0, 150.),
                  ),

    rcbus = device('toftof.rc.ModBusDriverHP',
                   tacodevice = '//%s/toftof/rs232/ifhubermot1' % (nethost,),
                   maxtries = 5,
                   lowlevel = True,
                  ),
    rc    = device('toftof.rc.RadialCollimator',
                   bus = 'rcbus',
                   address = 13,
                   start_angle = 1.0,
                   stop_angle = 5.4,
                   std_speed = 120,
                   ref_speed = 100,
                   timeout = 120,
#		   pollinterval = 5,
                   unit = 'deg',
                   fmtstr = '%.3f',
                  ),
)
