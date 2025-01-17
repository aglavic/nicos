description = 'Setup for the portable optics assembly.'

pvprefix = 'SQ:BOA:optics:'
devices = dict(
    optics_z = device('nicos_ess.devices.epics.motor.EpicsMonitorMotor',
        description = 'Z-motor',
        motorpv = f'{pvprefix}m1',
        #              errormsgpv=f'{pvprefix}m1-MsgTxt',
    ),
    optics_lin = device('nicos_ess.devices.epics.motor.EpicsMonitorMotor',
        description = 'linear stage',
        motorpv = f'{pvprefix}m2',
        #              errormsgpv=f'{pvprefix}m2-MsgTxt',
    ),
    optics_rot = device('nicos_ess.devices.epics.motor.EpicsMonitorMotor',
        description = 'rotation stage',
        motorpv = f'{pvprefix}m3',
        #              errormsgpv=f'{pvprefix}m3-MsgTxt',
    ),
)
