description = 'collimation tube'

includes = ['system', 'instrument_shutter']

excludes = ['collimation_config']

# included by sans1
group = 'lowlevel'

tangohost = 'tango://hw.sans1.frm2.tum.de:10000'

devices = dict(
    col = device('nicos.devices.generic.LockedDevice',
        description = 'sans1 primary collimation',
        lock = 'instrument_shutter',
        device = 'col_sw',
        #lockvalue = None,     # go back to previous value
        unlockvalue = 'close',
        #keepfixed = False,    # dont fix attenuator after movement
        pollinterval = 15,
        maxage = 60,
    ),
    col_sw = device('nicos.devices.generic.MultiSwitcher',
#    col = device('nicos.devices.generic.MultiSwitcher',
        description = 'collimator switching device',
        precision = None,
        blockingmove = False,
        unit = 'm',
        fmtstr = '%.1f',
        fallback = 'undefined',
        moveables = ['col_20', 'col_18', 'col_16', 'col_14', 'col_12', 'col_10',
        'col_8', 'col_6', 'col_4', 'col_3', 'col_2'],
        mapping = {
            1.5: ['ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng'],
            2: ['ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'col'],
            3: ['ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'col', 'col'],
            4: ['ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'col', 'col', 'col'],
            6: ['ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'col', 'col', 'col', 'col'],
            8: ['ng',  'ng',  'ng',  'ng',  'ng',  'ng',  'col', 'col', 'col', 'col', 'col'],
            10: ['ng',  'ng',  'ng',  'ng',  'ng',  'col', 'col', 'col', 'col', 'col', 'col'],
            12: ['ng',  'ng',  'ng',  'ng',  'col', 'col', 'col', 'col', 'col', 'col', 'col'],
            14: ['ng',  'ng',  'ng',  'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col'],
            16: ['ng',  'ng',  'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col'],
            18: ['ng',  'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col'],
            20: ['col', 'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col', 'col'],
        },
        visibility = (),
    ),
#    att = device('nicos_mlz.sans1.devices.collimotor.Switcher',
#        description = 'Attenuator',
#        mapping = dict(dia10=15.626, x10=108.626, x100=201.626, x1000=294.626, open=387.626),
#        moveable = 'att_a',
#        blockingmove = False,
#        pollinterval = 15,
#        maxage = 60,
#        precision = 0.1,
#    ),
#    att_a = device('nicos.devices.generic.Axis',
#        description = 'Attenuator axis',
#        motor = 'att_m',
#        coder = 'att_c',
#        dragerror = 17,
#        precision = 0.05,
#        visibility = (),
#        jitter = 1,
#    ),
#    att_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
#        description = 'Attenuator motor',
#        # IP-adresse: 172.25.49.107
#        tangodevice='%s/coll/ng-pol/modbus'% (tangohost,),
#        address = 0x4020+0*10,
#        slope = 200*4, # FULL steps per turn * turns per mm
#        microsteps = 8,
#        unit = 'mm',
#        refpos = 10.92,
#        abslimits = (-400, 600),
#        visibility = (),
#        precision = 0.0025,
#        autozero = None, # no auto referencing with an axis !!!
#        #autozero = 80,
#    ),
#    att_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
#        description = 'Attenuator coder',
#        # IP-adresse: 172.25.49.107
#        tangodevice='%s/coll/ng-pol/modbus'% (tangohost,),
#        address = 0x40c8,
#        slope = 1000000, # resolution = nm, we want mm
#        zeropos = -13.191 + 26.5861880569,
#        unit = 'mm',
#        visibility = (),
#    ),
    ng_pol = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Neutronguide polariser',
        mapping = dict(ng=1.060, pol1=117, pol2=234, col=352.7),
        moveable = 'ng_pol_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        precision = 0.05,
    ),
    ng_pol_a = device('nicos.devices.generic.Axis',
        description = 'Neutronguide polariser axis',
        motor = 'ng_pol_m',
        coder = 'ng_pol_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    ng_pol_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Neutronguide polariser motor',
        # IP-adresse: 172.25.49.107
        tangodevice='%s/coll/ng-pol/modbus'% (tangohost,),
        address = 0x4020+1*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -4.5,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    ng_pol_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Neutronguide polariser coder',
        # IP-adresse: 172.25.49.107
        tangodevice='%s/coll/ng-pol/modbus'% (tangohost,),
        address = 0x40cd,
        slope = 1000000, # resolution = nm, we want mm
        zeropos = -13.191 + 26.5861880569,
        unit = 'mm',
        visibility = (),
    ),
#-------------------------------------------------------------------------------
#    ng_pol_c_test = device('nicos.devices.entangle.Sensor',
#        description = 'NG Pol coder test device',
#        # IP-adresse: 172.25.49.114
#        tangodevice='%s/coll/3m_test/plc_encoder1'% (tangohost,),
#        unit = 'mm',
#        visibility = (),
#    ),
#-------------------------------------------------------------------------------
    col_20 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 20',
        mapping = dict(ng=1.003, col=117, free1=234, las=351),
        moveable = 'col_20_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        precision = 0.05,
    ),
    col_20_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 20',
        motor = 'col_20_m',
        coder = 'col_20_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_20_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 20 motor',
        # IP-adresse: 172.25.49.108
        tangodevice='%s/coll/col-20m/modbus'% (tangohost,),
        address = 0x4020+0*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -5.39,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_20_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 20 coder',
        # IP-adresse: 172.25.49.108
        tangodevice='%s/coll/col-20m/modbus'% (tangohost,),
        address = 0x40c8,  # docu page 9
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 12.8533378965, # unspecified in docu page 9
        unit = 'mm',
        visibility = (),
    ),
    col_18 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 18',
        mapping = dict(ng=0.841, col=117, free1=234, free2=351),
        moveable = 'col_18_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_18_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 18',
        motor = 'col_18_m',
        coder = 'col_18_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_18_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 18',
        # IP-adresse: 172.25.49.108
        tangodevice='%s/coll/col-20m/modbus'% (tangohost,),
        address = 0x4020+1*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -5.28,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_18_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 18 coder',
        # IP-adresse: 172.25.49.108
        tangodevice='%s/coll/col-20m/modbus'% (tangohost,),
        address = 0x40cd,  # docu page 10
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 13.899101438, # unspecified in docu page 10
        unit = 'mm',
        visibility = (),
    ),
    col_16 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 16',
        mapping = dict(ng=1.229, col=117, free1=234, free2=351),
        moveable = 'col_16_a',
        blockingmove = False,
        pollinterval = 1,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_16_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 16',
        motor = 'col_16_m',
        coder = 'col_16_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_16_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 16 motor',
        # IP-adresse: 172.25.49.111
        tangodevice='%s/coll/col-16m/modbus'% (tangohost,),
        address = 0x4020+1*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -4.29,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_16_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 16 coder',
        # IP-adresse: 172.25.49.111
        tangodevice='%s/coll/col-16m/modbus'% (tangohost,),
        address = 0x40c8,  # docu page 12
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 17.8761710467, # unspecified in docu page 12
        unit = 'mm',
        visibility = (),
    ),
    bg1 = device('nicos_mlz.sans1.devices.collimotor.Slit',
        description = 'Background slit1',
        mapping = {'49mm': 1.0, 'open': 91.3, '19mm': 181.3, '41mm': 271.3 },
        moveable = 'bg1_m',
        table = 'col_16',
        activeposition = 'col',
        pollinterval = 15,
        maxage = 60,
    ),
    bg1_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Background slit1 motor',
        # IP-adresse: 172.25.49.111
        tangodevice='%s/coll/col-16m/modbus'% (tangohost,),
        address = 0x4020+0*10,
        slope = 200*0.16, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'deg',
        refpos = -28.85,
        abslimits = (-40, 300),
        visibility = (),
        precision = 0.05,
        autozero = 400,
    ),
    col_14 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 14',
        mapping = dict(ng=1.486, col=117, free1=234, free2=351),
        moveable = 'col_14_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_14_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 14',
        motor = 'col_14_m',
        coder = 'col_14_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_14_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 14 motor',
        # IP-adresse: 172.25.49.111
        tangodevice='%s/coll/col-16m/modbus'% (tangohost,),
        address = 0x4020+2*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -2.31,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_14_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 14 coder',
        # IP-adresse: 172.25.49.111
        tangodevice='%s/coll/col-16m/modbus'% (tangohost,),
        address = 0x40cd,  # docu page 13
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 17.2842048903, # unspecified in docu page 13
        unit = 'mm',
        visibility = (),
    ),
    col_12 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 12',
        mapping = dict(ng=1.310, col=117, free1=234, free2=351),
        moveable = 'col_12_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_12_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 12',
        motor = 'col_12_m',
        coder = 'col_12_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_12_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 12 motor',
        # IP-adresse: 172.25.49.112
        tangodevice='%s/coll/col-12m/modbus'% (tangohost,),
        address = 0x4020+0*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -1.7,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_12_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 12 coder',
        # IP-adresse: 172.25.49.112
        tangodevice='%s/coll/col-12m/modbus'% (tangohost,),
        address = 0x40c8,  # docu page 14
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 17.1303596823, # unspecified in docu page 14
        unit = 'mm',
        visibility = (),
    ),
    col_10 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 10',
        mapping = dict(ng=1.348, col=117, free1=234, free2=351),
        moveable = 'col_10_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_10_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 10',
        motor = 'col_10_m',
        coder = 'col_10_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_10_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 10 motor',
        # IP-adresse: 172.25.49.112
        tangodevice='%s/coll/col-12m/modbus'% (tangohost,),
        address = 0x4020+1*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -5.14, #needs to be checked by O. Frank !!!
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_10_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 10 coder',
        # IP-adresse: 172.25.49.112
        tangodevice='%s/coll/col-12m/modbus'% (tangohost,),
        address = 0x40cd,  # docu page 15
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 17.2115868978, # unspecified in docu page 15
        unit = 'mm',
        visibility = (),
    ),
    col_8 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 8',
        mapping = dict(ng=1.679, col=117, free1=234, free2=351),
        moveable = 'col_8_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_8_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 8',
        motor = 'col_8_m',
        coder = 'col_8_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_8_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 8 motor',
        # IP-adresse: 172.25.49.113
        tangodevice='%s/coll/col-8m/modbus'% (tangohost,),
        address = 0x4020+1*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -3.88,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_8_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 8 coder',
        # IP-adresse: 172.25.49.113
        tangodevice='%s/coll/col-8m/modbus'% (tangohost,),
        address = 0x40c8,  # docu page 17
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 17.0752135418, # unspecified in docu page 17
        unit = 'mm',
        visibility = (),
    ),
    col_6 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 6',
        mapping = dict(ng=0.909, col=117, free1=234, free2=351),
        moveable = 'col_6_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_6_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 6',
        motor = 'col_6_m',
        coder = 'col_6_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_6_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 6 motor',
        # IP-adresse: 172.25.49.113
        tangodevice='%s/coll/col-8m/modbus'% (tangohost,),
        address = 0x4020+2*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -4.13,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_6_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 6 coder',
        # IP-adresse: 172.25.49.113
        tangodevice='%s/coll/col-8m/modbus'% (tangohost,),
        address = 0x40cd,  # docu page 18
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 15.859918895, # unspecified in docu page 18
        unit = 'mm',
        visibility = (),
    ),
    bg2 = device('nicos_mlz.sans1.devices.collimotor.Slit',
        description = 'Background slit2',
        mapping = {'27mm': 270, '19mm': 179.5, '11mm': 90.5, 'open': 1.2 },
        moveable = 'bg2_m',
        table = 'col_6',
        activeposition = 'col',
        pollinterval = 15,
        maxage = 60,
    ),
    bg2_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Background slit2 motor',
        # IP-adresse: 172.25.49.113
        tangodevice='%s/coll/col-8m/modbus'% (tangohost,),
        address = 0x4020+0*10,
        slope = 200*0.16, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'deg',
        refpos = -1.5,
        abslimits = (-40, 300),
        visibility = (),
        precision = 0.05,
        autozero = 400,
    ),
    col_4 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 4',
        mapping = dict(ng=0.985, col=117, free1=234, free2=351),
        moveable = 'col_4_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_4_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 4',
        motor = 'col_4_m',
        coder = 'col_4_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_4_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 4 motor',
        # IP-adresse: 172.25.49.114 neu
        tangodevice='%s/coll/col-4m/modbus'% (tangohost,),
        address = 0x4020+1*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -9.37,
        abslimits = (-400, 600),
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_4_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 4 coder',
        # IP-adresse: 172.25.49.114
        tangodevice='%s/coll/col-4m/modbus'% (tangohost,),
        address = 0x40cd,  # docu page 19
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 17.5324112754, # unspecified in docu page 20
        unit = 'mm',
        visibility = (),
    ),
    col_3 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 3',
        mapping = dict(ng=1.010, col=117, free1=234, free2=351),
        moveable = 'col_3_m',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_3_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 3',
        motor = 'col_3_m',
        # coder = 'col_3_m',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_3_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 3 motor',
        # IP-adresse: 172.25.49.114
        tangodevice='%s/coll/col-4m/modbus'% (tangohost,),
        address = 0x4020+2*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -9.35,
        abslimits = (-400, 600),
        autozero = 100, # auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
