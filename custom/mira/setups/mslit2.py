description = 'IPC slit after mono2 shielding'
group = 'optional'

devices = dict(
    ms2bus    = device('nicos.ipc.IPCModBusTCP',
                       host = 'mirars8.mira.frm2',
                       port = 4004,
                       lowlevel = True),

    ms2_l_mot = device('nicos.ipc.SlitMotor',
                       lowlevel = True,
                       bus = 'ms2bus',
                       addr = 0x88,
                       side = 2,
                       slope = -80,
                       zerosteps = 1170,
                       resetpos = -20,
                       abslimits = (-32, 13)),
    ms2_r_mot = device('nicos.ipc.SlitMotor',
                       lowlevel = True,
                       bus = 'ms2bus',
                       addr = 0x88,
                       side = 3,
                       slope = 80.,
                       zerosteps = 1800,
                       resetpos = 20,
                       abslimits = (-13, 32)),
    ms2_b_mot = device('nicos.ipc.SlitMotor',
                       lowlevel = True,
                       bus = 'ms2bus',
                       addr = 0x88,
                       side = 0,
                       slope = -40.,
                       zerosteps = 720,
                       resetpos = -45,
                       abslimits = (-70, 17)),
    ms2_t_mot = device('nicos.ipc.SlitMotor',
                       lowlevel = True,
                       bus = 'ms2bus',
                       addr = 0x88,
                       side = 1,
                       slope = 40.,
                       zerosteps = 790,
                       resetpos = 45,
                       abslimits = (-19, 70)),

    ms2_l     = device('nicos.generic.Axis',
                       lowlevel = True,
                       precision = 0.1,
                       backlash = -2.,
                       motor = 'ms2_l_mot',
                       coder = 'ms2_l_mot',
                       obs = None),
    ms2_r     = device('nicos.generic.Axis',
                       lowlevel = True,
                       precision = 0.1,
                       backlash = 2.,
                       motor = 'ms2_r_mot',
                       coder = 'ms2_r_mot',
                       obs = None),
    ms2_b     = device('nicos.generic.Axis',
                       lowlevel = True,
                       precision = 0.1,
                       backlash = -2.,
                       motor = 'ms2_b_mot',
                       coder = 'ms2_b_mot',
                       obs = None),
    ms2_t     = device('nicos.generic.Axis',
                       lowlevel = True,
                       precision = 0.1,
                       backlash = 2.,
                       motor = 'ms2_t_mot',
                       coder = 'ms2_t_mot',
                       obs = None),

    ms2       = device('nicos.generic.Slit',
                       description = 'slit after monochromator Mira2',
                       left = 'ms2_l',
                       right = 'ms2_r',
                       bottom = 'ms2_b',
                       top = 'ms2_t',
                       opmode = 'offcentered',
                       pollinterval = 5,
                       maxage = 10),
)
