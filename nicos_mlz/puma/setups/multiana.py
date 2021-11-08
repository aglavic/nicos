#  -*- coding: utf-8 -*-

description = 'Multianalyzer motors'

motorbus = 'motorbus13'

includes = ['system', motorbus]

modules = ['nicos_mlz.puma.commands']

group = 'lowlevel'

tr_speed = 15
tr_accel = 30
tr_microstep = 1
tr_slope = -516 * tr_microstep
tr_refswitch = 'low'
tr_refdirection = 'upper'
tr_refstep = 150
tr_refmove = 25
tr_zerosteps = 500000
tr_parkpos = None

ro_microstep = 4
ro_speed = 42
ro_accel = 30
ro_slope = -118 * ro_microstep  # -1797
ro_refstep = 0
ro_refmove = 25
ro_refswitch = 'low'
ro_refdirection = 'upper'
ro_parkpos = None

level = False

devices = dict(
    # Translations
    st_ta1 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 180,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 125.0# 16491, # 7.021
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta2 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 181,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16493, # 7.022
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta3 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 182,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16495, # 7.023
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta4 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 183,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16501, # 7.0257
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta5 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 184,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16495, # 7.023
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta6 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 185,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16470, # 7.0107
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta7 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 186,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16495, # 7.023
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta8 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 187,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16488, # 7.0194
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta9 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 188,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16498, # 7.024
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta10 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 189,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        refpos = 435500, # 16496, # 7.0234
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    st_ta11 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 190,
        slope = tr_slope,
        unit = 'mm',
        abslimits = (-124, 125),
        zerosteps = tr_zerosteps,
        lowlevel = True,
        refpos = 435500, # 16494, # 7.0223
        refswitch = tr_refswitch,
        refdirection = tr_refdirection,
        refstep = tr_refstep,
        parkpos = tr_parkpos,
        refmove = tr_refmove,
        microstep = tr_microstep,
        speed = tr_speed,
        accel = tr_accel,
    ),
    co_ta1 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 204,
        slope = -14.68,
        zerosteps = 2168.6,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta2 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 205,
        slope = -14.73,
        zerosteps = 206.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta3 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 206,
        slope = -14.70,
        zerosteps = 219.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta4 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 207,
        slope = -14.68,
        zerosteps = 199.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta5 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 208,
        slope = -14.70,
        zerosteps = 198.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta6 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 209,
        slope = -14.75,
        zerosteps = 211.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta7 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 210,
        slope = -14.66,
        zerosteps = 193.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta8 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 211,
        slope = -14.75,
        zerosteps = 226.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta9 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 212,
        slope = -14.65,
        zerosteps = 132.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta10 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 213,
        slope = -14.70,
        zerosteps = 256.24,
        unit = 'mm',
        lowlevel = True,
    ),
    co_ta11 = device('nicos.devices.vendor.ipc.Coder',
        bus = motorbus,
        addr = 214,
        slope = -14.76,
        zerosteps = 213.24,
        unit = 'mm',
        lowlevel = True,
    ),
    ta1 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 1 translation',
        motor = 'st_ta1',
        # obs = ['co_ta1'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta2 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 2 translation',
        motor = 'st_ta2',
        # obs = ['co_ta2'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta3 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 3 translation',
        motor = 'st_ta3',
        # obs = ['co_ta3'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta4 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 4 translation',
        motor = 'st_ta4',
        # obs = ['co_ta4'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta5 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 5 translation',
        motor = 'st_ta5',
        # obs = ['co_ta5'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta6 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 6 translation',
        motor = 'st_ta6',
        # obs = ['co_ta6'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta7 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 7 translation',
        motor = 'st_ta7',
        # obs = ['co_ta7'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta8 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 8 translation',
        motor = 'st_ta8',
        # obs = ['co_ta8'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta9 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 9 translation',
        motor = 'st_ta9',
        # obs = ['co_ta9'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta10 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 10 translation',
        motor = 'st_ta10',
        # obs = ['co_ta10'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    ta11 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 11 translation',
        motor = 'st_ta11',
        # obs = ['co_ta11'],
        precision = 0.1,
        offset = 5,
        maxtries = 3,
        lowlevel = level,
    ),
    # Rotations
    st_ra1 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 192,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 1.0),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9634,  # 8537, # 0.814, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra2 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 193,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 0.5),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9884,  # 9560, # 0.245, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra3 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 194,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 1.7),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9254, # 7161, # 1.58, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra4 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 195,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 1.0),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9646,  # 9686, # 0.175, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra5 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 196,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 0.5),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9943,  # 9784, # 0.12, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra6 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 197,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 0.5),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9828,  # 9344, # 0.365, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra7 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 198,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 1.0),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9577, # 8392, # 0.895, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra8 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 199,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 0.5),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9936, # 9757, # 0.135, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra9 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 200,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 0.5),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9988, # 9955, # 0.025, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra10 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 201,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 0.5),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9783,  # 9173, # 0.46, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        parkpos = ro_parkpos,
    ),
    st_ra11 = device('nicos_mlz.puma.devices.ipc.ReferenceMotor',
        bus = motorbus,
        addr = 202,
        slope = ro_slope,
        unit = 'deg',
        abslimits = (-60.0, 0.5),
        zerosteps = 10000,
        lowlevel = True,
        refswitch = ro_refswitch,
        refdirection = ro_refdirection,
        refpos = 9917,  # 9686, # 0.175, 10000, 0
        refspeed = ro_speed,
        microstep = ro_microstep,
        speed = ro_speed,
        accel = ro_accel,
        refstep = ro_refstep,
        refmove = ro_refmove,
        parkpos = ro_parkpos,
    ),
    ra1 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 1 rotation',
        motor = 'st_ra1',
        precision = 0.01,
        offset = 0, # -0.814,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra2 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 2 rotation',
        motor = 'st_ra2',
        precision = 0.01,
        offset = 0, # -0.245,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra3 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 3 rotation',
        motor = 'st_ra3',
        precision = 0.01,
        offset = 0, # -1.58,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra4 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 4 rotation',
        motor = 'st_ra4',
        precision = 0.01,
        offset = 0, # -0.175,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra5 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 5 rotation',
        motor = 'st_ra5',
        precision = 0.01,
        offset = 0, # -0.12,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra6 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 6 rotation',
        motor = 'st_ra6',
        precision = 0.01,
        offset = 0, # -0.365,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra7 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 7 rotation',
        motor = 'st_ra7',
        precision = 0.01,
        offset = 0, # -0.895,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra8 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 8 rotation',
        motor = 'st_ra8',
        precision = 0.01,
        offset = 0, # -0.135,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra9 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 9 rotation',
        motor = 'st_ra9',
        precision = 0.01,
        offset = 0, # -0.025,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra10 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 10 rotation',
        motor = 'st_ra10',
        precision = 0.01,
        offset = 0, # -0.46,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    ra11 = device('nicos.devices.generic.Axis',
        description = 'Multianalyzer crystal 11 rotation',
        motor = 'st_ra11',
        precision = 0.01,
        offset = 0, # -0.175,
        maxtries = 3,
        lowlevel = level,
        backlash = -1,
    ),
    man = device('nicos_mlz.puma.devices.PumaMultiAnalyzer',
        description = 'PUMA multi analyzer',
        translations = ['ta1', 'ta2', 'ta3', 'ta4', 'ta5', 'ta6', 'ta7', 'ta8',
                        'ta9', 'ta10', 'ta11'],
        rotations = ['ra1', 'ra2', 'ra3', 'ra4', 'ra5', 'ra6', 'ra7', 'ra8',
                     'ra9', 'ra10', 'ra11'],
    ),
)
