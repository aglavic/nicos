description = 'MIRA1 monochromator'
group = 'lowlevel'

includes = ['base']

devices = dict(
    Sample   = device('nicos.tas.TASSample'),

    MonoIPC  = device('nicos.ipc.IPCModBusTaco',
                      tacodevice = 'mira/rs485/mgott',
                      lowlevel = True),

#    MonoIPC  = device('nicos.ipc.IPCModBusSerial', port='/dev/ttyS1'),

    co_mth   = device('nicos.ipc.Coder',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 64,
                      confbyte = 153,
                      zerosteps = 14562275.0,
                      slope = 8192.0,
                      unit = 'deg'),
    mo_mth   = device('nicos.ipc.Motor',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 53,
                      confbyte = 44,
                      zerosteps = 500000,
                      slope = 400.0,
                      abslimits = (-15.0, -5.0),
                      unit = 'deg'),
    mth      = device('nicos.generic.Axis',
                      motor = 'mo_mth',
                      coder = 'co_mth',
                      obs = [],
                      fmtstr = '%.3f',
                      precision = 0.02),

    co_mtt   = device('nicos.ipc.Coder',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 69,
                      confbyte = 153,
                      zerosteps = 10919359.0,
                      slope = -294.0,
                      unit = 'deg'),
    mo_mtt   = device('nicos.ipc.Motor',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 50,
                      confbyte = 47,
                      zerosteps = 500000,
                      slope = -1437.0,
                      abslimits = (-28.0, -6.8),
                      unit = 'deg'),
    mtt      = device('nicos.generic.Axis',
                      motor = 'mo_mtt',
                      coder = 'co_mtt',
                      obs = [],
                      fmtstr = '%.3f',
                      precision = 0.05),

    co_mtx   = device('nicos.ipc.Coder',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 66,
                      confbyte = 153,
                      zerosteps = 14097352.0,
                      slope = -4096.0,
                      unit = 'mm'),
    mo_mtx   = device('nicos.ipc.Motor',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 54,
                      confbyte = 44,
                      zerosteps = 500000,
                      slope = -200.0,
                      abslimits = (-15.0, 15.0),
                      unit = 'mm'),
    mtx      = device('nicos.generic.Axis',
                      motor = 'mo_mtx',
                      coder = 'co_mtx',
                      obs = [],
                      fmtstr = '%.3f',
                      precision = 0.2),

    co_mty   = device('nicos.ipc.Coder',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 67,
                      confbyte = 153,
                      zerosteps = 20922015.0,
                      slope = -4096.0,
                      unit = 'mm'),
    mo_mty   = device('nicos.ipc.Motor',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 55,
                      confbyte = 44,
                      zerosteps = 500000,
                      slope = 200.0,
                      abslimits = (-15.0, 15.0),
                      unit = 'mm'),
    mty      = device('nicos.generic.Axis',
                      motor = 'mo_mty',
                      coder = 'co_mty',
                      obs = [],
                      fmtstr = '%.3f',
                      precision = 0.2),

    co_mgx   = device('nicos.ipc.Coder',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 68,
                      confbyte = 153,
                      zerosteps = 13451490.0,
                      slope = 8192.0,
                      unit = 'deg'),
    mo_mgx   = device('nicos.ipc.Motor',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 58,
                      confbyte = 44,
                      zerosteps = 500000,
                      slope = -400.0,
                      abslimits = (-5.0, 5.0),
                      unit = 'deg'),
    mgx      = device('nicos.generic.Axis',
                      motor = 'mo_mgx',
                      coder = 'co_mgx',
                      obs = [],
                      fmtstr = '%.3f',
                      precision = 0.02),

    co_mch   = device('nicos.ipc.Coder',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 65,
                      confbyte = 153,
                      zerosteps = 23820280.9,
                      slope = 8192.0,
                      unit = 'deg'),
    mo_mch   = device('nicos.ipc.Motor',
                      lowlevel = True,
                      bus = 'MonoIPC',
                      addr = 49,
                      confbyte = 44,
                      zerosteps = 500000,
                      slope = 400.0,
                      abslimits = (-100.0, 100.0),
                      unit = 'deg'),
    mchanger = device('nicos.generic.Axis',
                      motor = 'mo_mch',
                      coder = 'co_mch',
                      obs = [],
                      fmtstr = '%.3f',
                      precision = 0.05),

)