#    col_3_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
#        description = 'Collimotor 3 coder',
#        # IP-adresse: 172.25.49.114
#        tangodevice='%s/coll/col-4m/modbus'% (tangohost,),
#        address = 0x40c8,  # docu page 20
#        slope = 1000000, # resolution = nm, we want mm
#        zeropos = 18.6575767247, # unspecified in docu page 19
#        unit = 'mm',
#        visibility = (),
#    ),

    col_2 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'Collimotor 2',
        mapping = dict(ng=1, col=117, free1=234, free2=351),
        moveable = 'col_2_a',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
        visibility = (),
        precision = 0.05,
    ),
    col_2_a = device('nicos.devices.generic.Axis',
        description = 'Collimotor 2',
        motor = 'col_2_m',
        coder = 'col_2_c',
        dragerror = 17,
        precision = 0.05,
        visibility = (),
        jitter = 1,
    ),
    col_2_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'Collimotor 2 motor',
        # IP-adresse: 172.25.49.115
        tangodevice='%s/coll/col-2m/modbus'% (tangohost,),
        address = 0x4020+1*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -8.,
        abslimits = (-400, 600),
        autopower = 'on',
        autozero = None, # no auto referencing with an axis !!!
        precision = 0.0025,
        visibility = (),
    ),
    col_2_c = device('nicos_mlz.sans1.devices.collimotor.Coder',
        description = 'Collimotor 2 coder',
        # IP-adresse: 172.25.49.115
        tangodevice='%s/coll/col-2m/modbus'% (tangohost,),
        address = 0x40c8,  # docu page 22
        slope = 1000000, # resolution = nm, we want mm
        zeropos = 17.7929853926, # unspecified in docu page 22
        unit = 'mm',
        visibility = (),
    ),
    sa1 = device('nicos_mlz.sans1.devices.collimotor.Switcher',
        description = 'attenuation slits',
        mapping = {'29mm': 0, '19mm': 70, '9mm': 140},
        moveable = 'sa1_m',
        blockingmove = False,
        pollinterval = 15,
        maxage = 60,
    ),
    sa1_m = device('nicos_mlz.sans1.devices.collimotor.Motor',
        description = 'attenuation slits motor',
        # IP-adresse: 172.25.49.115
        tangodevice='%s/coll/col-2m/modbus'% (tangohost,),
        address = 0x4020+0*10,
        slope = 200*4, # FULL steps per turn * turns per mm
        microsteps = 8,
        unit = 'mm',
        refpos = -34.7,
        abslimits = (-40, 300),
        visibility = (),
        autozero = 400,
    ),
)

