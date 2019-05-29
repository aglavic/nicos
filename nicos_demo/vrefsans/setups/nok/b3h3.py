description = 'B3 aperture devices'

group = 'optional'

group = 'lowlevel'

devices = dict(
    b3 = device('nicos_mlz.refsans.devices.slits.DoubleSlitSequence',
        description = 'b3 and h3 inside Samplechamber',
        fmtstr = '%.3f mm, %.3f mm',
        adjustment = 'b3h3_frame',
        unit = '',
        slit_r = 'b3r',
        slit_s = 'b3s',
    ),
    b3h3_frame = device('nicos.devices.generic.ManualSwitch',
        description = 'positioning Frame of b3h3',
        states = ['110mm', '70mm'],
    ),
    b3r = device('nicos_mlz.refsans.devices.slits.SingleSlit',
       description = 'b3 slit, reactor side',
       visibility = (),
       motor = 'b3_r',
       nok_start = 11334.5,
       nok_end = 11334.5,
       masks = {
           'slit': 36.32,
           'point': 36.32,
           'gisans': 36.32,
       },
       unit = 'mm',
    ),
    b3s = device('nicos_mlz.refsans.devices.slits.SingleSlit',
       description = 'b3 slit, sample side',
       visibility = (),
       motor = 'b3_s',
       nok_start = 11334.5,
       nok_end = 11334.5,
       masks = {
           'slit': 36.404,
           'point': 36.404,
           'gisans': 36.404,
       },
       unit = 'mm',
    ),
    b3_r = device('nicos.devices.generic.Axis',
        description = 'b3, reactorside',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-393.0, 330.0),
            speed = 1.,
            unit = 'mm',
        ),
        offset = 0.0,
        precision = 0.01,
        visibility = (),
    ),
    b3_s = device('nicos.devices.generic.Axis',
        description = 'b3, sampleside',
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-102.0, 170.0),
            speed = 1.,
            unit = 'mm',
        ),
        offset = 0.0,
        precision = 0.01,
        visibility = (),
    ),
    h3 = device('nicos_mlz.refsans.devices.slits.DoubleSlit',
        description = 'h3 together with b3',
        fmtstr = 'open: %.3f, xpos: %.3f',
        maxheight = 80,
        unit = 'mm',
        slit_r = 'h3r',
        slit_s = 'h3s',
    ),
    h3r = device('nicos_mlz.refsans.devices.slits.SingleSlit',
        description = 'h3 blade TOFTOF',
        motor = 'h3_r',
        masks = {
            'slit':   151.0,
            'point':  0,
            'gisans': 0,
        },
        unit = 'mm',
        visibility = (),
    ),
    h3s = device('nicos_mlz.refsans.devices.slits.SingleSlit',
        description = 'h3 blade KWS',
        motor = 'h3_s',
        masks = {
            'slit':   48.0,
            'point':  0,
            'gisans': 0,
        },
        unit = 'mm',
        visibility = (),
    ),
    h3_r = device('nicos.devices.generic.Axis',
        description = 'h3, TOFTOF',
        motor = device('nicos.devices.generic.VirtualMotor',
            unit = 'mm',
            abslimits = (-393.0, 330.0),
            speed = 1.,
            visibility = (),
        ),
        precision = 0.03,
        visibility = (),
    ),
    h3_s = device('nicos.devices.generic.Axis',
        description = 'h3, ',
        motor = device('nicos.devices.generic.VirtualMotor',
            unit = 'mm',
            abslimits = (-102.0, 170.0),
            speed = 1.,
            visibility = (),
        ),
        precision = 0.03,
        visibility = (),
    ),
)

alias_config = {
    'last_aperture': {'b3': 100},
}
