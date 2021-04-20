description = 'ErWIN detector devices'

group = 'optional'

tango_host = 'taco6.ictrl.frm2.tum.de'

tango_base = 'tango://%s:10000/test/scharm/' % tango_host

devices = dict(
    s_anode1 = device('nicos.devices.entangle.PowerSupply',
        description = 'Anode 1',
        tangodevice = tango_base + 'anode1',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    s_anode2 = device('nicos.devices.entangle.PowerSupply',
        description = 'Anode 2',
        tangodevice = tango_base + 'anode2',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    s_banode1 = device('nicos.devices.entangle.PowerSupply',
        description = 'Boundary anode 1',
        tangodevice = tango_base + 'banode1',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    s_cathode1 = device('nicos.devices.entangle.PowerSupply',
        description = 'Cathode 1',
        tangodevice = tango_base + 'cathode1',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    s_cathode2 = device('nicos.devices.entangle.PowerSupply',
        description = 'Cathode 2',
        tangodevice = tango_base + 'cathode2',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    s_window = device('nicos.devices.entangle.PowerSupply',
        description = 'Window',
        tangodevice = tango_base + 'window',
        fmtstr = '%.1f',
        lowlevel = True,
    ),
    s_tripped = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Trip indicator',
        tangodevice = tango_base + 'trip',
        mapping = {
            '': 0,
            'High current seen': 1,
            'High current': 2,
            'Trip': 3,
        },
        pollinterval = 1,
    ),
    s_hv = device('nicos_mlz.erwin.devices.charmhv.HVSwitch',
        description = 'HV supply small detector',
        anodes = ['s_anode1', 's_anode2'],
        banodes = ['s_banode1'],
        cathodes = ['s_cathode1', 's_cathode2'],
        window = 's_window',
        trip = 's_tripped',
        pollinterval = 1,
        mapping = {
            'on': {
                's_anode1': 2175,
                's_anode2': 2200,
                's_banode1': 2185,
                's_cathode1': 200,
                's_cathode2': 200,
                's_window': -1500,
                'ramp': 50,
            },
            'off': {
                's_anode1': 0,
                's_anode2': 0,
                's_banode1': 0,
                's_cathode1': 0,
                's_cathode2': 0,
                's_window': 0,
                'ramp': 100,
            },
            'safe': {
                's_anode1': 200,
                's_anode2': 200,
                's_banode1': 200,
                's_cathode1': 200,
                's_cathode2': 200,
                's_window': 200,
                'ramp': 100,
            },
        },
    ),
)
