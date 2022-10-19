description = 'Julabo F25HL'

pv_root = 'E04:JULABOF25HL-001:'

devices = dict(
    T_julabo_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The temperature',
        readpv='{}TEMP'.format(pv_root),
        writepv='{}TEMP:SP1'.format(pv_root),
        targetpv='{}TEMP:SP1:RBV'.format(pv_root),
        abslimits=(-1e308, 1e308),
    ),
    julabo_mode_001=device(
        'nicos.devices.epics.pva.EpicsMappedMoveable',
        description='The status',
        readpv='{}MODE'.format(pv_root),
        writepv='{}MODE:SP'.format(pv_root),
        mapping={
            'OFF': 0,
            'ON': 1
        },
    ),
    T_julabo_external_001=device(
        'nicos.devices.epics.pva.EpicsReadable',
        description='The external sensor temperature',
        readpv='{}EXTT'.format(pv_root),
    ),
    julabo_external_enabled_001=device(
        'nicos.devices.epics.pva.EpicsMappedMoveable',
        description='Use external or internal sensor',
        readpv='{}EXTSENS'.format(pv_root),
        writepv='{}EXTSENS:SP'.format(pv_root),
        mapping={
            'Internal': 0,
            'External': 1
        },
    ),
    julabo_internal_P_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The internal P value',
        readpv='{}INTP'.format(pv_root),
        writepv='{}INTP:SP'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_internal_I_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The internal I value',
        readpv='{}INTI'.format(pv_root),
        writepv='{}INTI:SP'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_internal_D_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The internal D value',
        readpv='{}INTD'.format(pv_root),
        writepv='{}INTD:SP'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_safety_001=device(
        'nicos.devices.epics.pva.EpicsReadable',
        description='The safety sensor temperature',
        readpv='{}TSAFE'.format(pv_root),
        visibility=(),
    ),
    julabo_max_cooling_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The maximum cooling power %',
        readpv='{}MAX:COOL:RBV'.format(pv_root),
        writepv='{}MAX:COOL'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_max_heating_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The maximum heating power %',
        readpv='{}MAX:HEAT:RBV'.format(pv_root),
        writepv='{}MAX:HEAT'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_heating_power_001=device(
        'nicos.devices.epics.pva.EpicsReadable',
        description='The heating power being used %',
        readpv='{}POWER'.format(pv_root),
        visibility=(),
    ),
    julabo_internal_slope_001=device(
        'nicos.devices.epics.pva.EpicsReadable',
        description='The internal slope',
        readpv='{}SI:SLOPE:RBV'.format(pv_root),
        visibility=(),
    ),
    julabo_external_P_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The internal P value',
        readpv='{}EXTP'.format(pv_root),
        writepv='{}EXTP:SP'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_external_I_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The internal I value',
        readpv='{}EXTI'.format(pv_root),
        writepv='{}EXTI:SP'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_external_D_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The internal D value',
        readpv='{}EXTD'.format(pv_root),
        writepv='{}EXTD:SP'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_high_limit_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The high temp warning limit',
        readpv='{}HILIMIT'.format(pv_root),
        writepv='{}HILIMIT:SP'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_low_limit_001=device(
        'nicos.devices.epics.pva.EpicsAnalogMoveable',
        description='The low temp warning limit',
        readpv='{}LOWLIMIT'.format(pv_root),
        writepv='{}LOWLIMIT:SP'.format(pv_root),
        visibility=(),
        abslimits=(-1e308, 1e308),
    ),
    julabo_status_001=device(
        'nicos.devices.epics.pva.EpicsReadable',
        description='The status',
        readpv='{}STATUS'.format(pv_root),
        visibility=(),
    ),
    julabo_version_001=device(
        'nicos.devices.epics.pva.EpicsStringReadable',
        description='The software version',
        readpv='{}VERSION'.format(pv_root),
        visibility=(),
    ),
)
