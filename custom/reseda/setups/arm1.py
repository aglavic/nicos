#  -*- coding: utf-8 -*-

description = 'Arm 1 (NRSE)'
group = 'optional'

taco_base = '//resedasrv.reseda.frm2/reseda'
tango_base = 'tango://resedahw2.reseda.frm2:10000/reseda'

devices = dict(
    arm1_fg_frequency = device('nicos.devices.tango.AnalogOutput',
        description = 'Frequency Generator Arm 1 (Frequency)',
        tangodevice = '%s/arm1/fg_frequency' % tango_base,
    ),
    arm1_fg_amplitude = device('nicos.devices.tango.AnalogOutput',
        description = 'Frequency Generator Arm 1 (Amplitude)',
        tangodevice = '%s/arm1/fg_amplitude' % tango_base,
    ),
    arm1_fg_burst = device('nicos.devices.tango.DigitalOutput',
        description = 'Frequency Generator Arm 1 (Burst)',
        tangodevice = '%s/arm1/fg_burst' % tango_base,
    ),
    arm1_rot_mot = device('nicos.devices.tango.Motor',
        description = 'Rotation arm 1 (motor)',
        tangodevice = '%s/arm1/2theta' % tango_base,
        fmtstr = '%.3f',
        lowlevel = True,
    ),
    arm1_rot_enc = device('nicos.devices.taco.Coder',
        description = 'Rotation arm 1 (encoder)',
        tacodevice = '%s/enc/arm1' % taco_base,
        fmtstr = '%.3f',
        lowlevel = True,
    ),
    arm1_rot_air = device('nicos.devices.tango.DigitalOutput',
        description = 'Rotation arm 1 (air)',
        tangodevice = '%s/iobox/plc_air_a1' % tango_base,
        fmtstr = '%.3f',
        lowlevel = True,
    ),
    arm1_rot = device('mira.axis.HoveringAxis',
        description = 'Rotation arm 1',
        motor = 'arm1_rot_mot',
        coder = 'arm1_rot_enc',
        switch = 'arm1_rot_air',
        startdelay = 2.0,
        stopdelay = 2.0,
        fmtstr = '%.3f',
        precision = 0.01,
    ),
    T_arm1_coil1 = device('nicos.devices.tango.AnalogInput',
        description = 'Arm 1 coil 1 temperature',
        tangodevice = '%s/iobox/plc_t_arm1coil1' % tango_base,
        fmtstr = '%.3f',
    ),
    T_arm1_coil2 = device('nicos.devices.tango.AnalogInput',
        description = 'Arm 1 coil 2 temperature',
        tangodevice = '%s/iobox/plc_t_arm1coil2' % tango_base,
        fmtstr = '%.3f',
    ),
    T_arm1_coil3 = device('nicos.devices.tango.AnalogInput',
        description = 'Arm 1 coil 3 temperature',
        tangodevice = '%s/iobox/plc_t_arm1coil3' % tango_base,
        fmtstr = '%.3f',
    ),
    T_arm1_coil4 = device('nicos.devices.tango.AnalogInput',
        description = 'Arm 1 coil 4 temperature',
        tangodevice = '%s/iobox/plc_t_arm1coil4' % tango_base,
        fmtstr = '%.3f',
    ),
)
