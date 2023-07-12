description = 'GALAXI absorber plates setup'
group = 'optional'

tango_base = 'tango://phys.galaxi.jcns.fz-juelich.de:10000/galaxi/'
s7_digital = tango_base + 'fzjdp_digital/'

devices = dict(
    absorber00 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 0 position.',
        tangodevice = s7_digital + 'AbsorberPlate1',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber01 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 1 position.',
        tangodevice = s7_digital + 'AbsorberPlate2',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber02 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 2 position.',
        tangodevice = s7_digital + 'AbsorberPlate3',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber03 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 3 position.',
        tangodevice = s7_digital + 'AbsorberPlate4',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber04 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 4 position.',
        tangodevice = s7_digital + 'AbsorberPlate5',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber05 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 5 position.',
        tangodevice = s7_digital + 'AbsorberPlate6',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber06 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 6 position.',
        tangodevice = s7_digital + 'AbsorberPlate7',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber07 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 7 position.',
        tangodevice = s7_digital + 'AbsorberPlate8',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber08 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 8 position.',
        tangodevice = s7_digital + 'AbsorberPlate9',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber09 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 9 position.',
        tangodevice = s7_digital + 'AbsorberPlate10',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber10 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 10 position.',
        tangodevice = s7_digital + 'AbsorberPlate11',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber11 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 11 position.',
        tangodevice = s7_digital + 'AbsorberPlate12',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber12 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 12 position.',
        tangodevice = s7_digital + 'AbsorberPlate13',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber13 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 13 position.',
        tangodevice = s7_digital + 'AbsorberPlate14',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber14 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Absorberplate 14 position.',
        tangodevice = s7_digital + 'AbsorberPlate15',
        mapping = {'out': 0, 'in': 1},
    ),
    absorber = device('nicos_jcns.galaxi.devices.absorber.AbsorberDevice',
        description = 'Absorber attenuation.',
        absorbers = ['absorber00', 'absorber01', 'absorber02', 'absorber03',
                     'absorber04', 'absorber05', 'absorber06', 'absorber07',
                     'absorber08', 'absorber09', 'absorber10', 'absorber11',
                     'absorber12', 'absorber13'],
        unit = '',
        abslimits = (1., float('Inf')),
    ),
)
