#  -*- coding: utf-8 -*-

description = 'Resonance flippers'
group = 'lowlevel'
display_order = 24

tango_base = 'tango://resedahw2.reseda.frm2:10000/reseda'

devices = dict(
    hrf_0a = device('nicos.devices.entangle.PowerSupply',
        description = 'Helmholtz coils for resonant flippers arm 0 - A',
        tangodevice = '%s/spf1/current' % tango_base,
        fmtstr = '%.3f',
        tangotimeout = 5.0,
        pollinterval = 60,
        maxage = 120,
        unit = 'A',
        precision = 0.02,
    ),
    hrf_0a_current = device('nicos.devices.entangle.Sensor',
        description = 'Read back of the current in arm 0 - A coil',
        tangodevice = tango_base + '/mss1/current',
    ),
    hrf_0b = device('nicos.devices.entangle.PowerSupply',
        description = 'Helmholtz coils for resonant flipper arm 0 - B',
        tangodevice = '%s/spf2/current' % tango_base,
        fmtstr = '%.3f',
        tangotimeout = 5.0,
        pollinterval = 60,
        maxage = 120,
        unit = 'A',
        precision = 0.02,
    ),
    hrf_0b_current = device('nicos.devices.entangle.Sensor',
        description = 'Read back of the current in arm 0 - B coil',
        tangodevice = tango_base + '/mss2/current',
    ),
    hrf_1a = device('nicos.devices.entangle.PowerSupply',
        description = 'Helmholtz coils for resonant flipper arm 1 - A',
        tangodevice = '%s/heinzinger1a/current' % tango_base,
        fmtstr = '%.3f',
        tangotimeout = 5.0,
        pollinterval = 60,
        maxage = 120,
        unit = 'A',
        precision = 0.02,
    ),
    hrf_1b = device('nicos.devices.entangle.PowerSupply',
        description = 'Helmholtz coils for resonant flipper arm 1 - B',
        tangodevice = '%s/heinzinger1b/current' % tango_base,
        fmtstr = '%.3f',
        tangotimeout = 5.0,
        pollinterval = 60,
        maxage = 120,
        unit = 'A',
        precision = 0.02,
    ),
)

for i in range(1, 4):
    devices['T_hrf_0a_%d' % i] = device('nicos.devices.entangle.Sensor',
                                        description = 'Temperature %d in superconduting coil 0a' % i,
                                        tangodevice = tango_base + '/mss1/temp%d' % i,
                                        )
    devices['T_hrf_0b_%d' % i] = device('nicos.devices.entangle.Sensor',
                                        description = 'Temperature %d in superconduting coil 0b' % i,
                                        tangodevice = tango_base + '/mss2/temp%d' % i,
                                        )
