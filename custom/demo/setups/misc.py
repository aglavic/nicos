description = 'miscellaneous devices'
group = 'optional'

includes = ['system']

devices = dict(
    m1       = device('devices.generic.VirtualMotor',
                      lowlevel = True,
                      #loglevel = 'debug',
                      abslimits = (-100, 100),
                      speed = 0.5,
                      unit = 'deg',
                     ),

    m2       = device('devices.generic.VirtualMotor',
                      lowlevel = True,
                      loglevel = 'debug',
                      abslimits = (-100, 100),
                      speed = 1,
                      unit = 'deg',
                     ),

    c1       = device('devices.generic.VirtualCoder',
                      lowlevel = True,
                      motor = 'm1',
                      unit = 'deg',
                     ),

    a1       = device('devices.generic.Axis',
                      description = 'demo axis',
                      motor = 'm1',
                      coder = 'c1',
                      obs = ['c1'],
                      abslimits = (0, 100),
                      userlimits = (0, 50),
                      precision = 0,
                      pollinterval = 0.5,
                     ),

    a2       = device('devices.generic.Axis',
                      description = 'demo axis #2',
                      motor = 'm2',
                      coder = 'm2',
                      obs = [],
                      precision = 0,
                      abslimits = (0, 100),
                     ),

    a3       = device('devices.generic.Axis',
                      description = 'demo axis #3',
                      motor = device('devices.generic.VirtualMotor',
                          abslimits = (-100, 100),
                          speed = 1,
                          unit = 'deg',
                         ),
                      precision = 0,
                     ),

    sw       = device('devices.generic.Switcher',
                      description = 'demo switcher',
                      moveable = 'a2',
                      mapping = {'in': 1, 'out': 0},
                      precision = 0,
                     ),

    ap       = device('devices.generic.DeviceAlias',
                      alias = 'a1',
                      devclass = 'nicos.core.Moveable',
                     ),

    a1speed  = device('devices.generic.ParamDevice',
                      description = 'sets the speed of a1 on move()',
                      device = 'a1',
                      parameter = 'speed',
                     ),

    sxl      = device('devices.generic.VirtualMotor',
                      description = 'left slit motor',
                      abslimits = (-20, 40),
                      unit = 'mm',
                     ),
    sxr      = device('devices.generic.VirtualMotor',
                      description = 'right slit motor',
                      abslimits = (-40, 20),
                      unit = 'mm',
                     ),
    sxb      = device('devices.generic.VirtualMotor',
                      description = 'bottom slit motor',
                      abslimits = (-50, 30),
                      unit = 'mm',
                     ),
    sxt      = device('devices.generic.VirtualMotor',
                      description = 'top slit motor',
                      abslimits = (-30, 50),
                      unit = 'mm',
                     ),
    slit     = device('devices.generic.Slit',
                      description = '4-blade slit',
                      left = 'sxl',
                      right = 'sxr',
                      bottom = 'sxb',
                      top = 'sxt',
                     ),

    mm       = device('devices.generic.ManualMove',
                      description = 'manual move demo',
                      abslimits = (0, 100),
                      unit = 'mm',
                     ),
    msw      = device('devices.generic.ManualSwitch',
                      description = 'manual switch demo',
                      states = ['unknown', 'on', 'off'],
                      requires = {'level': 10},
                     ),

    mfh_mot  = device('panda.rot_axis.VirtualRotAxisMotor',
                      abslimits = (-360, 360),
                      unit = 'deg',
                      speed = 20,
                      jitter = 0.1,
                      lowlevel = True,
                     ),
    mfh      = device('panda.rot_axis.RotAxis',
                      description = 'horizontal focus for the monochromator',
                      abslimits = (-360, 360),
                      unit = 'deg',
                      refpos = 220,
                      refspeed = 1,
                      autoref = -10,
                      wraparound = 360,
                      precision = 0.1,
                      motor = 'mfh_mot',
                      coder = 'mfh_mot',
                      obs = [],
                     ),

    ld       = device('devices.generic.LockedDevice',
                      description = 'demo locked device',
                      device = 'a1',
                      lock = 'a2',
                      lockvalue = 10,
                      unlockvalue = 20,
                      loglevel = 'debug',
                     ),

)
