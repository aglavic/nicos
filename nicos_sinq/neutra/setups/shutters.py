description = 'NEUTRA shutters (HE, FS, Exp)'

display_order = 10

group = 'lowlevel'

epics_timeout = 3.0

devices = dict(
    # Main Shutter HE
    he_sopen = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = epics_timeout,
        description = 'HE Shutter opening bit',
        readpv = 'SQ:NEUTRA:b4io3:HEopen',
        writepv = 'SQ:NEUTRA:b4io3:HEopen',
        lowlevel = True,
    ),
    he_sclose = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = epics_timeout,
        description = 'HE Shutter closing bit',
        readpv = 'SQ:NEUTRA:b4io3:HEclose',
        writepv = 'SQ:NEUTRA:b4io3:HEclose',
        lowlevel = True,
    ),
    he_ropen = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'HE Shutter opened bit',
        readpv = 'SQ:NEUTRA:b4io1:HEopenRBV',
        lowlevel = True,
    ),
    he_rclose = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'HE Shutter closed bit',
        readpv = 'SQ:NEUTRA:b4io1:HEclosedRBV',
        lowlevel = True,
    ),
    he_renabled = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'HE Shutter enable bit',
        readpv = 'SQ:NEUTRA:b4io1:HEenabledRBV',
        lowlevel = True,
    ),
    he_popen = device('nicos.devices.generic.Pulse',
        description = 'HE Shutter opening pulse',
        moveable = 'he_sopen',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        lowlevel = True,
    ),
    he_pclose = device('nicos.devices.generic.Pulse',
        description = 'HE Shutter closing pulse',
        moveable = 'he_sclose',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        lowlevel = True,
    ),
    he_shutter = device('nicos_sinq.devices.niag_shutter.NiagShutter',
        description = 'HE shutter',
        do_open = 'he_popen',
        do_close = 'he_pclose',
        is_open = 'he_ropen',
        is_closed = 'he_rclose',
        is_enabled = 'he_renabled',
        mapping = {
            'open': [1, 0],
            'closed': [0, 1],
        },
        fallback = 'interstage',
        timeout = 60.0,
    ),

    #Fail save shutter FS
    fs_sopen = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = epics_timeout,
        description = 'FS Shutter opening bit',
        readpv = 'SQ:NEUTRA:b4io3:FSopen',
        writepv = 'SQ:NEUTRA:b4io3:FSopen',
        lowlevel = True,
    ),
    fs_sclose = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = epics_timeout,
        description = 'FS Shutter closing bit',
        readpv = 'SQ:NEUTRA:b4io3:FSclose',
        writepv = 'SQ:NEUTRA:b4io3:FSclose',
        lowlevel = True,
    ),
    fs_ropen = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'FS Shutter opened bit',
        readpv = 'SQ:NEUTRA:b4io1:FSopenRBV',
        lowlevel = True,
    ),
    fs_rclose = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'FS Shutter closed bit',
        readpv = 'SQ:NEUTRA:b4io1:FSclosedRBV',
        lowlevel = True,
    ),
    fs_renabled = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'FS Shutter enabled bit',
        readpv = 'SQ:NEUTRA:b4io1:FSenabledRBV',
        lowlevel = True,
    ),
    fs_popen = device('nicos.devices.generic.Pulse',
        description = 'FS Shutter opening pulse',
        moveable = 'fs_sopen',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        lowlevel = True,
    ),
    fs_pclose = device('nicos.devices.generic.Pulse',
        description = 'FS Shutter closing pulse',
        moveable = 'fs_sclose',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        lowlevel = True,
    ),
    fs_shutter = device('nicos_sinq.devices.niag_shutter.NiagShutter',
        description = 'Fail save (FS) shutter',
        do_open = 'fs_popen',
        do_close = 'fs_pclose',
        is_open = 'fs_ropen',
        is_closed = 'fs_rclose',
        is_enabled = 'fs_renabled',
        mapping = {
            'open': [1, 0],
            'closed': [0, 1],
        },
        fallback = 'interstage',
        timeout = 10.0,
    ),

    #Experimental shutter EXP
    ex_sopen = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = epics_timeout,
        description = 'EXP Shutter opening bit',
        readpv = 'SQ:NEUTRA:b4io4:EXPopen',
        writepv = 'SQ:NEUTRA:b4io4:EXPopen',
        lowlevel = True,
    ),
    ex_sclose = device('nicos.devices.epics.EpicsDigitalMoveable',
        epicstimeout = epics_timeout,
        description = 'EXP Shutter closing bit',
        readpv = 'SQ:NEUTRA:b4io4:EXPclose',
        writepv = 'SQ:NEUTRA:b4io4:EXPclose',
        lowlevel = True,
    ),
    ex_ropen = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'EXP Shutter opened bit',
        readpv = 'SQ:NEUTRA:b4io2:EXPopenRBV',
        lowlevel = True,
    ),
    ex_rclose = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'EXP Shutter closed bit',
        readpv = 'SQ:NEUTRA:b4io2:EXPclosedRBV',
        lowlevel = True,
    ),
    ex_renabled = device('nicos.devices.epics.EpicsReadable',
        epicstimeout = epics_timeout,
        description = 'EXP Shutter enabled bit',
        #readpv='SQ:NEUTRA:b4io2:EXPenabledRBV',
        readpv = 'SQ:NEUTRA:b5io2:EXPenabledRBV',
        lowlevel = True,
    ),
    ex_popen = device('nicos.devices.generic.Pulse',
        description = 'EXP Shutter opening pulse',
        moveable = 'ex_sopen',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        lowlevel = True,
    ),
    ex_pclose = device('nicos.devices.generic.Pulse',
        description = 'EXP Shutter closing pulse',
        moveable = 'ex_sclose',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        lowlevel = True,
    ),
    exp_shutter = device('nicos_sinq.devices.niag_shutter.NiagShutter',
        description = 'Experiment (EXP) shutter',
        do_open = 'ex_popen',
        do_close = 'ex_pclose',
        #do_fast='ex_pfast',
        #do_slow='ex_pslow',
        is_open = 'ex_ropen',
        is_closed = 'ex_rclose',
        is_enabled = 'ex_renabled',
        #is_fast='ex_rfast',
        mapping = {
            'open': [1, 0],
            'closed': [0, 1],
        },
        fallback = 'interstage',
        timeout = 10.0,
    ),
    fs_he_auto = device('nicos.devices.generic.manual.ManualSwitch',
        description =
        'Switch which decides if main shutters are managed automatically or manually',
        states = ['auto', 'manual'],
    ),
    exp_auto = device('nicos.devices.generic.manual.ManualSwitch',
        description =
        'Switch which decides if the experiment shutter is managed automatically or manually',
        states = ['auto', 'manual'],
    ),
    shuttersink = device('nicos_sinq.icon.devices.shuttersink.ShutterSink',
        description =
        'Sink which manages opening and closing shutters around scans',
        shutter1 = 'fs_shutter',
        shutter2 = 'he_shutter',
        auto = 'fs_he_auto'
    ),
)
