description = 'Monochromator tower devices'

group = 'lowlevel'

tango_base = 'tango://kompasshw.kompass.frm2:10000/kompass/'

devices = dict(
    # A1
    mth_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'mono/mth_m',
        fmtstr = '%.4f',
        visibility = (),
    ),
    mth_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'mono/mth_c',
        fmtstr = '%.4f',
        visibility = (),
    ),
    mth = device('nicos.devices.generic.Axis',
        description = 'monochromator theta (A1)',
        motor = 'mth_m',
        coder = 'mth_c',
        fmtstr = '%.3f',
        precision = 0.001,
    ),
    # A2
    mtt_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'aircontrol/plc_mtt_mot',
        fmtstr = '%.4f',
        visibility = (),
    ),
    mtt_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'aircontrol/plc_mtt_enc',
        fmtstr = '%.4f',
        visibility = (),
    ),
    air_mono = device('nicos.devices.entangle.DigitalOutput',
        tangodevice = tango_base + 'aircontrol/plc_airpads_sampletable',
        visibility = (),
    ),
    mtt = device('nicos_mlz.mira.devices.axis.HoveringAxis',
        description = 'primary spectrometer angle (A2)',
        motor = 'mtt_m',
        coder = 'mtt_c',
        startdelay = 2,
        stopdelay = 2,
        switch = 'air_mono',
        switchvalues = (0, 1),
        fmtstr = '%.4f',
        precision = 0.001,
    ),
    mx_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'mono/mx_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    mx_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'mono/mx_c',
        fmtstr = '%.2f',
        visibility = (),
    ),
    mx = device('nicos.devices.generic.Axis',
        description = 'monochromator table X',
        motor = 'mx_m',
        coder = 'mx_c',
        fmtstr = '%.2f',
        precision = 0.05,
    ),
    my_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'mono/my_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    my_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'mono/my_c',
        fmtstr = '%.2f',
        visibility = (),
    ),
    my = device('nicos.devices.generic.Axis',
        description = 'monochromator table Y',
        motor = 'my_m',
        coder = 'my_m',
        fmtstr = '%.2f',
        precision = 0.05,
    ),
    mc_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'mono/mc_m',
        fmtstr = '%.1f',
        visibility = (),
    ),
    mc_c = device('nicos.devices.entangle.Sensor',
        tangodevice = tango_base + 'mono/mc_c',
        fmtstr = '%.1f',
        visibility = (),
    ),
    mc = device('nicos.devices.generic.Axis',
        description = 'monochromator table cradle',
        motor = 'mc_m',
        coder = 'mc_m',  # 'mc_c',
        fmtstr = '%.1f',
        precision = 0.05,
    ),
    mfv_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'mono/mfv_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    # currently unused
    #mfv_c = device('nicos.devices.entangle.Sensor',
    #    tangodevice = tango_base + 'mono/mfv_c',
    #    fmtstr = '%.2f',
    #    visibility = (),
    #),
    mfv = device('nicos.devices.generic.Axis',
        description = 'monochromator vertical focus',
        motor = 'mfv_m',
        coder = 'mfv_m',
        fmtstr = '%.2f',
        precision = 0.01,
    ),
    mfh_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'mono/mfh_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    # currently broken
    #mfh_c = device('nicos.devices.entangle.Sensor',
    #    tangodevice = tango_base + 'mono/mfh_c',
    #    fmtstr = '%.2f',
    #    visibility = (),
    #),
    mfh = device('nicos.devices.generic.Axis',
        description = 'monochromator horizontal focus',
        motor = 'mfh_m',
        coder = 'mfh_m',
        fmtstr = '%.2f',
        precision = 0.01,
    ),

    mono = device('nicos.devices.tas.Monochromator',
        description = 'monochromator unit to move incoming wavevector',
        unit = 'A-1',
        theta = 'mth',
        twotheta = 'mtt',
        focush = 'mfh',
        focusv = 'mfv',
        # abslimits = (0.1, 10),
        abslimits = (1.08, 3.3),
        focmode = 'manual',  # for now
        hfocuspars = [0],
        vfocuspars = [0],
        scatteringsense = 1,
        crystalside = 1,
        dvalue = 3.355,
    ),

    mshl_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'slit/mshl_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    # currently unused
    #mshl_c = device('nicos.devices.entangle.Sensor',
    #    tangodevice = tango_base + 'mono/mshl_c',
    #    fmtstr = '%.2f',
    #    visibility = (),
    #),
    mshl = device('nicos.devices.generic.Axis',
        description = 'monochromator slit left',
        motor = 'mshl_m',
        coder = 'mshl_m',
        fmtstr = '%.2f',
        precision = 0.01,
        visibility = (),
    ),

    mshr_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'slit/mshr_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    # currently unused
    #mshr_c = device('nicos.devices.entangle.Sensor',
    #    tangodevice = tango_base + 'mono/mshr_c',
    #    fmtstr = '%.2f',
    #    visibility = (),
    #),
    mshr = device('nicos.devices.generic.Axis',
        description = 'monochromator slit right',
        motor = 'mshr_m',
        coder = 'mshr_m',
        fmtstr = '%.2f',
        precision = 0.01,
        visibility = (),
    ),

    msvb_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'slit/msvb_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    # currently unused
    #msvb_c = device('nicos.devices.entangle.Sensor',
    #    tangodevice = tango_base + 'mono/msvb_c',
    #    fmtstr = '%.2f',
    #    visibility = (),
    #),
    msvb = device('nicos.devices.generic.Axis',
        description = 'monochromator slit bottom',
        motor = 'msvb_m',
        coder = 'msvb_m',
        fmtstr = '%.2f',
        precision = 0.01,
        visibility = (),
    ),

    msvt_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'slit/msvt_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    # currently unused
    #msvt_c = device('nicos.devices.entangle.Sensor',
    #    tangodevice = tango_base + 'mono/msvt_c',
    #    fmtstr = '%.2f',
    #    visibility = (),
    #),
    msvt = device('nicos.devices.generic.Axis',
        description = 'monochromator slit top',
        motor = 'msvt_m',
        coder = 'msvt_m',
        fmtstr = '%.2f',
        precision = 0.01,
        visibility = (),
    ),

    ms = device('nicos.devices.generic.Slit',
        description = 'slit before monochromator',
        left = 'mshl',
        right = 'mshr',
        bottom = 'msvb',
        top = 'msvt',
        opmode = 'offcentered',
        coordinates = 'opposite',
    ),
)
