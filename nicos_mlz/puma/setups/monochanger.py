#  -*- coding: utf-8 -*-

description = 'Monochanger'

group = 'optional'

includes = ['system', 'motorbus1', 'motorbus4', 'motorbus7', 'motorbus9',
            'monochromator', 'tas']

monostates = ['GE311', 'PG002', 'CU220', 'CU111', 'None']
monodevices = ['mono_ge311', 'mono_pg002', 'mono_cu220', 'mono_cu111',
               'mono_dummy']
magazinepos = [(315.4, 8), (45.46, 1), (135.4, 2), (225.4, 4)]


devices = dict(
    st_lift = device('nicos.devices.vendor.ipc.Motor',
        description = 'Motor of the monochromator lift',
        bus = 'motorbus4',
        addr = 51,
        slope = -160,
        unit = 'mm',
        abslimits = (-144, 370),
        zerosteps = 500000,
        visibility = (),
        confbyte = 52,
    ),
    co_lift = device('nicos_mlz.puma.devices.ipc.Coder',
        description = 'Potentiometer coder of the monochromator' \
        ' lift',
        bus = 'motorbus1',
        addr = 162,
        # slope = -7.466319,
        # zerosteps = 2935.18,
        poly = [409.105, -0.144828, 1.3677e-6, 7.105e-11],
        unit = 'mm',
        visibility = (),
        readings = 10,
    ),
    mli = device('nicos.devices.generic.Axis',
        description = 'Axis for the monochromater changer lift',
        motor = 'st_lift',
        # coder = 'co_lift',
        obs = ['co_lift'],
        dragerror = 20,
        obsreadings = 1,
        precision = 0.2,
        offset = 0,
        maxtries = 3,
        loopdelay = 1,
    ),
    sw_lift = device('nicos.devices.vendor.ipc.IPCSwitches',
        description = 'Switches of the lift axis card',
        bus = 'motorbus4',
        addr = 51,
        fmtstr = '%d',
        visibility = (),
    ),
    lift = device('nicos_mlz.puma.devices.SenseSwitch',
        description = 'Monochromator lift',
        moveables = 'mli',
        readables = 'sw_lift',
        # distance between upper and lower limit switch is 498.2 !!
        mapping = dict(
            top2   = (357.5, 1), #before 359.6
            top1 = (355.3, 0), # 355.3
            ref = (0, 4),
            bottom = (-138.04, 2),
        ),
        precision = [0.5, 0],
        blockingmove = True,
        fallback ='<unknown>',
        timeout = 300,
    ),

    # Magazine
    st_mag = device('nicos.devices.vendor.ipc.Motor',
        bus = 'motorbus7',
        addr = 76,
        slope = 200,
        unit = 'deg',
        abslimits = (20, 340),
        zerosteps = 500000,
        visibility = (),
        confbyte = 44,
    ),
    # co_mag = device('nicos.devices.vendor.ipc.Coder',
    #     bus = 'motorbus1',
    #     addr = 123,
    #     slope = 181.97,
    #     zerosteps = 2681.64,
    #     unit = 'deg',
    #     visibility = (),
    # ),
    mag = device('nicos.devices.generic.Axis',
        description = 'monochromator magazine moving axis',
        motor = 'st_mag',
        precision = 0.05,
        offset = 0,
        maxtries = 10,
        dragerror = 90,
        loopdelay = 2,
    ),
    io_mag = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 106,
        first = 3,
        last = 6,
        unit = '',
        visibility = (),
    ),
    magazine = device('nicos_mlz.puma.devices.SenseSwitch',
        description = 'Monochromator magazine',
        moveables = 'mag',
        readables = 'io_mag',
        mapping = dict(zip(monostates[:4], magazinepos)),
        precision = [0.2, 0],
        unit = '',
        blockingmove = True,
        fallback ='<unknown>',
        timeout = 300,
    ),

    # Magnetic Lock
    mlock_op = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 101,
        first = 0,
        last = 3,
        unit = '',
        visibility = (),
    ),
    mlock_cl = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 101,
        first = 5,
        last = 8,
        unit = '',
        visibility = (),
    ),
    mlock_set = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus9',
        addr = 110,
        first = 0,
        last = 3,
        unit = '',
        visibility = (),
    ),
    mlock = device('nicos_mlz.puma.devices.MagLock',
        description = 'Magnetic lock at magazine',
        states = monostates[:4],
        magazine = 'magazine',
        io_open = 'mlock_op',
        io_closed = 'mlock_cl',
        io_set = 'mlock_set',
        unit = '',
    ),

    # Greifer (grip)
    gr_stat = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 101,
        first = 14,
        last = 15,
        unit = '',
        visibility = (),
    ),
    gr_set = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus9',
        addr = 110,
        first = 5,
        last = 5,
        unit = '',
        visibility = (),
    ),
    grip = device('nicos_mlz.puma.devices.SenseSwitch',
        description = 'monochromator grip',
        moveables = 'gr_set',
        readables = 'gr_stat',
        mapping = dict(open=(1, 2), closed=(0, 1)),
        precision = None,  # literal compare!
        blockingmove = True,
        unit = '',
        timeout = 13,
        fallback ='<unknown>',
    ),

    # 3R coupling
    r3_set = device('nicos.devices.vendor.ipc.Output',
        bus = 'motorbus9',
        addr = 110,
        first = 4,
        last = 4,
        unit = '',
        visibility = (),
    ),
    r3 =  device('nicos.devices.generic.Switcher',
        description = 'R3 coupling holding monochromators',
        moveable = 'r3_set',
        mapping = dict(closed=0, open=1),
        precision = 0.0,
        blockingmove = True,
        unit = '',
    ),

    # holdstat
    holdstat_io = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 101,
        first = 9,
        last = 12,
        unit = '',
        visibility = (),
    ),
    holdstat = device('nicos.devices.generic.ReadonlySwitcher',
        description = 'What is in the holder position',
        # monostates has five elements ! (last one is for 'none')
        mapping = dict(zip(monostates, [14, 13, 11, 7, 15])),
        readable = 'holdstat_io',
    ),
    monostat_io = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 106,
        first = 0,
        last = 2,
        unit = '',
        visibility = (),
    ),
    mono_stat = device('nicos.devices.generic.ReadonlySwitcher',
        description = 'What is at the monotable',
        # monostates has five elements ! (last one is for 'none').
        # Unfortunately, Dummy (like 'none') returns 0
        mapping = dict(zip(monostates, [4, 5, 2, 3, 0])),
        readable = 'monostat_io',
    ),

    # Mchanger
    mchanger = device('nicos_mlz.puma.devices.Mchanger',
        description = 'The actual monochromator changer',
        monochromator = 'mono',
        mapping = dict(zip(monostates, monodevices)),
        magazine = 'magazine',
        r3 = 'r3',
        lift = 'lift',
        grip = 'grip',
        mlock = 'mlock',
        holdstat = 'holdstat',
        mono_stat = 'mono_stat',
        focush = 'mfhpg',
        focusv = 'mfvpg',
        changing_positions = dict(
            # taking into account mth offset 90.0, /2017.07.27
            mth = 90.222,
            mtt = -36.5027,
            # nominal position is 16.14, but w/o coder we use a slightly
            # different value.
            mty = 18.14,
            mgx = 0,
            mgy = 0,
        ),
        init_positions = dict(
            mty = 70,
            mgx = 0,
            mgy = 0.1,
        ),
        unit = '',
    ),
    mono_dummy = device('nicos.devices.tas.Monochromator',
        description = 'Dummy monochromator, DONT USE FOR EXPERIMENTS!',
        order = 1,
        unit = 'A-1',
        theta = 'mth',
        twotheta = 'mtt',
        reltheta = True,
        focush = None,
        focusv = None,
        hfocuspars = [1],
        vfocuspars = [1],
        abslimits = (1, 60),
        dvalue = 3.1415,
        scatteringsense = -1,
        crystalside = -1,
        fixed = 'Dummy monochromator, DONT USE FOR EXPERIMENTS!',
        fixedby = ('brain', 30),
    ),
)
