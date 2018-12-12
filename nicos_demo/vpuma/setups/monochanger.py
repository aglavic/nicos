#  -*- coding: utf-8 -*-

description = 'Monochanger'

group = 'optional'

includes = ['system', 'monochromator']

monostates = ['GE311', 'PG002', 'CU220', 'CU111', 'None']
monodevices = ['mono_ge311', 'mono_pg002', 'mono_cu220', 'mono_cu111',
               'mono_dummy']
magazinpos = [(315.4, 8), (45.46, 1), (135.4, 2), (225.4, 4)]

devices = dict(
    st_lift = device('nicos_mlz.puma.devices.virtual.VirtualReferenceMotor',
        description = 'Motor of the monochromator lift',
        unit = 'mm',
        abslimits = (-145, 360),
        lowlevel = True,
        speed = 0.1,
    ),
    co_lift = device('nicos.devices.generic.VirtualCoder',
        description = 'Potentiometer coder of the monochromator lift',
        motor = 'st_lift',
        unit = 'mm',
        lowlevel = True,
        # readings = 50,
        # jitter = 0.2,
    ),
    mli = device('nicos.devices.generic.Axis',
        description = 'Axis for the monochromater changer lift',
        motor = 'st_lift',
        coder = 'co_lift',
        obs = ['co_lift'],
        dragerror = 20,
        obsreadings = 100,
        precision = 0.15,
        offset = 0,
        maxtries = 10,
        loopdelay = 1,
    ),
    sw_lift = device('nicos.devices.generic.ReadonlySwitcher',
        description = 'Switches of the lift axis card',
        readable = 'st_lift',
        fmtstr = '%d',
        lowlevel = True,
        mapping = {
            1: -142.2,
            2: 358.1,
            4: 0,
        },
        fallback = 0,
    ),
    lift = device('nicos_mlz.puma.devices.senseswitch.SenseSwitch',
        description = 'Monochromator lift',
        moveables = 'mli',
        readables = 'sw_lift',
        mapping = dict(
            top2   = (358.1, 1),
            top1 = (355.3, 0),
            ref = (0, 4),
            bottom = (-142.5, 2),
        ),
        precision = [0.5, 0],
        blockingmove = True,
        fallback ='<unknown>',
        timeout = 300,
    ),
    # Magazin
    st_mag = device('nicos.devices.generic.VirtualMotor',
        unit = 'deg',
        abslimits = (20, 340),
        lowlevel = True,
    ),
    mag = device('nicos.devices.generic.Axis',
        description = 'monochromator magazin moving axis',
        motor = 'st_mag',
        obs = [],
        precision = 0.05,
        offset = 0,
        maxtries = 10,
        dragerror = 90,
        loopdelay = 2,
        lowlevel = False,
    ),
    io_mag = device('nicos.devices.generic.ReadonlySwitcher',
        readable = 'mag',
        mapping = {
            1: 45.46,
            2: 135.4,
            4: 225.4,
            8: 315.4,
        },
        fallback = 0,
        unit = '',
        lowlevel = True,
    ),
    magazin = device('nicos_mlz.puma.devices.senseswitch.SenseSwitch',
        description = 'Monochromator magazine',
        moveables = 'mag',
        readables = 'io_mag',
        mapping = dict(zip(monostates[:4], magazinpos)),
        precision = [0.2, 0],
        unit = '',
        blockingmove = True,
        fallback ='<unknown>',
        timeout = 300,
    ),
    # Magnetic Lock
    mlock_op = device('nicos_mlz.puma.devices.virtual.LogoFeedBack',
        input = 'mlock_set',
        unit = '',
        lowlevel = True,
    ),
    mlock_cl = device('nicos_mlz.puma.devices.virtual.LogoFeedBack',
        input = 'mlock_set',
        unit = '',
        lowlevel = True,
    ),
    mlock_set = device('nicos_mlz.puma.devices.virtual.DigitalOutput',
        unit = '',
        lowlevel = True,
    ),
    mlock = device('nicos_mlz.puma.devices.maglock.MagLock',
        description = 'Magnetic lock at magazin',
        states = monostates[:4],
        magazin = 'magazin',
        io_open = 'mlock_op',
        io_closed = 'mlock_cl',
        io_set = 'mlock_set',
        unit = '',
    ),
    # Greifer (grip)
    gr_stat = device('nicos_mlz.puma.devices.virtual.LogoFeedBack',
        input = 'gr_set',
        unit = '',
        lowlevel = True,
    ),
    gr_set = device('nicos_mlz.puma.devices.virtual.DigitalOutput',
        unit = '',
        lowlevel = True,
    ),
    grip = device('nicos_mlz.puma.devices.senseswitch.SenseSwitch',
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
    r3 =  device('nicos.devices.generic.ManualSwitch',
        description = 'R3 coupling holding monochromators',
        states = ['closed', 'open'],
        unit = '',
    ),
    # holdstat
    holdstat_io = device('nicos.devices.vendor.ipc.Input',
        bus = 'motorbus9',
        addr = 101,
        first = 9,
        last = 12,
        unit = '',
        lowlevel = True,
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
        lowlevel = True,
    ),
    mono_stat = device('nicos.devices.generic.ReadonlySwitcher',
        description = 'What is at the monotable',
        # monostates has five elements ! (last one is for 'none').
        # Unfortunately, Dummy (like 'none') returns 0
        mapping = dict(zip(monostates, [4, 5, 2, 3, 0])),
        readable = 'monostat_io',
    ),
    # Mchanger
    mchanger = device('nicos_mlz.puma.devices.mchanger.Mchanger',
        description = 'The actual monochromator changer',
        monochromator = 'mono',
        mapping = dict(zip(monostates, monodevices)),
        magazin = 'magazin',
        r3 = 'r3',
        lift = 'lift',
        grip = 'grip',
        mlock = 'mlock',
        holdstat = 'holdstat',
        mono_stat = 'mono_stat',
        # foch = 'mfhpg',
        # focv = 'mfvpg',
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
