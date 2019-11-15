description = 'Slits'

group = 'lowlevel'

devices = dict(
    # Monochromator slit
    # slitm_u = device('nicos.devices.vendor.caress.MuxMotor',
    #     description = 'HWB SLITM_U',
    #     fmtstr = '%.2f',
    #     unit = 'mm',
    #     coderoffset = 0,
    #     abslimits = (-31, 85),
    #     nameserver = '%s' % nameservice,
    #     objname = '%s' % servername,
    #     config = 'SLITM_U 39 3 1 1 10000 500 200 5.12 60',
    #     lowlevel = True,
    #     mux = 'mux',
    # ),
    # slitm_d = device('nicos.devices.vendor.caress.MuxMotor',
    #     description = 'HWB SLITM_D',
    #     fmtstr = '%.2f',
    #     unit = 'mm',
    #     coderoffset = 0,
    #     abslimits = (-85, 31),
    #     nameserver = '%s' % nameservice,
    #     objname = '%s' % servername,
    #     config = 'SLITM_D 39 3 1 2 10000 500 200 5.12 60',
    #     lowlevel = True,
    #     mux = 'mux',
    # ),
    # slitm_l = device('nicos.devices.vendor.caress.MuxMotor',
    #     description = 'HWB SLITM_L',
    #     fmtstr = '%.2f',
    #     unit = 'mm',
    #     coderoffset = 0,
    #     abslimits = (-15.2, 15.2),
    #     nameserver = '%s' % nameservice,
    #     objname = '%s' % servername,
    #     config = 'SLITM_L 39 3 1 3 1000 500 200 5.12 30',
    #     lowlevel = True,
    #     mux = 'mux',
    # ),
    # slitm_r = device('nicos.devices.vendor.caress.MuxMotor',
    #     description = 'HWB SLITM_R',
    #     fmtstr = '%.2f',
    #     unit = 'mm',
    #     coderoffset = 0,
    #     abslimits = (-15.2, 15.2),
    #     nameserver = '%s' % nameservice,
    #     objname = '%s' % servername,
    #     config = 'SLITM_R 39 3 1 4 1000 500 200 5.12 30',
    #     lowlevel = True,
    #     mux = 'mux',
    # ),
    # slitm = device('nicos_mlz.stressi.devices.slit.Slit',
    #     description = 'Monochromator slit 4 blades',
    #     left = 'slits_l',
    #     right = 'slits_r',
    #     bottom = 'slits_d',
    #     top = 'slits_u',
    #     opmode = 'centered',
    #     pollinterval = 60,
    #     maxage = 90,
    # ),
    slits_u = device('nicos.devices.generic.VirtualReferenceMotor',
        description = 'Sample slit upper blade',
        fmtstr = '%.2f',
        unit = 'mm',
        abslimits = (0, 45),
        lowlevel = True,
        speed = 1,
        refswitch = 'high',
        refpos = 46,
    ),
    slits_d = device('nicos.devices.generic.VirtualReferenceMotor',
        description = 'Sample slit lower blade',
        fmtstr = '%.2f',
        unit = 'mm',
        abslimits = (0, 45),
        lowlevel = True,
        speed = 1,
        refswitch = 'high',
        refpos = 46,
    ),
    slits_l = device('nicos.devices.generic.VirtualReferenceMotor',
        description = 'Sample slit left blade',
        fmtstr = '%.2f',
        unit = 'mm',
        abslimits = (0, 15),
        lowlevel = True,
        speed = 1,
        refswitch = 'high',
        refpos = 16,
    ),
    slits_r = device('nicos.devices.generic.VirtualReferenceMotor',
        description = 'Sample slit right blade',
        fmtstr = '%.2f',
        unit = 'mm',
        abslimits = (0, 15),
        lowlevel = True,
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
