description = 'New phytron based slits'
group = 'optional'
display_order = 6
tango_base = 'tango://resedahw2.reseda.frm2:10000/reseda/slit'

devices = dict(
    slit1_top_mot = device('nicos.devices.entangle.Motor',
        description = 'Slit 1 top blade',
        tangodevice = tango_base + '1/top_mot',
        visibility = (),
    ),
    slit1_top_enc = device('nicos.devices.entangle.Sensor',
        description = 'Slit 1 top blade',
        tangodevice = tango_base + '1/top_enc',
        fmtstr = '%.3f',
        visibility = (),
    ),
    slit1_top = device('nicos.devices.generic.Axis',
        description = 'Slit 1 top blade',
        motor = 'slit1_top_mot',
        coder = 'slit1_top_enc',
        fmtstr = '%.3f',
        precision = 0.1,
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit1_bottom_mot = device('nicos.devices.entangle.Motor',
        description = 'Slit 1 bottom blade',
        tangodevice = tango_base + '1/bottom_mot',
        visibility = (),
    ),
    slit1_bottom_enc = device('nicos.devices.entangle.Sensor',
        description = 'Slit 1 bottom blade',
        tangodevice = tango_base + '1/bottom_enc',
        fmtstr = '%.3f',
        visibility = (),
    ),
    slit1_bottom = device('nicos.devices.generic.Axis',
        description = 'Slit 1 bottom blade',
        motor = 'slit1_bottom_mot',
        coder = 'slit1_bottom_enc',
        fmtstr = '%.3f',
        precision = 0.1,
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit1_left_mot = device('nicos.devices.entangle.Motor',
        description = 'Slit 1 left blade',
        tangodevice = tango_base + '1/left_mot',
        visibility = (),
    ),
    slit1_left_enc = device('nicos.devices.entangle.Sensor',
        description = 'Slit 1 left blade',
        tangodevice = tango_base + '1/left_enc',
        fmtstr = '%.3f',
        visibility = (),
    ),
    slit1_left = device('nicos.devices.generic.Axis',
        description = 'Slit 1 left blade',
        motor = 'slit1_left_mot',
        coder = 'slit1_left_enc',
        fmtstr = '%.3f',
        precision = 0.1,
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit1_right_mot = device('nicos.devices.entangle.Motor',
        description = 'Slit 1 right blade',
        tangodevice = tango_base + '1/right_mot',
        visibility = (),
    ),
    slit1_right_enc = device('nicos.devices.entangle.Sensor',
        description = 'Slit 1 right blade',
        tangodevice = tango_base + '1/right_enc',
        fmtstr = '%.3f',
       visibility = (),
    ),
    slit1_right = device('nicos.devices.generic.Axis',
        description = 'Slit 1 right blade',
        motor = 'slit1_right_mot',
        coder = 'slit1_right_enc',
        fmtstr = '%.3f',
        precision = 0.1,
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit1 = device('nicos.devices.generic.Slit',
        description = 'Slit 1',
        top = 'slit1_top',
        bottom = 'slit1_bottom',
        left = 'slit1_left',
        right = 'slit1_right',
        opmode = 'offcentered',
        coordinates = 'opposite',
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit2_top_mot = device('nicos.devices.entangle.Motor',
        description = 'Slit 2 top blade',
        tangodevice = tango_base + '2/top_mot',
        visibility = (),
    ),
    slit2_top_enc = device('nicos.devices.entangle.Sensor',
        description = 'Slit 2 top blade',
        tangodevice = tango_base + '2/top_enc',
        fmtstr = '%.3f',
        visibility = (),
    ),
    slit2_top = device('nicos.devices.generic.Axis',
        description = 'Slit 2 top blade',
        motor = 'slit2_top_mot',
        coder = 'slit2_top_enc',
        fmtstr = '%.3f',
        precision = 0.1,
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit2_bottom_mot = device('nicos.devices.entangle.Motor',
        description = 'Slit 2 bottom blade',
        tangodevice = tango_base + '2/bottom_mot',
        visibility = (),
    ),
    slit2_bottom_enc = device('nicos.devices.entangle.Sensor',
        description = 'Slit 2 bottom blade',
        tangodevice = tango_base + '2/bottom_enc',
        fmtstr = '%.3f',
        visibility = (),
    ),
    slit2_bottom = device('nicos.devices.generic.Axis',
        description = 'Slit 2 bottom blade',
        motor = 'slit2_bottom_mot',
        coder = 'slit2_bottom_enc',
        fmtstr = '%.3f',
        precision = 0.1,
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit2_left_mot = device('nicos.devices.entangle.Motor',
        description = 'Slit 2 left blade',
        tangodevice = tango_base + '2/left_mot',
        visibility = (),
    ),
    slit2_left_enc = device('nicos.devices.entangle.Sensor',
        description = 'Slit 2 left blade',
        tangodevice = tango_base + '2/left_enc',
        fmtstr = '%.3f',
        visibility = (),
    ),
    slit2_left = device('nicos.devices.generic.Axis',
        description = 'Slit 2 left blade',
        motor = 'slit2_left_mot',
        coder = 'slit2_left_enc',
        fmtstr = '%.3f',
        precision = 0.1,
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit2_right_mot = device('nicos.devices.entangle.Motor',
        description = 'Slit 2 right blade',
        tangodevice = tango_base + '2/right_mot',
        visibility = (),
    ),
    slit2_right_enc = device('nicos.devices.entangle.Sensor',
        description = 'Slit 2 right blade',
        tangodevice = tango_base + '2/right_enc',
        fmtstr = '%.3f',
        visibility = (),
    ),
    slit2_right = device('nicos.devices.generic.Axis',
        description = 'Slit 2 right blade',
        motor = 'slit2_right_mot',
        coder = 'slit2_right_enc',
        fmtstr = '%.3f',
        precision = 0.1,
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
    slit2 = device('nicos.devices.generic.Slit',
        description = 'Slit 2',
        top = 'slit2_top',
        bottom = 'slit2_bottom',
        left = 'slit2_left',
        right = 'slit2_right',
        opmode = 'offcentered',
        coordinates = 'opposite',
        unit = 'mm',
        maxage = 119,
        pollinterval = 60,
    ),
)
