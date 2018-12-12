description = 'setup for Oxford 8T magnet'

group = 'plugplay'
tango_base = 'tango://jvm2:10000/box/'

includes = ['alias_T', 'alias_B', 'alias_sth']

devices = dict(
    sth_jvm2 = device('nicos_mlz.jcns.devices.motor.Motor',
        description = 'sample rotation motor',
        tangodevice = tango_base + 'motor/motx',
        fmtstr = '%.3f',
        precision = 0.002,
    ),
    stz_jvm2 = device('nicos_mlz.jcns.devices.motor.Motor',
        description = 'sample height motor',
        tangodevice = tango_base + 'motor/motz',
        fmtstr = '%.3f',
        precision = 0.01,
    ),
    T_jvm2_vti = device('nicos.devices.tango.TemperatureController',
        description = 'temperature control of the VTI',
        tangodevice = tango_base + 'itc2/vti_ctrl',
    ),
    T_jvm2_stick = device('nicos.devices.tango.TemperatureController',
        description = 'temperature control of the low-temperature sample stick',
        tangodevice = tango_base + 'itc2/lt_stick_ctrl',
    ),
    T_jvm2_htstick = device('nicos.devices.tango.TemperatureController',
        description = 'temperature control of the high-temperature sample stick',
        tangodevice = tango_base + 'itc2/ht_stick_ctrl',
    ),
    jvm2_vti_heater = device('nicos.devices.tango.AnalogOutput',
        description = 'heater setting for VTI',
        tangodevice = tango_base + 'itc2/vti_heater',
    ),
    jvm2_vti_nv = device('nicos.devices.tango.AnalogOutput',
        description = 'needle valve opening for VTI',
        tangodevice = tango_base + 'itc2/needlevalve',
    ),
    jvm2_stick_heater = device('nicos.devices.tango.AnalogOutput',
        description = 'heater setting for the sample stick',
        tangodevice = tango_base + 'itc2/lt_stick_heater',
    ),
    jvm2_htstick_heater = device('nicos.devices.tango.AnalogOutput',
        description = 'heater setting for the HT sample stick',
        tangodevice = tango_base + 'itc2/ht_stick_heater',
    ),
#    T_jvm2_sample_vtireg = device('nicos.devices.tango.TemperatureController',
#        description = 'temperature control of VTI heater using stick sensor',
#        tangodevice = tango_base + 'itc2/cross_regulation',
#    ),
    B_jvm2 = device('nicos.devices.tango.Actuator',
        description = 'magnetic field',
        tangodevice = tango_base + 'ips/field',
        precision = 0.001,
    ),
    jvm2_Bhall = device('nicos.devices.tango.Sensor',
        description = 'Hall probe measuring field in main coils',
        tangodevice = tango_base + 'ips/hallprobe',
    ),
    I_jvm2_supply = device('nicos.devices.tango.AnalogInput',
        description = 'actual current output of power supplies',
        tangodevice = tango_base + 'ips/current',
    ),
    jvm2_vti_regulation = device('nicos.devices.tango.NamedDigitalOutput',
        description = 'heater setting for VTI',
        tangodevice = tango_base + 'itc2/vti_regulation',
        mapping = dict(none = 0, heater = 1, valve = 2, both = 3),
    ),
    jvm2_Tmag = device('nicos.devices.tango.Sensor',
        description = 'temperature of magnet coils',
        tangodevice = tango_base + 'ips/temp',
    ),
    jvm2_pdewar = device('nicos.devices.tango.TemperatureController',
        description = 'He pressure in dewar',
        tangodevice = tango_base + 'itc/condenser_pressure',
    ),
    jvm2_Tcoldhead = device('nicos.devices.tango.Sensor',
        description = 'temperature of recondenser coldhead',
        tangodevice = tango_base + 'itc/condenser_temp',
    ),
    jvm2_Urecon = device('nicos.devices.tango.Sensor',
        description = 'current applied at recondenser',
        tangodevice = tango_base + 'itc/u_recon',
    ),
    jvm2_LHe = device('nicos.devices.tango.Sensor',
        description = 'liquid helium level',
        tangodevice = tango_base + 'ips/level',
    ),
    jvm2_LHe_fastmode = device('nicos.devices.tango.NamedDigitalOutput',
        description = 'liquid helium level mode',
        tangodevice = tango_base + 'ips/level_fastmode',
        mapping = dict(on = 1, off = 0),
    ),
    jvm2_LN2 = device('nicos.devices.tango.Sensor',
        description = 'liquid nitrogen level',
        tangodevice = tango_base + 'itc/nitrogen_level',
    ),
)

alias_config = {
    'T': {'T_jvm2_vti': 220, 'T_jvm2_stick': 210, 'T_jvm2_htstick': 210},
    'Ts': {'T_jvm2_stick': 120, 'T_jvm2_htstick': 120},
    'B': {'B_jvm2': 100},
    'sth': {'sth_jvm2': 200},
}

extended = dict(
    representative = 'B_jvm2',
)
