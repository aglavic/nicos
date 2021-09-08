description = 'Small Beam Limiter in Experimental Chamber 1'

group = 'optional'

tango_base = 'tango://phytron01.nectar.frm2:10000/'

devices = dict(
    nbl_l = device('nicos.devices.entangle.Motor',
        description = 'Beam Limiter Left Blade',
        tangodevice = tango_base + 'box/nbl_l/mot',
        lowlevel = True,
    ),
    nbl_r = device('nicos.devices.entangle.Motor',
        description = 'Beam Limiter Right Blade',
        tangodevice = tango_base + 'box/nbl_r/mot',
        lowlevel = True,
    ),
    nbl_t = device('nicos.devices.entangle.Motor',
        description = 'Beam Limiter Top Blade',
        tangodevice = tango_base + 'box/nbl_t/mot',
        lowlevel = True,
    ),
    nbl_b = device('nicos.devices.entangle.Motor',
        description = 'Beam Limiter Bottom Blade',
        tangodevice = tango_base + 'box/nbl_b/mot',
        lowlevel = True,
    ),
    nbl = device('nicos_mlz.nectar.devices.BeamLimiter',
        description = 'NECTAR Beam Limiter',
        left = 'nbl_l',
        right = 'nbl_r',
        top = 'nbl_t',
        bottom = 'nbl_b',
        opmode = 'centered',
        coordinates = 'opposite',
        pollinterval = 5,
        maxage = 10,
        parallel_ref = True,
    ),
)
