description = 'JCNS humidity generator'

group = 'plugplay'

tango_base = 'tango://%s:10000/box/' % setupname

devices = {
    '%s_flowrate' % setupname: device('nicos.devices.entangle.WindowTimeoutAO',
        description = 'Flow rate through humidity cell',
        tangodevice = tango_base + 'mhg/flowrate',
        fmtstr = '%.1f',
        unit = 'ml',
        timeout = 600.0,
        precision = 0.2,
    ),
    '%s_humidity' % setupname: device('nicos.devices.entangle.WindowTimeoutAO',
        description = 'Humidity in humidity cell',
        tangodevice = tango_base + 'mhg/humidity',
        fmtstr = '%.1f',
        unit = '%rH',
        timeout = 600.0,
        precision = 1,
    ),
    'T_%s_cell' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'Temperature in humidity cell',
        tangodevice = tango_base + 'mhg/temperature',
        fmtstr = '%.1f',
        unit = 'degC',
    ),
    '%s_standby' % setupname: device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Switches standby mode on and off',
        tangodevice = tango_base + 'mhg/standby',
        mapping = {'on': 1, 'off': 0},
    ),
}
