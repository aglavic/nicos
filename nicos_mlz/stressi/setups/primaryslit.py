description = 'Primary slit devices'

group = 'lowlevel'

tango_base = 'tango://motorbox03.stressi.frm2.tum.de:10000/box/'

devices = dict(
    pst_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'channel1/motor',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    pst_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'channel1/coder',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    pst = device('nicos.devices.generic.Axis',
        description = 'Primary slit translation (PST)',
        motor = 'pst_m',
        coder = 'pst_c',
        precision = 0.01,
    ),
    psz_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'channel2/motor',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    psz_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'channel2/coder',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    psz = device('nicos.devices.generic.Axis',
        description = 'Primary slit Z translation (PSZ)',
        motor = 'psz_m',
        coder = 'psz_c',
        precision = 0.01,
    ),
    psx_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'channel5/motor',
        fmtstr = '%.2f',
        speed = 2,
        lowlevel = True,
    ),
    psx = device('nicos.devices.generic.Axis',
        description = 'Primary optics translation in beam direction',
        fmtstr = '%.2f',
        motor = 'psx_m',
        precision = 0.01,
    ),
)
