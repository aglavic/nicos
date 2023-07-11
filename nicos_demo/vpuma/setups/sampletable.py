description = 'Sample table'
group = 'lowlevel'

devices = dict(
    st_phi = device('nicos.devices.generic.VirtualMotor',
        unit = 'deg',
        abslimits = (-50, 116.1),
        speed = 1.5,
        visibility = (),
    ),
    co_phi = device('nicos.devices.generic.VirtualCoder',
        motor = 'st_phi',
        visibility = (),
    ),
    phi = device('nicos.devices.generic.Axis',
        description = 'Sample scattering angle Two Theta',
        motor = 'st_phi',
        coder = 'co_phi',
        precision = 0.005,
        offset = 0.21, #May 2017 done by GE
        maxtries = 10,
        loopdelay = 1,
        jitter = 0.2,
        dragerror = 1,
    ),
    st_psi = device('nicos.devices.generic.VirtualMotor',
        unit = 'deg',
        abslimits = (-1000, 1000),
        userlimits = (5, 355),
        speed = 2,
        visibility = (),
    ),
    psi_puma = device('nicos.devices.generic.Axis',
        description = 'Sample rocking angle Theta',
        motor = 'st_psi',
        precision = 0.005,
        offset = 0,
        maxtries = 5,
    ),
    psi = device('nicos.devices.generic.DeviceAlias',
        description = 'Sample rocking angle Theta',
        alias = 'psi_puma',
        # when magnet is on :
        # alias = 'sth_m7T5_ccr',
        devclass = 'nicos.devices.generic.Axis',
        # when magnet is on :
        # devclass = 'nicos.devices.taco.Axis',
    ),
    # Tilting
    st_sgx = device('nicos.devices.generic.VirtualMotor',
        unit = 'deg',
        abslimits = (-15.6, 15.6),
        speed = 1,
        visibility = (),
    ),
    st_sgy = device('nicos.devices.generic.VirtualMotor',
        unit = 'deg',
        abslimits = (-15.6, 15.6),
        speed = 1,
        visibility = (),
    ),
    sgx = device('nicos.devices.generic.Axis',
        description = 'Sample tilt around X',
        motor = 'st_sgx',
        precision = 0.02,
        offset = 0,
        fmtstr = '%.3f',
        maxtries = 5,
    ),
    sgy = device('nicos.devices.generic.Axis',
        description = 'Sample tilt around Y',
        motor = 'st_sgy',
        precision = 0.02,
        offset = 0,
        fmtstr = '%.3f',
        maxtries = 5,
    ),

    # Translation
    st_stx = device('nicos.devices.generic.VirtualMotor',
        unit = 'mm',
        abslimits = (-18.1, 18.1),
        speed = 1,
        visibility = (),
    ),
    st_sty = device('nicos.devices.generic.VirtualMotor',
        unit = 'mm',
        abslimits = (-18.1, 18.1),
        speed = 1,
        visibility = (),
    ),
    st_stz = device('nicos.devices.generic.VirtualMotor',
        unit = 'mm',
        abslimits = (-20, 20),
        speed = 1,
        visibility = (),
    ),
    stx = device('nicos.devices.generic.Axis',
        description = 'Sample translation along X',
        motor = 'st_stx',
        precision = 0.05,
        offset = 0.0,
        fmtstr = '%.3f',
        maxtries = 9,
        loopdelay = 1,
        abslimits = (-18.1, 18.1),
    ),
    sty = device('nicos.devices.generic.Axis',
        description = 'Sample translation along Y',
        motor = 'st_sty',
        precision = 0.05,
        offset = 0.0,
        fmtstr = '%.3f',
        maxtries = 9,
        loopdelay = 1,
    ),
    stz = device('nicos.devices.generic.Axis',
        description = 'Sample translation along Z',
        motor = 'st_stz',
        precision = 0.1,
        offset = 0,
        fmtstr = '%.2f',
        maxtries = 10,
        loopdelay = 2,
    ),
    vg1 = device('nicos.devices.tas.VirtualGonio',
        description = 'Gonio along orient1 reflex',
        cell = 'Sample',
        gx = 'sgx',
        gy = 'sgy',
        axis = 1,
        unit = 'deg',
    ),
    vg2 = device('nicos.devices.tas.VirtualGonio',
        description = 'Gonio along orient2 reflex',
        cell = 'Sample',
        gx = 'sgx',
        gy = 'sgy',
        axis = 2,
        unit = 'deg',
    ),
)

alias_config = {
    'psi': {'psi_puma': 0},
}
