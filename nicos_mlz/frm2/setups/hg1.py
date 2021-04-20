description = 'Humidity generator for SANS humidity cell'

group = 'plugplay'

tango_base = 'tango://%s:10000/box/' % setupname

devices = {
    'T_%s_heater' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'Temperature of heater',
        tangodevice = tango_base + 'heater/control',
        fmtstr = '%.1f',
        unit = 'degC',
        timeout = 600.0,
        precision = 0.2,
    ),
    'T_%s_julabo' % setupname: device('nicos.devices.entangle.TemperatureController',
        description = 'Temperature of Julabo',
        tangodevice = tango_base + 'julabo/control',
        fmtstr = '%.1f',
        unit = 'degC',
        timeout = 600.0,
        precision = 0.2,
    ),
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
        unit = '%',
        timeout = 600.0,
        precision = 1,
    ),
    'T_%s_cell' % setupname: device('nicos.devices.entangle.Sensor',
        description = 'Temperature in humidity cell',
        tangodevice = tango_base + 'mhg/temperature',
        fmtstr = '%.1f',
        unit = 'degC',
    ),
}
