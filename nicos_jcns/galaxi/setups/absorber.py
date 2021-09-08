# -*- coding: utf-8 -*-

description = 'GALAXI absorber plates'

group = 'optional'

tango_base = 'tango://phys.galaxi.kfa-juelich.de:10000/galaxi/'
tango_digital = tango_base + 'fzjdp_digital/'

devices = dict(
    absorber00 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 0',
        tangodevice = tango_digital + 'AbsorberPlate1',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber01 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 1',
        tangodevice = tango_digital + 'AbsorberPlate2',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber02 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 2',
        tangodevice = tango_digital + 'AbsorberPlate3',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber03 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 3',
        tangodevice = tango_digital + 'AbsorberPlate4',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber04 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 4',
        tangodevice = tango_digital + 'AbsorberPlate5',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber05 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 5',
        tangodevice = tango_digital + 'AbsorberPlate6',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber06 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 6',
        tangodevice = tango_digital + 'AbsorberPlate7',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber07 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 7',
        tangodevice = tango_digital + 'AbsorberPlate8',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber08 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 8',
        tangodevice = tango_digital + 'AbsorberPlate9',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber09 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 9',
        tangodevice = tango_digital + 'AbsorberPlate10',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber10 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 10',
        tangodevice = tango_digital + 'AbsorberPlate11',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber11 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 11',
        tangodevice = tango_digital + 'AbsorberPlate12',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber12 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 12',
        tangodevice = tango_digital + 'AbsorberPlate13',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber13 = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Absorberplate 13',
        tangodevice = tango_digital + 'AbsorberPlate14',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber14 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Absorberplate 14',
        tangodevice = tango_digital + 'AbsorberPlate15',
        mapping = {
            'in': 1,
            'out': 0
        },
    ),
    absorber = device('nicos_jcns.galaxi.devices.absorber.AbsorberDevice',
        description = 'Absorber attenuation',
        absorbers = [
            'absorber00', 'absorber01', 'absorber02', 'absorber03',
            'absorber04', 'absorber05', 'absorber06', 'absorber07',
            'absorber08', 'absorber09', 'absorber10', 'absorber11',
            'absorber12', 'absorber13'
        ],
        unit = '',
        abslimits = (1., float('Inf')),
    ),
)
