description = 'The PACE5000 in the ESSIIP-lab.'

pv_root = 'SES-PREMP:Pctrl-PACE5000-01:'

devices = dict(
    pace_setpoint=device(
        'nicos.devices.epics.EpicsAnalogMoveable',
        description='The pressure set-point',
        readpv='{}Setpoint_RBV'.format(pv_root),
        writepv='{}Setpoint'.format(pv_root),
    ),
    pace_pressure=device(
        'nicos.devices.epics.EpicsReadable',
        description='The current pressure',
        readpv='{}Pressure_RBV'.format(pv_root),
    ),
    pace_effort=device(
        'nicos.devices.epics.EpicsReadable',
        description='The current effort',
        readpv='{}Effort_RBV'.format(pv_root),
    ),
    pace_vent=device(
        'nicos_ess.devices.epics.extensions.EpicsMappedMoveable',
        description='The vent status',
        readpv='{}Vent_RBV'.format(pv_root),
        writepv='{}Vent'.format(pv_root),
        visibility=(),
        mapping={
            'Vent OK': 0,
            'Vent in progress': 1,
            'Vent complete': 2,
        },
    ),
    pace_slew=device(
        'nicos.devices.epics.EpicsAnalogMoveable',
        description='The current slew',
        readpv='{}Slew_RBV'.format(pv_root),
        writepv='{}Slew'.format(pv_root),
        visibility=(),
    ),
    pace_slew_mode=device(
        'nicos_ess.devices.epics.extensions.EpicsMappedMoveable',
        description='The slew mode',
        readpv='{}SlewMode_RBV'.format(pv_root),
        writepv='{}SlewMode'.format(pv_root),
        visibility=(),
        mapping={
            'MAX': 0,
            'LIN': 1,
        },
    ),
)
