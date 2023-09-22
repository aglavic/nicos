description = 'Attenuator and PGFilter'
group = 'lowlevel'

includes = ['motorbus6', 'motorbus9']

devices = dict(
    att_sw = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 104,
        first = 0,
        last = 9,
        visibility = (),
        unit = '',
    ),
    att_press = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 103,
        first = 13,
        last = 13,
        visibility = (),
        unit = '',
    ),
    att_set = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus9',
        addr = 114,
        first = 3,
        last = 7,
        visibility = (),
        unit = '',
    ),
    atn = device('nicos_mlz.puma.devices.Attenuator',
        description = 'Sample attenuator, width=0..38mm',
        io_status = 'att_sw',
        io_set = 'att_set',
        io_press = 'att_press',
        abslimits = (0, 38),
        unit = 'mm',
    ),
    fpg_sw = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus6',
        addr = 111,
        first = 12,
        last = 13,
        visibility = (),
        unit = ''
    ),
    fpg_set = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus6',
        addr = 103,
        first = 4,
        last = 4,
        visibility = (),
        unit = '',
    ),
    fpg1 = device('nicos_mlz.puma.devices.SenseSwitch',
        description = 'First PG filter',
        readables = 'fpg_sw',
        moveables = 'fpg_set',
        mapping = {
            'in': (1, 1),
            'out': (0, 0),
        },
        precision = [0, 0],
        blockingmove = True,
        timeout = 20,
    ),
    uni_sw = device('nicos.devices.vendor.ipc.IPCSwitches',
        description = 'Switches of the lift axis card',
        bus = 'motorbus6',
        addr = 70,
        fmtstr = '%d',
        visibility = (),
    ),
    uni_st = device('nicos.devices.vendor.ipc.Motor',
        description = 'Motor of the lift axis?',
        bus = 'motorbus6',
        addr = 70,
        slope = 1,
        unit = 'mm',
        abslimits = (0, 999999),
        zerosteps = 0,
        visibility = (),
    ),
    fpg2 = device('nicos_mlz.puma.devices.SenseSwitch',
        description = 'Second PG filter',
        moveables = 'uni_st',
        readables = 'uni_sw',
        mapping = {
            'in': (500000, 1),
            'out': (536400, 2),
        },
        precision = [350, 0],
        blockingmove = True,
        timeout = 300,
    ),
    tube_sw = device('nicos.devices.vendor.ipc.Input',
        description = 'limit switch status drum shielding',
        bus = 'motorbus9',
        addr = 104,
        first = 10,
        last = 11,
        visibility = (),
    ),
    tube_press = device('nicos.devices.vendor.ipc.Input',
        description = 'pressure monitor drum shielding',
        bus = 'motorbus9',
        addr = 103,
        first = 12,
        last = 12,
        visibility = (),
    ),
)
