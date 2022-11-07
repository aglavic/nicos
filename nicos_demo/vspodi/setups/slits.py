description = 'Slits'

group = 'lowlevel'

devices = dict(
    # Monochromator slit
    slitm_u = device('nicos.devices.generic.Axis',
        description = 'Monochromator slit upper blade',
        motor = 'slitm_u_m',
        coder = 'slitm_u_c',
        precision = 0.01,
    ),
    slitm_u_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (0, 87),
        unit = 'mm',
        speed = 1,
        fmtstr = '%.2f',
        visibility = (),
    ),
    slitm_u_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'slitm_u_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    slitm_d = device('nicos.devices.generic.Axis',
        description = 'Monochromator slit lower blade',
        motor = 'slitm_d_m',
        coder = 'slitm_d_c',
        precision = 0.01,
    ),
    slitm_d_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (0, 87),
        unit = 'mm',
        speed = 1,
        fmtstr = '%.2f',
        visibility = (),
    ),
    slitm_d_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'slitm_d_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    slitm_l = device('nicos.devices.generic.Axis',
        description = 'Monochromator slit left blade',
        motor = 'slitm_l_m',
        coder = 'slitm_l_c',
        precision = 0.01,
    ),
    slitm_l_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (0, 16),
        unit = 'mm',
        speed = 1,
        fmtstr = '%.2f',
        visibility = (),
    ),
    slitm_l_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'slitm_l_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    slitm_r = device('nicos.devices.generic.Axis',
        description = 'Monochromator slit right blade',
        motor = 'slitm_r_m',
        coder = 'slitm_r_c',
        precision = 0.01,
    ),
    slitm_r_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (0, 16),
        unit = 'mm',
        speed = 1,
        fmtstr = '%.2f',
        visibility = (),
    ),
    slitm_r_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'slitm_r_m',
        fmtstr = '%.2f',
        visibility = (),
    ),
    slitm = device('nicos.devices.generic.Slit',
        description = 'Monochromator slit 4 blades',
        left = 'slits_l',
        right = 'slits_r',
        bottom = 'slits_d',
        top = 'slits_u',
        coordinates = 'opposite',
        opmode = 'centered',
    ),
    slits_u = device('nicos.devices.generic.VirtualReferenceMotor',
        description = 'Sample slit upper blade',
        fmtstr = '%.2f',
        unit = 'mm',
        abslimits = (0, 45),
        visibility = (),
        speed = 1,
        refswitch = 'high',
        refpos = 46,
    ),
    slits_d = device('nicos.devices.generic.VirtualReferenceMotor',
        description = 'Sample slit lower blade',
        fmtstr = '%.2f',
        unit = 'mm',
        abslimits = (0, 45),
        visibility = (),
        speed = 1,
        refswitch = 'high',
        refpos = 46,
    ),
    slits_l = device('nicos.devices.generic.VirtualReferenceMotor',
        description = 'Sample slit left blade',
        fmtstr = '%.2f',
        unit = 'mm',
        abslimits = (0, 15),
        visibility = (),
        speed = 1,
        refswitch = 'high',
        refpos = 16,
    ),
    slits_r = device('nicos.devices.generic.VirtualReferenceMotor',
        description = 'Sample slit right blade',
        fmtstr = '%.2f',
        unit = 'mm',
        abslimits = (0, 15),
        visibility = (),
        speed = 1,
        refswitch = 'high',
        refpos = 16,
    ),
    slits = device('nicos.devices.generic.Slit',
        description = 'Sample slit 4 blades',
        left = 'slits_l',
        right = 'slits_r',
        bottom = 'slits_d',
        top = 'slits_u',
        coordinates = 'opposite',
        opmode = 'centered',
        parallel_ref = True,
    ),
)
