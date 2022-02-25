description = 'Oxford vertical 8T magnet with He recondenser'

group = 'plugplay'
tango_base = 'tango://%s:10000/box/' % setupname

includes = ['alias_T', 'alias_B', 'alias_sth']

devices = {
    'sth_%s' % setupname: device('nicos.devices.entangle.MotorAxis',
        description = 'sample rotation motor',
        tangodevice = tango_base + 'motor/motx',
        fmtstr = '%.3f',
        precision = 0.002,
    ),
    'sth_%s_ax' % setupname: device('nicos.devices.generic.Axis',
        description = 'sample rotation motor, with backlash correction',
        motor = 'sth_%s' % setupname,
        fmtstr = '%.3f',
        abslimits = (-360, 360),
        precision = 0.002,
        backlash = -1.0,
    ),
    'stz_%s' % setupname: device('nicos.devices.entangle.MotorAxis',
        description = 'sample height motor',
        tangodevice = tango_base + 'motor/motz',
        fmtstr = '%.3f',
        precision = 0.01,
    ),
    'T_%s_vti' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'temperature control of the VTI',
        tangodevice = tango_base + 'itc2/vti_ctrl',
    ),
    'T_%s_stick' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'temperature control of the low-temperature sample stick',
        tangodevice = tango_base + 'itc2/lt_stick_ctrl',
    ),
    'T_%s_htstick' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'temperature control of the high-temperature sample stick',
        tangodevice = tango_base + 'itc2/ht_stick_ctrl',
    ),
    '%s_vti_heater' % setupname: device('nicos.devices.entangle.AnalogOutput',
        description = 'heater setting for VTI',
        tangodevice = tango_base + 'itc2/vti_heater',
    ),
    '%s_vti_nv' % setupname: device('nicos.devices.entangle.AnalogOutput',
        description = 'needle valve opening for VTI',
        tangodevice = tango_base + 'itc2/needlevalve',
    ),
    '%s_stick_heater' % setupname: device('nicos.devices.entangle.AnalogOutput',
        description = 'heater setting for the sample stick',
        tangodevice = tango_base + 'itc2/lt_stick_heater',
    ),
    '%s_htstick_heater' % setupname: device('nicos.devices.entangle.AnalogOutput',
        description = 'heater setting for the HT sample stick',
        tangodevice = tango_base + 'itc2/ht_stick_heater',
    ),
#    'T_%s_sample_vtireg' % setupname: device('nicos.devices.entangle.TemperatureController',
#        description = 'temperature control of VTI heater using stick sensor',
#        tangodevice = tango_base + 'itc2/cross_regulation',
#    ),
    'B_%s' % setupname: device('nicos.devices.entangle.Actuator',
        description = 'magnetic field',
        tangodevice = tango_base + 'ips/field',
        precision = 0.001,
    ),
    '%s_Bhall' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'Hall probe measuring field in main coils',
        tangodevice = tango_base + 'ips/hallprobe',
    ),
    'I_%s_supply' % setupname: device('nicos.devices.entangle.AnalogInput',
        description = 'actual current output of power supplies',
        tangodevice = tango_base + 'ips/current',
    ),
    '%s_vti_regulation' % setupname: device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'automatic regulation type for VTI temperature control',
        tangodevice = tango_base + 'itc2/vti_regulation',
        mapping = dict(none = 0, heater = 1, valve = 2, both = 3),
    ),
    '%s_pvti' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'He pressure in VTI',
        tangodevice = tango_base + 'itc2/vti_pressure',
    ),
    '%s_Tmag' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'temperature of top magnet coil',
        tangodevice = tango_base + 'ips/temp',
    ),
    '%s_pdewar' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'He pressure in dewar',
        tangodevice = tango_base + 'itc/condenser_pressure',
    ),
    '%s_Tcoldhead' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'temperature of recondenser coldhead',
        tangodevice = tango_base + 'itc/condenser_temp',
    ),
    '%s_Urecon' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'current applied at recondenser',
        tangodevice = tango_base + 'itc/u_recon',
    ),
    '%s_LHe' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'liquid helium level',
        tangodevice = tango_base + 'ips/level',
    ),
    '%s_LHe_fastmode' % setupname: device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'liquid helium level mode',
        tangodevice = tango_base + 'ips/level_fastmode',
        mapping = dict(on = 1, off = 0),
    ),
    '%s_LN2' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'liquid nitrogen level',
        tangodevice = tango_base + 'itc/nitrogen_level',
    ),
    '%s_gas_switch' % setupname : device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Switch for the gas valve',
        tangodevice = tango_base + 'leybold/gas',
        mapping = {'on': 1, 'off': 0},
    ),
    '%s_vacuum_switch' % setupname : device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Switch for the vacuum valve',
        tangodevice = tango_base + 'leybold/vacuum',
        mapping = {'on': 1, 'off': 0},
    ),
    '%s_psample' % setupname : device('nicos.devices.entangle.AnalogInput',
        description = 'Pressure in sample space',
        tangodevice = tango_base + 'leybold/sensor',
        fmtstr = '%.3g',
        unit = 'mbar',
    ),
    '%s_shutdown' % setupname : device('nicos.devices.entangle.DigitalInput',
        description = 'Heater shutdown due to overheat',
        tangodevice = tango_base + 'heater/monitor',
    ),
}

alias_config = {
    'T': {'T_%s_vti' % setupname: 220, 'T_%s_stick' % setupname: 210,
          'T_%s_htstick' % setupname: 210},
    'Ts': {'T_%s_stick' % setupname: 120, 'T_%s_htstick' % setupname: 120},
    'B': {'B_%s' % setupname: 100},
    'sth': {'sth_%s_ax' % setupname: 250, 'sth_%s' % setupname: 200},
}

extended = dict(
    representative = 'B_%s' % setupname,
)

watch_conditions = [
    dict(condition = 'ccm8v_lhe_value < 30',
         type = 'se',
         setup = 'ccm8v',
         message = '8T Magnet: He level below 30%',
        ),
    dict(condition = 'ccm8v_shutdown_value > 0',
         type = 'se',
         setup = 'ccm8v',
         message = '8T Magnet: Heaters shut down due to overheat',
        ),
]
