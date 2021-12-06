description = 'Sample table devices'

group = 'lowlevel'
includes = ['sampleslit']

tango_base = 'tango://kompasshw.kompass.frm2:10000/kompass/'

devices = dict(
    # A3
    sth_st_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'sample/sth_m',
        fmtstr = '%.4f',
        lowlevel = True,
    ),
    sth_st_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'sample/sth_c',
        fmtstr = '%.4f',
        lowlevel = True,
    ),
    sth_st = device('nicos.devices.generic.Axis',
        description = 'sample theta (A3)',
        motor = 'sth_st_m',
        coder = 'sth_st_c',
        fmtstr = '%.3f',
        precision = 0.001,
    ),
    # A4
    stt_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'sample/stt_m',
        fmtstr = '%.4f',
        lowlevel = True,
    ),
    stt_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'sample/stt_c',
        fmtstr = '%.4f',
        lowlevel = True,
    ),
    air_anadet = device('nicos.devices.entangle.DigitalOutput',
        tangodevice = tango_base + 'aircontrol/plc_airpads_analyser',
        lowlevel = True,
    ),

    pbs = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'primary beamstop at sample table',
        tangodevice = tango_base + 'aircontrol/plc_primary_beamstop',
        mapping = dict(up=1, down=0),
    ),

    stt = device('nicos_mlz.kompass.devices.pbs.SttWithPBS',
        description = 'secondary spectrometer angle (A4) with pbs',
        stt = 'stt_ax',
        pbs = 'pbs',
        limits = (-30, 38),
        pbs_values = ('down', 'up'),
    ),

    stt_ax = device('nicos_mlz.mira.devices.axis.HoveringAxis',
        description = 'secondary spectrometer angle (A4)',
        motor = 'stt_m',
        coder = 'stt_c',
        startdelay = 2,
        stopdelay = 2,
        switch = 'air_anadet',
        switchvalues = (0, 1),
        fmtstr = '%.3f',
        precision = 0.001,
    ),

    # sample translation
    sx_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'sample/sx_m',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    sx_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'sample/sx_c',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    sx = device('nicos.devices.generic.Axis',
        description = 'sample table X',
        motor = 'sx_m',
        coder = 'sx_c',
        fmtstr = '%.2f',
        precision = 0.05,
    ),
    sy_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'sample/sy_m',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    sy_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'sample/sy_c',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    sy = device('nicos.devices.generic.Axis',
        description = 'sample table Y',
        motor = 'sy_m',
        coder = 'sy_c',
        fmtstr = '%.2f',
        precision = 0.05,
    ),

    # sample gonios
    scx_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'sample/scx_m',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    scx_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'sample/scx_c',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    scx = device('nicos.devices.generic.Axis',
        description = 'sample table cradle X',
        motor = 'scx_m',
        coder = 'scx_c',
        fmtstr = '%.1f',
        precision = 0.05,
    ),
    scy_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'sample/scy_m',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    scy_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'sample/scy_c',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    scy = device('nicos.devices.generic.Axis',
        description = 'sample table cradle Y',
        motor = 'scy_m',
        coder = 'scy_c',
        fmtstr = '%.1f',
        precision = 0.05,
    ),

    sz_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'sample/sz_m',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    sz = device('nicos.devices.generic.Axis',
        description = 'sample table Z translation',
        motor = 'sz_m',
        coder = 'sz_m',
        fmtstr = '%.1f',
        precision = 0.01,
    ),
    vg1 = device('nicos.devices.tas.VirtualGonio',
        description = 'Gonio along orient1 reflex',
        cell = 'Sample',
        gx = 'scx',
        gy = 'scy',
        axis = 1,
        unit = 'deg',
    ),
    vg2 = device('nicos.devices.tas.VirtualGonio',
        description = 'Gonio along orient2 reflex',
        cell = 'Sample',
        gx = 'scx',
        gy = 'scy',
        axis = 2,
        unit = 'deg',
    ),
)

alias_config = {
    'sth': {'sth_st': 100}
}
