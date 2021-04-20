description = 'MIRA1 monochromator'
group = 'lowlevel'

includes = ['base', 'sample', 'alias_mono']

tango_base = 'tango://miractrl.mira.frm2:10000/mira/'

devices = dict(
    co_m1tt = device('nicos.devices.entangle.Sensor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mtt_enc',
        unit = 'deg',
        precision = 0.05,
    ),
    mo_m1tt = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'mono1/mtt_mot',
        lowlevel = True,
        precision = 0.05,
    ),
    m1tt = device('nicos_mlz.mira.devices.axis.HoveringAxis',
        description = 'monochromator two-theta angle',
        abslimits = (-50.0, 0),
        motor = 'mo_m1tt',
        coder = 'co_m1tt',
        startdelay = 1,
        stopdelay = 4,
        switch = 'air_mono',
        switchvalues = (0, 1),
        fmtstr = '%.3f',
        precision = 0.05,
    ),
    co_m1th = device('nicos.devices.entangle.Sensor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mth_enc',
        unit = 'deg',
        precision = 0.02,
    ),
    mo_m1th = device('nicos.devices.entangle.Motor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mth_mot',
        unit = 'deg',
        precision = 0.02,
    ),
    m1th = device('nicos.devices.generic.Axis',
        description = 'monochromator theta angle',
        motor = 'mo_m1th',
        coder = 'co_m1th',
        fmtstr = '%.3f',
        precision = 0.02,
    ),
    co_m1tx = device('nicos.devices.entangle.Sensor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mtx_enc',
        unit = 'mm',
        precision = 0.02,
    ),
    mo_m1tx = device('nicos.devices.entangle.Motor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mtx_mot',
        unit = 'mm',
        precision = 0.02,
    ),
    m1tx = device('nicos.devices.generic.Axis',
        description = 'monochromator translation',
        motor = 'mo_m1tx',
        coder = 'co_m1tx',
        fmtstr = '%.3f',
        precision = 0.2,
    ),
    co_m1ty = device('nicos.devices.entangle.Sensor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mty_enc',
        unit = 'mm',
        precision = 0.2,
    ),
    mo_m1ty = device('nicos.devices.entangle.Motor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mty_mot',
        unit = 'mm',
        precision = 0.2,
    ),
    m1ty = device('nicos.devices.generic.Axis',
        description = 'monochromator translation',
        motor = 'mo_m1ty',
        coder = 'co_m1ty',
        fmtstr = '%.3f',
        precision = 0.2,
    ),
    co_m1gx = device('nicos.devices.entangle.Sensor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mgx_enc',
        unit = 'deg',
        precision = 0.02,
    ),
    mo_m1gx = device('nicos.devices.entangle.Motor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mgx_mot',
        unit = 'deg',
        precision = 0.02,
    ),
    m1gx = device('nicos.devices.generic.Axis',
        description = 'monochromator tilt',
        motor = 'mo_m1gx',
        coder = 'co_m1gx',
        fmtstr = '%.3f',
        precision = 0.02,
    ),
    co_m1ch = device('nicos.devices.entangle.Sensor',
        lowlevel = True,
        tangodevice = tango_base + 'mono1/mch_enc',
        unit = 'deg',
        precision = 0.02,
    ),
    mo_m1ch = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'mono1/mch_mot',
        lowlevel = True,
    ),
    m1ch = device('nicos.devices.generic.Axis',
        description = 'monochromator changer table rotation',
        motor = 'mo_m1ch',
        coder = 'co_m1ch',
        fmtstr = '%.3f',
        precision = 0.05,
    ),
)

startupcode = '''
mth.alias = m1th
mtt.alias = m1tt
mtx.alias = m1tx
mty.alias = m1ty
mgx.alias = m1gx
mfv.alias = None
'''
