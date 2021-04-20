description = 'motors moving the sample stage in the experiment chamber.'

group = 'lowlevel'

tangobase = 'tango://localhost:10000/box/'

devices = dict(
    sample_Ty_m = device('nicos.devices.entangle.Motor',
        description = 'Sample translation y-axis motor',
        tangodevice = tangobase + 'sample/Ty_Motor',
        lowlevel = True,
    ),
    sample_Ty = device('nicos.devices.generic.Axis',
        description = 'Sample translation y-axis',
        motor = 'sample_Ty_m',
        # coder = 'sample_tilt_c',
        precision = 0.01,
    ),
    sample_Tz_m = device('nicos.devices.entangle.Motor',
        description = 'Sample translation z-axis motor',
        tangodevice = tangobase + 'sample/Tz_Motor',
        lowlevel = True,
    ),
    sample_Tz = device('nicos.devices.generic.Axis',
        description = 'Sample translation z-axis',
        motor = 'sample_Tz_m',
        # coder = 'sample_tilt_c',
        precision = 0.01,
    ),
    sample_Rx_m = device('nicos.devices.entangle.Motor',
        description = 'sample stage rotation x-axis motor',
        tangodevice = tangobase + 'sample/Rx_Motor',
        lowlevel = True,
    ),
    sample_Rx = device('nicos.devices.generic.Axis',
        description = 'sample stage rotation x-axis',
        motor = 'sample_Rx_m',
        precision = 0.01,
    ),
    sample_Ry_m = device('nicos.devices.entangle.Motor',
        description = 'sample stage rotation y-axis motor',
        tangodevice = tangobase + 'sample/Ry_Motor',
        lowlevel = True,
    ),
    # if encoder should be used, this is how to implement it
    # sample_Rot_y_c = device('nicos.devices.entangle.Sensor',
    #    description = 'sample stage rotation coder',
    #    tangodevice = tangobase + 'sample/Ry_encoder',
    #    lowlevel = True,
    # ),
    sample_Ry = device('nicos.devices.generic.Axis',
        description = 'sample stage rotation y-axis',
        motor = 'sample_Ry_m',
        # coder = 'sample_Ry_c',
        precision = 0.01,
    ),
    sample_Rz_m = device('nicos.devices.entangle.Motor',
        description = 'sample stage rotation z-axis motor',
        tangodevice = tangobase + 'sample/Rz_Motor',
        lowlevel = True,
    ),
    sample_Rz = device('nicos.devices.generic.Axis',
        description = 'sample stage rotation z-axis',
        motor = 'sample_Rz_m',
        # coder = 'sample_tilt_c',
        precision = 0.01,
    ),
)
