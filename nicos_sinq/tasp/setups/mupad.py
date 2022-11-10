description = 'Setup for MUPAD at TASP'

pvprefix = 'SQ:TASP:mupad:'

modules = ['nicos_sinq.tasp.commands.polmat']

devices = dict(
    i1 = device('nicos_sinq.tasp.devices.slsmagnet.SLSMagnet',
        epicstimeout = 3.0,
        description = 'Magnet 1',
        readpv = pvprefix + 'I1:CurRBV',
        writepv = pvprefix + 'I1:CurSet',
        wenable = pvprefix + 'I1:STATUS',
        renable = pvprefix + 'I1:STATUS_RBV',
        precision = .1,
        abslimits = (-20., 20.)
    ),
    i2 = device('nicos_sinq.tasp.devices.slsmagnet.SLSMagnet',
        epicstimeout = 3.0,
        description = 'Magnet 2',
        readpv = pvprefix + 'I2:CurRBV',
        writepv = pvprefix + 'I2:CurSet',
        abslimits = (-20., 20.),
        wenable = pvprefix + 'I2:STATUS',
        renable = pvprefix + 'I2:STATUS_RBV',
        precision = .1,
    ),
    i3 = device('nicos_sinq.tasp.devices.slsmagnet.SLSMagnet',
        epicstimeout = 3.0,
        description = 'Magnet 3',
        readpv = pvprefix + 'I3:CurRBV',
        writepv = pvprefix + 'I3:CurSet',
        abslimits = (-20., 20.),
        wenable = pvprefix + 'I3:STATUS',
        renable = pvprefix + 'I3:STATUS_RBV',
        precision = .1,
    ),
    i4 = device('nicos_sinq.tasp.devices.slsmagnet.SLSMagnet',
        epicstimeout = 3.0,
        description = 'Magnet 4',
        readpv = pvprefix + 'I4:CurRBV',
        writepv = pvprefix + 'I4:CurSet',
        abslimits = (-20., 20.),
        wenable = pvprefix + 'I4:STATUS',
        renable = pvprefix + 'I4:STATUS_RBV',
        precision = .1,
    ),
    i5 = device('nicos_sinq.tasp.devices.slsmagnet.SLSMagnet',
        epicstimeout = 3.0,
        description = 'Magnet 5',
        readpv = pvprefix + 'I5:CurRBV',
        writepv = pvprefix + 'I5:CurSet',
        abslimits = (-20., 20.),
        wenable = pvprefix + 'I5:STATUS',
        renable = pvprefix + 'I5:STATUS_RBV',
        precision = .1,
    ),
    i6 = device('nicos_sinq.tasp.devices.slsmagnet.SLSMagnet',
        epicstimeout = 3.0,
        description = 'Magnet 6',
        readpv = pvprefix + 'I6:CurRBV',
        writepv = pvprefix + 'I6:CurSet',
        abslimits = (-20., 20.),
        wenable = pvprefix + 'I6:STATUS',
        renable = pvprefix + 'I6:STATUS_RBV',
        precision = .1,
    ),
    i7 = device('nicos_ess.devices.epics.base.EpicsAnalogMoveableEss',
        epicstimeout = 3.0,
        description = 'Guide field',
        readpv = 'SQ:TASP:I7:CurRBV',
        writepv = 'SQ:TASP:I7:CurSet',
        abslimits = (-18., 18.)
    ),
    gufi = device('nicos_sinq.tasp.devices.gufi.GuideField',
        description = 'Guide field control',
        magnet = 'i7',
        hold_value = 1.2
    ),
    mupad = device('nicos_sinq.tasp.devices.mupad.Mupad',
        description = 'Mupad polarsiation device',
        i1 = 'i1',
        i2 = 'i2',
        i3 = 'i3',
        i4 = 'i4',
        mono = 'mono',
        ana = 'ana',
        a4 = 'a4'
    ),
    musw = device('nicos_sinq.tasp.devices.mupad.MuSwitch',
        description = 'Device to switch mupad by x, -x syntax',
        mupad = 'mupad'
    ),
    munumsw = device('nicos_sinq.tasp.devices.mupad.MuNumSwitch',
        description = 'Device to switch mupad 1, 2, 3 syntax',
        mupad = 'mupad'
    ),
)
