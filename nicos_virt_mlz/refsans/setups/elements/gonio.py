description = 'Sample table devices'

group = 'lowlevel'

devices = dict(
    gonio_theta = device('nicos.devices.generic.Axis',
        description = 'Theta axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-5, 5),
            speed = 0.125,
            unit = 'deg',
        ),
        precision = 0.01,
    ),
    gonio_phi = device('nicos.devices.generic.Axis',
        description = 'Phi axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-500, 500),
            speed = 1.,
            unit = 'deg',
        ),
        precision = 0.01,
    ),
    gonio_omega = device('nicos.devices.generic.Axis',
        description = 'Omega axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-500, 500),
            speed = 0.1,
            unit = 'deg',
        ),
        precision = 0.01,
    ),
    gonio_y = device('nicos.devices.generic.Axis',
        description = 'Y axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-500, 500),
            speed = 0.2,
            unit = 'mm',
        ),
        precision = 0.01,
    ),
    gonio_z = device('nicos.devices.generic.Axis',
        description = 'Z axis',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-500, 500),
            speed = 0.5,
            unit = 'mm',
        ),
        precision = 0.01,
    ),
    gonio_x = device('nicos_mlz.refsans.devices.analogencoder.AnalogEncoder',
        description = 'pos of goniometer in beamdirection, with respect to b3',
        device = device('nicos.devices.generic.ManualMove',
            # default = 0.14501711047921587,
            default = 55,
            abslimits = (0, 100),
            unit = 'V',
        ),
        poly = [-0.269211180059716, 381.122648733114],
        unit = 'mm',
    ),
)

alias_config = {
    'alphai': {'gonio_theta': 100},
    'd_last_slit_sample': {'gonio_x': 300},
}
