description = 'Devices and commands for the Siemens S7 SPS at ZEBRA'

spsprefix = 'SQ:ZEBRA:SPS:'
hide = ()

modules = ['nicos_sinq.zebra.commands.spscommands']

devices = dict(
    opt_bench_p = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Optical bench pressure failure',
        readpv = spsprefix + 'OPT-BENCH-P_RBV',
        visibility = hide,
    ),
    beam_exit_p = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Beam exit pressure failure',
        readpv = spsprefix + 'BEAM-EXIT-P_RBV',
        visibility = hide,
    ),
    exc_count = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Excessive countrate on 2D detector',
        readpv = spsprefix + 'EXC-COUNTRATE_RBV',
        visibility = hide,
    ),
    shutter_error = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Shutter system error',
        readpv = spsprefix + 'SHUTTER_ERROR_RBV',
        visibility = hide,
    ),
    w1_p = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Wagen 1 pressure failure',
        readpv = spsprefix + 'WG1-P_RBV',
        visibility = hide,
    ),
    w2_p = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Wagen 2 pressure failure',
        readpv = spsprefix + 'WG2-P_RBV',
        visibility = hide,
    ),
    w1_c = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Wagen 1 motor crash',
        readpv = spsprefix + 'WG1-CRASH_RBV',
        visibility = hide,
    ),
    w2_c = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Wagen 2 motor crash',
        readpv = spsprefix + 'WG2-CRASH_RBV',
        visibility = hide,
    ),
    w1 = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Wagen 1 connected',
        readpv = spsprefix + 'WAGEN1_RBV',
        visibility = hide,
    ),
    w2 = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Wagen 2 connected',
        readpv = spsprefix + 'WAGEN2_RBV',
        visibility = hide,
    ),
    oned = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'Single counter',
        readpv = spsprefix + 'ONED_RBV',
        visibility = hide,
    ),
    twod = device('nicos.devices.epics.pyepics.EpicsReadable',
        description = 'EMBL 2D detector',
        readpv = spsprefix + 'TWOD_RBV',
        visibility = hide,
    ),
    mcu2 = device('nicos_sinq.devices.epics.extensions.EpicsCommandReply',
        description = 'Direct connection to MCU2',
        commandpv = 'SQ:ZEBRA:mcu2' + '.AOUT',
        replypv = 'SQ:ZEBRA:mcu2' + '.AINP',
    ),
    euler_present = device('nicos_sinq.zebra.devices.readeuler.EulerPresent',
        description = 'Eulerian cradle',
        unit = 'Bool',
        mcu = 'mcu2'
    ),
    pgbutton = device('nicos.devices.epics.pyepics.EpicsDigitalMoveable',
        description = 'PG filter toggle',
        readpv = spsprefix + 'PGFILTER_BUTTON',
        writepv = spsprefix + 'PGFILTER_BUTTON',
        visibility = hide
    ),
    pgpulse = device('nicos.devices.generic.Pulse',
        moveable = 'pgbutton',
        onvalue = 1,
        offvalue = 0,
        ontime = 1.1,
        visibility = hide
    ),
    pgfilter = device('nicos_sinq.devices.s7_switch.S7Switch',
        description = 'Control for the PG filter',
        button = 'pgpulse',
        readpv = spsprefix + 'PGFILTER_RBV',
        timeout = 5,
        mapping = {
            'In': 1,
            'Out': 0
        }
    ),
    colbutton = device('nicos.devices.epics.pyepics.EpicsDigitalMoveable',
        description = 'PG filter toggle',
        readpv = spsprefix + 'COLL2D_BUTTON',
        writepv = spsprefix + 'COLL2D_BUTTON',
        visibility = hide
    ),
    colpulse = device('nicos.devices.generic.Pulse',
        moveable = 'colbutton',
        onvalue = 1,
        offvalue = 0,
        ontime = 1.1,
        visibility = hide
    ),
    coll2d = device('nicos_sinq.devices.s7_switch.S7Switch',
        description = 'Control for the collimator for the 2D detector',
        button = 'colpulse',
        readpv = spsprefix + 'COLL2D_RBV',
        timeout = 5,
        mapping = {
            'On': 1,
            'Off': 0
        }
    ),
    shbutton = device('nicos.devices.epics.pyepics.EpicsDigitalMoveable',
        description = 'Shutter button',
        readpv = spsprefix + 'SHUTTER_BUTTON',
        writepv = spsprefix + 'SHUTTER_BUTTON',
        visibility = hide
    ),
    shpulse = device('nicos.devices.generic.Pulse',
        moveable = 'shbutton',
        onvalue = 1,
        offvalue = 0,
        ontime = 1.1,
        visibility = hide
    ),
    shutter = device('nicos_sinq.devices.s7_switch.S7Shutter',
        description = 'Shutter Control',
        button = 'shpulse',
        readpv = spsprefix + 'SHUTTER_OPEN_RBV',
        closedpv = spsprefix + 'SHUTTER_CLOSED_RBV',
        readypv = spsprefix + 'SHUTTER_READY_RBV',
        errorpv = spsprefix + 'SHUTTER_ERROR_RBV',
        timeout = 5,
    ),
)
