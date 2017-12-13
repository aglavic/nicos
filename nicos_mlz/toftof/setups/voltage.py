description = 'low and high voltage power supplies for detector'

group = 'lowlevel'

includes = []

nethost = 'toftofsrv.toftof.frm2'

devices = dict(
    lvbus = device('nicos.devices.vendor.toni.ModBus',
        tacodevice = '//%s/toftof/rs232/ifpowersupply' % nethost,
        lowlevel = True,
    ),
    lv0 = device('nicos.devices.vendor.toni.LVPower',
        description = 'LV power supply 1',
        requires = {'level': 'admin'},
        bus = 'lvbus',
        addr = 0xF1,
        pollinterval = 10,
        maxage = 12,
    ),
    lv1 = device('nicos.devices.vendor.toni.LVPower',
        description = 'LV power supply 2',
        requires = {'level': 'admin'},
        bus = 'lvbus',
        addr = 0xF2,
        pollinterval = 10,
        maxage = 12,
    ),
    lv2 = device('nicos.devices.vendor.toni.LVPower',
        description = 'LV power supply 3',
        requires = {'level': 'admin'},
        bus = 'lvbus',
        addr = 0xF3,
        pollinterval = 10,
        maxage = 12,
    ),
    lv3 = device('nicos.devices.vendor.toni.LVPower',
        description = 'LV power supply 4',
        requires = {'level': 'admin'},
        bus = 'lvbus',
        addr = 0xF4,
        pollinterval = 10,
        maxage = 12,
    ),
    lv4 = device('nicos.devices.vendor.toni.LVPower',
        description = 'LV power supply 5',
        requires = {'level': 'admin'},
        bus = 'lvbus',
        addr = 0xF5,
        pollinterval = 10,
        maxage = 12,
    ),
    lv5 = device('nicos.devices.vendor.toni.LVPower',
        description = 'LV power supply 6',
        requires = {'level': 'admin'},
        bus = 'lvbus',
        addr = 0xF6,
        pollinterval = 10,
        maxage = 12,
    ),
    lv6 = device('nicos.devices.vendor.toni.LVPower',
        description = 'LV power supply 7',
        requires = {'level': 'admin'},
        bus = 'lvbus',
        addr = 0xF7,
        pollinterval = 10,
        maxage = 12,
    ),
    lv7 = device('nicos.devices.vendor.toni.LVPower',
        description = 'LV power supply 8',
        requires = {'level': 'admin'},
        bus = 'lvbus',
        addr = 0xF8,
        pollinterval = 10,
        maxage = 12,
    ),
    hv0 = device('nicos_mlz.toftof.devices.iseg.VoltageSupply',
        description = 'ISEG HV power supply 1',
        requires = {'level': 'admin'},
        tacodevice = '//%s/toftof/iseg1/voltage' % nethost,
        abslimits = (0, 1600),
        ramp = 120,
    ),
    hv1 = device('nicos_mlz.toftof.devices.iseg.VoltageSupply',
        description = 'ISEG HV power supply 2',
        requires = {'level': 'admin'},
        tacodevice = '//%s/toftof/iseg2/voltage' % nethost,
        abslimits = (0, 1600),
        ramp = 120,
    ),
)
