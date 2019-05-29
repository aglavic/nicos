#  -*- coding: utf-8 -*-

description = 'Primary shutter'

group = 'lowlevel'

includes = ['system', 'motorbus5']

devices = dict(
    io_sw1 = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus5',
        addr = 107,
        first = 0,
        last = 2,
        visibility = (),
        unit = '',
    ),
    io_air1 = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus5',
        addr = 117,
        first = 0,
        last = 0,
        visibility = (),
        unit = '',
    ),
    io_pos1 = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus5',
        addr = 117,
        first = 3,
        last = 3,
        visibility = (),
        unit = '',
    ),
    cy1 = device('nicos_mlz.puma.devices.SH_Cylinder',
        description = 'Cylinder 1 (Er filter)',
        io_ref = 'io_sw1',
        io_air = 'io_air1',
        io_pos = 'io_pos1',
        unit = '',
    ),
    erbium = device('nicos_mlz.puma.devices.SenseSwitch',
        description = 'Erbium filter',
        moveables = 'cy1',
        readables = 'io_sw1',
        mapping = {
            'closed': (-1, 1),
            'in': (0, 4),
            'out': (1, 2),
        },
        precision = None,
        fallback = '<unknown>',
        timeout = 10,
    ),
    io_sw2 = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus5',
        addr = 107,
        first = 3,
        last = 7,
        visibility = (),
        unit = '',
    ),
    io_air2 = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus5',
        addr = 117,
        first = 1,
        last = 1,
        visibility = (),
        unit = '',
    ),
    io_pos2 = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus5',
        addr = 117,
        first = 4,
        last = 6,
        visibility = (),
        unit = '',
    ),
    cy2 = device('nicos_mlz.puma.devices.SH_Cylinder',
        description = 'Cylinder 2 (Collimators)',
        io_ref = 'io_sw2',
        io_air = 'io_air2',
        io_pos = 'io_pos2',
        unit = '',
    ),
    alpha1 = device('nicos_mlz.puma.devices.SenseSwitch',
        description = 'Primary collimator',
        moveables = 'cy2',
        readables = 'io_sw2',
        mapping = {
            'closed': (-1, 1),
            '120': (1, 2),
            '20': (0, 16),
            '40': (2, 4),
            '60': (4, 8),
        },
        precision = None,
        fallback = '<unknown>',
        timeout = 10,
    ),
    io_sw3 = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus5',
        addr = 107,
        first = 8,
        last = 10,
        visibility = (),
        unit = '',
    ),
    io_air3 = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus5',
        addr = 117,
        first = 2,
        last = 2,
        visibility = (),
        unit = '',
    ),
    io_pos3 = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus5',
        addr = 117,
        first = 7,
        last = 7,
        visibility = (),
        unit = '',
    ),
    cy3 = device('nicos_mlz.puma.devices.SH_Cylinder',
        description = 'Cylinder 1 (Sapphire filter)',
        io_ref = 'io_sw3',
        io_air = 'io_air3',
        io_pos = 'io_pos3',
        unit = '',
    ),
    sapphire = device('nicos_mlz.puma.devices.SenseSwitch',
        description = 'Sapphire filter',
        moveables = 'cy3',
        readables = 'io_sw3',
        mapping = {
            'closed': (-1, 1),
            'in': (0, 4),
            'out': (1, 2),
        },
        precision = None,
        fallback = '<unknown>',
        timeout = 10,
    ),
)
