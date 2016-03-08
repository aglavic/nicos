description = 'POLI sample table'

group = 'lowlevel'
excludes = ['table']

tango_base = 'tango://phys.poli.frm2:10000/poli/'

devices = dict(
    co_omega = device('devices.tango.Sensor',
                      lowlevel = True,
                      tangodevice = tango_base + 'table/omegaenc',
                      unit = 'deg',
                     ),
    mo_omega = device('devices.tango.Motor',
                      lowlevel = True,
                      tangodevice = tango_base + 'table/omegamot',
                      abslimits = (-180, 180),
                      unit = 'deg',
                      precision = 0.005,
                     ),
    omega    = device('devices.generic.Axis',
                      description = 'table omega axis',
                      motor = 'mo_omega',
                      coder = 'co_omega',
                      obs = [],
                      fmtstr = '%.2f',
                      precision = 0.005,
                     ),

    co_twotheta = device('devices.tango.Sensor',
                      lowlevel = True,
                      tangodevice = tango_base + 'table/2thetaenc',
                      unit = 'deg',
                     ),
    mo_twotheta = device('devices.tango.Motor',
                      lowlevel = True,
                      tangodevice = tango_base + 'table/2thetamot',
                      abslimits = (-20, 130),
                      unit = 'deg',
                      precision = 0.005,
                     ),
    twotheta = device('devices.generic.Axis',
                      description = 'table twotheta axis',
                      motor = 'mo_twotheta',
                      coder = 'co_twotheta',
                      obs = [],
                      fmtstr = '%.2f',
                      precision = 0.005,
                     ),

    co_chi1  = device('devices.tango.Sensor',
                      lowlevel = True,
                      tangodevice = tango_base + 'table/chi1enc',
                      unit = 'deg',
                     ),
    mo_chi1  = device('devices.tango.Motor',
                      lowlevel = True,
                      tangodevice = tango_base + 'table/chi1mot',
                      abslimits = (-5, 5),
                      unit = 'deg',
                      precision = 0.005,
                     ),
    chi1     = device('devices.generic.Axis',
                      description = 'table chi1 axis',
                      motor = 'mo_chi1',
                      coder = 'co_chi1',
                      obs = [],
                      fmtstr = '%.2f',
                      precision = 0.005,
                     ),

    co_chi2  = device('devices.tango.Sensor',
                      lowlevel = True,
                      tangodevice = tango_base + 'table/chi2enc',
                      unit = 'deg',
                     ),
    mo_chi2  = device('devices.tango.Motor',
                      lowlevel = True,
                      tangodevice = tango_base + 'table/chi2mot',
                      abslimits = (-5, 5),
                      unit = 'deg',
                      precision = 0.005,
                     ),
    chi2     = device('devices.generic.Axis',
                      description = 'table chi2 axis',
                      motor = 'mo_chi2',
                      coder = 'co_chi2',
                      obs = [],
                      fmtstr = '%.2f',
                      precision = 0.005,
                     ),

    co_lftctr = device('devices.tango.Sensor',
                      lowlevel = True,
                      tangodevice = tango_base + 'lftctr/lftctrenc',
                      unit = 'deg',
                     ),
    mo_lftctr = device('devices.tango.Motor',
                      lowlevel = True,
                      tangodevice = tango_base + 'lftctr/lftctrmot',
                      abslimits = (-5, 30),
                      unit = 'deg',
                      precision = 0.01,
                     ),
    liftingctr = device('devices.generic.Axis',
                      description = 'lifting counter axis',
                      motor = 'mo_lftctr',
                      coder = 'co_lftctr',
                      pollinterval = 15,
                      maxage = 61,
                      fmtstr = '%.2f',
                      abslimits = (-5, 30),
                      precision = 0.01,
                     ),

    lubrication = device('poli.lubrication.LubeSwitch',
                      description = 'lubrication switch',
                      tangodevice = tango_base + 'fzjdp_digital/lubrication',
                      lowlevel = True,
                     ),
)

startupcode = """
"""
