#  -*- coding: utf-8 -*-

description = 'Sample table (translation)'
group = 'optional'

tango_base = 'tango://resedahw2.reseda.frm2:10000/reseda'

devices = dict(
    srz_mot = device('nicos.devices.entangle.Motor',
        description = 'Sample rotation: z (motor)',
        tangodevice = '%s/srz/motor' % tango_base,
        fmtstr = '%.3f',
        unit = 'deg',
        visibility = (),
    ),
    srz_enc = device('nicos.devices.entangle.Sensor',
        description = 'Sample rotation: z (encoder)',
        tangodevice = '%s/srz/coder' % tango_base,
        fmtstr = '%.3f',
        unit = 'deg',
        visibility = (),
    ),
    srz = device('nicos.devices.generic.Axis',
        description = 'Sample rotation: z',
        motor = 'srz_mot',
        coder = 'srz_enc',
        fmtstr = '%.3f',
        precision = 0.02,
        unit = 'deg',
    ),
    stx_mot = device('nicos.devices.entangle.Motor',
        description = 'Sample table: x',
        tangodevice = '%s/stx/motor' % tango_base,
        fmtstr = '%.2f',
        unit = 'mm',
        visibility = (),
    ),
    stx_enc = device('nicos.devices.entangle.Sensor',
        description = 'Sample table: x (encoder)',
        tangodevice = '%s/stx/coder' % tango_base,
        fmtstr = '%.3f',
        unit = 'mm',
        visibility = (),
    ),
    stx = device('nicos.devices.generic.Axis',
        description = 'Sample table: x',
        motor = 'stx_mot',
        coder = 'stx_enc',
        fmtstr = '%.3f',
        precision = 0.02,
        unit = 'mm',
    ),
    sty_mot = device('nicos.devices.entangle.Motor',
        description = 'Sample table: y',
        tangodevice = '%s/sty/motor' % tango_base,
        fmtstr = '%.2f',
        unit = 'mm',
        visibility = (),
    ),
    sty_enc = device('nicos.devices.entangle.Sensor',
        description = 'Sample table: y (encoder)',
        tangodevice = '%s/sty/coder' % tango_base,
        fmtstr = '%.3f',
        unit = 'mm',
        visibility = (),
    ),
    sty = device('nicos.devices.generic.Axis',
        description = 'Sample table: y',
        motor = 'sty_mot',
        coder = 'sty_enc',
        fmtstr = '%.3f',
        precision = 0.02,
        unit = 'mm',
    ),
    stz_mot = device('nicos.devices.entangle.Motor',
        description = 'Sample table: z',
        tangodevice = '%s/stz/motor' % tango_base,
        fmtstr = '%.2f',
        unit = 'mm',
        visibility = (),
    ),
    stz_enc = device('nicos.devices.entangle.Sensor',
        description = 'Sample table: z (encoder)',
        tangodevice = '%s/stz/coder' % tango_base,
        fmtstr = '%.3f',
        unit = 'mm',
        visibility = (),
    ),
    stz = device('nicos.devices.generic.Axis',
        description = 'Sample table: z',
        motor = 'stz_mot',
        # coder = 'stz_enc',  # hardware is not working properly
        fmtstr = '%.3f',
        precision = 0.02,
        unit = 'mm',
    ),
    sgx_mot = device('nicos.devices.entangle.Motor',
        description = 'Sample goniometer: x',
        tangodevice = '%s/sgx/motor' % tango_base,
        fmtstr = '%.3f',
        unit = 'deg',
        visibility = (),
    ),
    sgx_enc = device('nicos.devices.entangle.Sensor',
        description = 'Sample goniometer: x (encoder)',
        tangodevice = '%s/sgx/coder' % tango_base,
        fmtstr = '%.3f',
        unit = 'deg',
        visibility = (),
    ),
    sgx = device('nicos.devices.generic.Axis',
        description = 'Sample goniometer: x',
        motor = 'sgx_mot',
        coder = 'sgx_enc',
        fmtstr = '%.3f',
        precision = 0.002,
        unit = 'deg',
    ),
    sgy_mot = device('nicos.devices.entangle.Motor',
        description = 'Sample goniometer: x',
        tangodevice = '%s/sgy/motor' % tango_base,
        fmtstr = '%.3f',
        unit = 'deg',
        visibility = (),
    ),
    sgy_enc = device('nicos.devices.entangle.Sensor',
        description = 'Sample goniometer: y (encoder)',
        tangodevice = '%s/sgy/coder' % tango_base,
        fmtstr = '%.3f',
        unit = 'deg',
        visibility = (),
    ),
    sgy = device('nicos.devices.generic.Axis',
        description = 'Sample goniometer: y',
        motor = 'sgy_mot',
        # coder = 'sgy_enc',  # hardware is not working properly
        fmtstr = '%.3f',
        precision = 0.002,
        unit = 'deg',
    ),
    st_air = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Sample table pressured air',
        tangodevice = '%s/iobox/plc_air_sampletable' % tango_base,
        mapping = {'on': 1,
                   'off': 0},
        unit = '',
    ),
)
