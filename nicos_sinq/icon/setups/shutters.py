description = 'ICON shutters (HE, FS, Exp)'

group = 'lowlevel'

display_order = 10

sysconfig = dict(datasinks = [
    'shuttersink',
])

devices = dict(
    #Main Shutter HE
    he_sopen = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        description = 'HE Shutter opening bit',
        readpv = 'SQ:ICON:b4io3:HEopen',
        writepv = 'SQ:ICON:b4io3:HEopen',
        visibility = (),
    ),
    he_sclose = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        description = 'HE Shutter closing bit',
        readpv = 'SQ:ICON:b4io3:HEclose',
        writepv = 'SQ:ICON:b4io3:HEclose',
        visibility = (),
    ),
    he_ropen = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'HE Shutter opened bit',
        readpv = 'SQ:ICON:b4io1:HEopenRBV',
        visibility = (),
    ),
    he_rclose = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'HE Shutter closed bit',
        readpv = 'SQ:ICON:b4io1:HEcloseRBV',
        visibility = (),
    ),
    he_renabled = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'HE Shutter enable bit',
        readpv = 'SQ:ICON:b4io1:HEenabledRBV',
        visibility = (),
    ),
    he_popen = device('nicos.devices.generic.Pulse',
        description = 'HE Shutter opening pulse',
        moveable = 'he_sopen',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        visibility = (),
    ),
    he_pclose = device('nicos.devices.generic.Pulse',
        description = 'HE Shutter closing pulse',
        moveable = 'he_sclose',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        visibility = (),
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
    fs_sopen = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        description = 'FS Shutter opening bit',
        readpv = 'SQ:ICON:b4io3:FSopen',
        writepv = 'SQ:ICON:b4io3:FSopen',
        visibility = (),
    ),
    fs_sclose = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        description = 'FS Shutter closing bit',
        readpv = 'SQ:ICON:b4io3:FSclose',
        writepv = 'SQ:ICON:b4io3:FSclose',
        visibility = (),
    ),
    fs_ropen = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'FS Shutter opened bit',
        readpv = 'SQ:ICON:b4io1:FSopenRBV',
        visibility = (),
    ),
    fs_rclose = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'FS Shutter closed bit',
        readpv = 'SQ:ICON:b4io1:FScloseRBV',
        visibility = (),
    ),
    fs_renabled = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'FS Shutter enabled bit',
        readpv = 'SQ:ICON:b4io1:FSenabledRBV',
        visibility = (),
    ),
    fs_popen = device('nicos.devices.generic.Pulse',
        description = 'FS Shutter opening pulse',
        moveable = 'fs_sopen',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        visibility = (),
    ),
    fs_pclose = device('nicos.devices.generic.Pulse',
        description = 'FS Shutter closing pulse',
        moveable = 'fs_sclose',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        visibility = (),
    ),
    fs_shutter = device('nicos_sinq.devices.niag_shutter.NiagShutter',
        description = 'FS shutter',
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
    exp_sopen = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        description = 'EXP Shutter opening bit',
        readpv = 'SQ:ICON:b4io4:EXPopen',
        writepv = 'SQ:ICON:b4io4:EXPopen',
        visibility = (),
    ),
    exp_sclose = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        description = 'EXP Shutter closing bit',
        readpv = 'SQ:ICON:b4io4:EXPclose',
        writepv = 'SQ:ICON:b4io4:EXPclose',
        visibility = (),
    ),
    exp_sslow = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        description = 'EXP Shutter set slow bit',
        readpv = 'SQ:ICON:b4io4:EXPslow',
        writepv = 'SQ:ICON:b4io4:EXPslow',
        visibility = (),
    ),
    exp_sfast = device('nicos_sinq.devices.epics.EpicsDigitalMoveable',
        description = 'EXP Shutter set fast bit',
        readpv = 'SQ:ICON:b4io4:EXPfast',
        writepv = 'SQ:ICON:b4io4:EXPfast',
        visibility = (),
    ),
    exp_ropen = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'EXP Shutter opened bit',
        readpv = 'SQ:ICON:b4io2:EXPopenRBV',
        visibility = (),
    ),
    exp_rclose = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'EXP Shutter closed bit',
        readpv = 'SQ:ICON:b4io2:EXPclosedRBV',
        visibility = (),
    ),
    exp_renabled = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'EXP Shutter enabled bit',
        #readpv='SQ:ICON:b4io2:EXPenabledRBV',
        readpv = 'SQ:ICON:b4io2:EXPenabledRBV',
        visibility = (),
    ),
    exp_rfast = device('nicos_sinq.devices.epics.EpicsReadable',
        description = 'EXP Shutter fast bit',
        readpv = 'SQ:ICON:b4io2:EXPfastRBV',
        visibility = (),
    ),
    exp_popen = device('nicos.devices.generic.Pulse',
        description = 'EXP Shutter opening pulse',
        moveable = 'exp_sopen',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        visibility = (),
    ),
    exp_pclose = device('nicos.devices.generic.Pulse',
        description = 'EXP Shutter closing pulse',
        moveable = 'exp_sclose',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        visibility = (),
    ),
    exp_pslow = device('nicos.devices.generic.Pulse',
        description = 'EXP Shutter set slow pulse',
        moveable = 'exp_sslow',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        visibility = (),
    ),
    exp_pfast = device('nicos.devices.generic.Pulse',
        description = 'EXP Shutter set fast pulse',
        moveable = 'exp_sfast',
        onvalue = 1,
        offvalue = 0,
        ontime = 0.1,
        visibility = (),
    ),
    exp_shutter = device('nicos_sinq.devices.niag_shutter.NiagExpShutter',
        description = 'EXP shutter',
        do_open = 'exp_popen',
        do_close = 'exp_pclose',
        do_fast = 'exp_pfast',
        do_slow = 'exp_pslow',
        is_open = 'exp_ropen',
        is_closed = 'exp_rclose',
        is_enabled = 'exp_renabled',
        is_fast = 'exp_rfast',
        mapping = {
            'open': [1, 0],
            'closed': [0, 1],
        },
        fallback = 'interstage',
        timeout = 10.0,
        fast = False,
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
        shutter1 = 'he_shutter',
        shutter2 = 'fs_shutter',
        auto = 'fs_he_auto'
    ),
)
