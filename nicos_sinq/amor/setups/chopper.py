description = 'Airbus chopper device in SINQ AMOR'

pvprefix = 'SQ:AMOR:chopper:'

devices = dict(
    ch1_speed = device('nicos_ess.devices.epics.base.EpicsAnalogMoveableEss',
        description = 'Speed of the master chopper',
        readpv = pvprefix + 'DCU1:Speed',
        writepv = pvprefix + 'DCU1:Speed:SP',
    ),
    ch1_position = device('nicos_ess.devices.epics.base.EpicsReadableEss',
        description = 'Position of the master chopper',
        readpv = pvprefix + 'DCU1:Position',
    ),
    ch1_flags = device('nicos_ess.devices.epics.base.EpicsReadableEss',
        description = 'Flags of the master chopper',
        readpv = pvprefix + 'DCU1:Flags',
        fmtstr = '%d',
        lowlevel = True
    ),
    ch1_state = device('nicos_ess.devices.epics.base.EpicsStringReadableEss',
        description = 'State of the master chopper',
        readpv = pvprefix + 'DCU1:State',
    ),
    ch1_motor_temperature = device('nicos_ess.devices.epics.base.EpicsReadableEss',
        description = 'Motor temperature of the master chopper',
        readpv = pvprefix + 'DCU1:MotorTemp',
        lowlevel = True
    ),
    ch1_drive_temperature = device('nicos_ess.devices.epics.base.EpicsReadableEss',
        description = 'Drive temperature of the master chopper',
        readpv = pvprefix + 'DCU1:DriveTemp',
        lowlevel = True
    ),
    ch1_command = device('nicos.devices.epics.EpicsStringMoveable',
        description = 'Command to the master chopper',
        readpv = pvprefix + 'DCU1:Command:SP',
        writepv = pvprefix + 'DCU1:Command:SP',
        lowlevel = True
    ),
    ch2_speed = device('nicos_ess.devices.epics.base.EpicsReadableEss',
        description = 'Speed of the master chopper',
        readpv = pvprefix + 'DCU2:Speed',
    ),
    ch2_position = device('nicos_ess.devices.epics.base.EpicsAnalogMoveableEss',
        description = 'Position of the master chopper',
        readpv = pvprefix + 'DCU2:Position',
        writepv = pvprefix + 'DCU2:Position:SP',
    ),
    ch2_gear_ratio = device('nicos_ess.devices.epics.base.EpicsDigitalMoveableEss',
        description = 'Position of the master chopper',
        readpv = pvprefix + 'DCU2:GearRatio',
        writepv = pvprefix + 'DCU2:GearRatio:SP',
    ),
    ch2_flags = device('nicos_ess.devices.epics.base.EpicsReadableEss',
        description = 'Flags of the master chopper',
        readpv = pvprefix + 'DCU2:Flags',
        fmtstr = '%d',
        lowlevel = True
    ),
    ch2_state = device('nicos_ess.devices.epics.base.EpicsStringReadableEss',
        description = 'State of the master chopper',
        readpv = pvprefix + 'DCU2:State',
    ),
    ch2_motor_temperature = device('nicos_ess.devices.epics.base.EpicsReadableEss',
        description = 'Motor temperature of the master chopper',
        readpv = pvprefix + 'DCU2:MotorTemp',
        lowlevel = True
    ),
    ch2_drive_temperature = device('nicos_ess.devices.epics.base.EpicsReadableEss',
        description = 'Drive temperature of the master chopper',
        readpv = pvprefix + 'DCU2:DriveTemp',
        lowlevel = True
    ),
    ch2_command = device('nicos.devices.epics.EpicsStringMoveable',
        description = 'Command to the master chopper',
        readpv = pvprefix + 'DCU2:Command:SP',
        writepv = pvprefix + 'DCU2:Command:SP',
        lowlevel = True
    ),
)
