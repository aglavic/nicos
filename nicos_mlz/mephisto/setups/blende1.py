description = 'sample table devices'

includes = ['system']

nethost = '//mephistosrv.mephisto.frm2/'

devices = dict(
    edge1 = device('nicos.devices.taco.Motor',
        description = 'top edge',
        tacodevice = nethost + 'mephisto/aperture1/motor1',
        fmtstr = '%7.3f',
        abslimits = (-100, 100),
        lowlevel = True,
    ),
    edge2 = device('nicos.devices.taco.Motor',
        description = 'bottom edge',
        tacodevice = nethost + 'mephisto/aperture1/motor2',
        fmtstr = '%7.3f',
        abslimits = (-100, 100),
        lowlevel = True,
    ),
    edge3 = device('nicos.devices.taco.Motor',
        tacodevice = nethost + 'mephisto/aperture1/motor3',
        fmtstr = '%7.3f',
        abslimits = (-100, 100),
        lowlevel = True,
    ),
    edge4 = device('nicos.devices.taco.Motor',
        tacodevice = nethost + 'mephisto/aperture1/motor4',
        fmtstr = '%7.3f',
        abslimits = (-100, 100),
        lowlevel = True,
    ),
    e1 = device('nicos.devices.generic.Axis',
        motor = 'edge1',
        coder = 'edge1',
        obs = None,
        precision = 0.1,
        lowlevel = True,
    ),
    e2 = device('nicos.devices.generic.Axis',
        motor = 'edge2',
        coder = 'edge2',
        obs = None,
        precision = 0.1,
        lowlevel = True,
    ),
    e3 = device('nicos.devices.generic.Axis',
        motor = 'edge3',
        coder = 'edge3',
        obs = None,
        precision = 0.1,
        lowlevel = True,
    ),
    e4 = device('nicos.devices.generic.Axis',
        motor = 'edge4',
        coder = 'edge4',
        obs = None,
        precision = 0.1,
        lowlevel = True,
    ),
    b1 = device('nicos.devices.generic.Slit',
        description = 'first slit',
        top = 'e1',
        bottom = 'e2',
        right = 'e3',
        left = 'e4',
    ),
)
