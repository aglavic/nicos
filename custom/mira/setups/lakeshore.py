description = 'LakeShore 340 cryo controller'

devices = dict(
    T        = device('nicos.taco.TemperatureController',
                      tacodevice = 'mira/ls340/control',
                      sensor_A = 'TA',
                      sensor_B = 'TB',
                      sensor_C = 'TC',
                      sensor_D = None,
                      pollinterval = 0.7,
                      maxage = 2,
                      abslimits = (0, 300)),
    TA       = device('nicos.taco.TemperatureSensor',
                      tacodevice = 'mira/ls340/a',
                      pollinterval = 0.7,
                      maxage = 2),
    TB       = device('nicos.taco.TemperatureSensor',
                      tacodevice = 'mira/ls340/b',
                      pollinterval = 0.7,
                      maxage = 2),
    TC       = device('nicos.taco.TemperatureSensor',
                      tacodevice = 'mira/ls340/c',
                      pollinterval = 0.7,
                      maxage = 2),
    Pcryo    = device('nicos.taco.AnalogInput',
                      description = 'Cryo sample tube pressure',
                      tacodevice = 'mira/ccr/p1',
                      fmtstr = '%.3f'),
    Cryo     = device('nicos.taco.NamedDigitalOutput',
                      mapping = {0: 'off', 1: 'on'},
                      tacodevice = 'mira/ccr/pump',),
    CryoGas  = device('nicos.taco.NamedDigitalOutput',
                      mapping = {0: 'off', 1: 'on'},
                      tacodevice = 'mira/ccr/gas'),
    CryoVac  = device('nicos.taco.NamedDigitalOutput',
                      mapping = {0: 'off', 1: 'on'},
                      tacodevice = 'mira/ccr/vacuum'),
)
