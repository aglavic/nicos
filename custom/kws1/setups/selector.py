#  -*- coding: utf-8 -*-

description = 'setup for the velocity selector'
group = 'lowlevel'

excludes = ['virtual_selector']

tango_base = 'tango://phys.kws1.frm2:10000/kws1/'

SELECTOR_PRESETS = {
    '5A':  dict(lam=5,  speed=26730.0),
    '6A':  dict(lam=6,  speed=22275.0),
    '7A':  dict(lam=7,  speed=19092.6),
    '8A':  dict(lam=8,  speed=16706.4),
    '10A': dict(lam=10, speed=13365.0),
    '12A': dict(lam=12, speed=11137.2),
}

devices = dict(
    selector        = device('devices.generic.MultiSwitcher',
                             description = 'select selector presets',
                             moveables = ['selector_speed'],
                             mapping = dict((k, [v['speed']])
                                            for (k, v) in SELECTOR_PRESETS.items()),
                             precision = [10.0],
                            ),

    selector_speed  = device('devices.tango.WindowTimeoutAO',
                             description = 'Selector speed control',
                             tangodevice = tango_base + 'selector/speed',
                             unit = 'rpm',
                             fmtstr = '%.0f',
                             warnlimits = (11000, 27000),
                             abslimits = (11000, 27000),
                             precision = 10,
                            ),

    selector_lambda = device('kws1.selector.SelectorLambda',
                             description = 'Selector wavelength control',
                             seldev = 'selector_speed',
                             unit = 'A',
                             fmtstr = '%.2f',
                             constant = 2227.5,
                            ),

    selector_rtemp  = device('devices.tango.AnalogInput',
                             description = 'Temperature of the selector rotor',
                             tangodevice = tango_base + 'selector/rotortemp',
                             unit = 'degC',
                             fmtstr = '%.1f',
                             warnlimits = (10, 40),
                            ),
    selector_winlt  = device('devices.tango.AnalogInput',
                             description = 'Cooling water temperature at inlet',
                             tangodevice = tango_base + 'selector/waterintemp',
                             unit = 'degC',
                             fmtstr = '%.1f',
                             warnlimits = (15, 22),
                            ),
    selector_woutt  = device('devices.tango.AnalogInput',
                             description = 'Cooling water temperature at outlet',
                             tangodevice = tango_base + 'selector/waterouttemp',
                             unit = 'degC',
                             fmtstr = '%.1f',
                             warnlimits = (15, 26),
                            ),
    selector_wflow  = device('devices.tango.AnalogInput',
                             description = 'Cooling water flow rate through selector',
                             tangodevice = tango_base + 'selector/flowrate',
                             unit = 'l/min',
                             fmtstr = '%.1f',
                             warnlimits = (1.0, 10),
                            ),
    selector_vacuum = device('devices.tango.AnalogInput',
                             description = 'Vacuum in the selector',
                             tangodevice = tango_base + 'selector/vacuum',
                             unit = 'mbar',
                             fmtstr = '%.5f',
                             warnlimits = (0, 0.02),
                            ),
    selector_vibrt  = device('devices.tango.AnalogInput',
                             description = 'Selector vibration',
                             tangodevice = tango_base + 'selector/vibration',
                             unit = 'mm/s',
                             fmtstr = '%.2f',
                             warnlimits = (0, 0.6),
                            ),
)