monitor_blocks = dict(
    default = Block('Collimation',
        [
            BlockRow(
                Field(dev='att', name='att',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['x10','x100','x1000','OPEN'],
                      width=6.5,height=9),
                Field(dev='ng_pol', name='ng_pol',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','POL2','POL1','NG'],
                      width=5.5,height=9),
                Field(dev='col_20', name='20',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='col_18', name='18',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='bg1', name='bg1',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['50mm','OPEN','20mm','42mm'],
                      disabled_options = ['N.A.'],
                      width=7,height=9),
                Field(dev='col_16', name='16',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='col_14', name='14',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='col_12', name='12',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='col_10', name='10',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='col_8', name='8',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='col_6', name='6',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='bg2', name='bg2',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['28mm','20mm','12mm','OPEN'],
                      disabled_options = ['N.A.'],
                      width=7,height=9),
                Field(dev='col_4', name='4',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='col_3', name='3',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                Field(dev='col_2', name='2',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['LAS','free','COL','NG'],
                      width=5,height=9),
                # Field(dev='col_2b', name='2b',
                #       widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                #       options=['LAS','free','COL','NG'],
                #       width=5, height=9),
                Field(dev='sa1', name='sa1',
                      widget='nicos_mlz.sans1.gui.monitorwidgets.CollimatorTable',
                      options=['20mm','30mm','50x50'],
                      disabled_options = ['N.A.'],
                      width=7,height=9),
            ),
            BlockRow(
                Field(dev='bg1_m', name='bg1_m', format='%.1f', width=12),
                Field(dev='bg2_m', name='bg2_m', format='%.1f', width=12),
                Field(dev='sa1_m', name='sa1_m', format='%.1f', width=12),
            ),
            BlockRow(
                Field(dev='att_m', name='att_m', format='%.1f', width=12),
                Field(dev='col_20_m', name='20_m', format='%.1f', width=12),
                Field(dev='col_16_m', name='16_m', format='%.1f', width=12),
                Field(dev='col_12_m', name='12_m', format='%.1f', width=12),
                Field(dev='col_8_m', name='8_m', format='%.1f', width=12),
                Field(dev='col_4_m', name='4_m', format='%.1f', width=12),
                Field(dev='col_2_m', name='2_m', format='%.1f', width=12),
            ),
            BlockRow(
                Field(dev='ng_pol_m', name='ng_pol_m', format='%.1f', width=12),
                Field(dev='col_18_m', name='18_m', format='%.1f', width=12),
                Field(dev='col_14_m', name='14_m', format='%.1f', width=12),
                Field(dev='col_10_m', name='10_m', format='%.1f', width=12),
                Field(dev='col_6_m', name='6_m', format='%.1f', width=12),
                Field(dev='col_3_m', name='3_m', format='%.1f', width=12),
                # Field(dev='col_2b_m', name='2b_m', format='%.1f', width=12),
            ),
            BlockRow(
                Field(dev='col', name='col'),
            ),
        ],
    ),
    html = Block('Collimation',
        [
            BlockRow(
                Field(dev='bg1', name='bg1', width=12),
                Field(dev='bg2', name='bg2', width=12),
                Field(dev='sa1', name='sa1', width=12),
                Field(dev='sa2', name='sa2', width=12),
            ),
            BlockRow(
                Field(dev='col', name='col', unit='m', format = '%.1f', width=12),
            ),
        ],
    ),
)
