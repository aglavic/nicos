description = 'ErWIN detector devices'

group = 'optional'

tango_host = 'taco6.ictrl.frm2.tum.de'

tango_base = 'tango://%s:10000/test/bcharm/' % tango_host

devices = dict(
    b_cathode1 = device('nicos.devices.tango.PowerSupply',
        description = 'Cathode 1',
        tangodevice = tango_base + 'cathode1',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    b_cathode2 = device('nicos.devices.tango.PowerSupply',
        description = 'Cathode 2',
        tangodevice = tango_base + 'cathode2',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    b_window = device('nicos.devices.tango.PowerSupply',
        description = 'Window',
        tangodevice = tango_base + 'window',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    b_tripped = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Trip indicator',
        tangodevice = tango_base + 'trip',
        mapping = {
            '': 0,
            'High current seen': 1,
            'High current': 2,
            'Trip': 3,
        },
    ),
    b_hv = device('nicos_mlz.erwin.devices.charmhv.HVSwitch',
        description = 'HV supply small detector',
        anodes = ['b_anode%d' % i for i in range(1, 10)],
        banodes = ['b_banode%d' % i for i in range(1, 9)],
        cathodes = ['b_cathode1', 'b_cathode2'],
        window = 'b_window',
        mapping = {
            'on': {
                'b_anode1': 2190,
                'b_anode2': 2192,
                'b_anode3': 2194,
                'b_anode4': 2197,
                'b_anode5': 2200,
                'b_anode6': 2203,
                'b_anode7': 2206,
                'b_anode8': 2208,
                'b_anode9': 2210,
                'b_banode1': 2192,
                'b_banode2': 2194,
                'b_banode3': 2196,
                'b_banode4': 2199,
                'b_banode5': 2299,
                'b_banode6': 2298,
                'b_banode7': 2297,
                'b_banode8': 2296,
                'b_cathode1': 200,
                'b_cathode2': 200,
                'b_window': -1500,
                'ramp': 50,
            },
            'off': {
                'b_anode1': 0,
                'b_anode2': 0,
                'b_anode3': 0,
                'b_anode4': 0,
                'b_anode5': 0,
                'b_anode6': 0,
                'b_anode7': 0,
                'b_anode8': 0,
                'b_anode9': 0,
                'b_banode1': 0,
                'b_banode2': 0,
                'b_banode3': 0,
                'b_banode4': 0,
                'b_banode5': 0,
                'b_banode6': 0,
                'b_banode7': 0,
                'b_banode8': 0,
                'b_cathode1': 0,
                'b_cathode2': 0,
                'b_window': 0,
                'ramp': 100,
            },
            'safe': {
                'b_anode1': 200,
                'b_anode2': 200,
                'b_anode3': 200,
                'b_anode4': 200,
                'b_anode5': 200,
                'b_anode6': 200,
                'b_anode7': 200,
                'b_anode8': 200,
                'b_anode9': 200,
                'b_banode1': 200,
                'b_banode2': 200,
                'b_banode3': 200,
                'b_banode4': 200,
                'b_banode5': 200,
                'b_banode6': 200,
                'b_banode7': 200,
                'b_banode8': 200,
                'b_cathode1': 200,
                'b_cathode2': 200,
                'b_window': 200,
                'ramp': 100,
            },
        },
    ),
)

for i in range(1, 10):
    devices['b_anode%d' % i] = device('nicos.devices.tango.PowerSupply',
        description = 'Anode %d' % i,
        tangodevice = tango_base + 'anode%d' % i,
        fmtstr = '%.1f',
        lowlevel = True,
    )

for i in range(1, 9):
    devices['b_banode%d' % i] = device('nicos.devices.tango.PowerSupply',
        description = 'Boundary anode %d' % i,
        tangodevice = tango_base + 'banode%d' % i,
        fmtstr = '%.1f',
        lowlevel = True,
    )
