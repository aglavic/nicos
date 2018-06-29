# -*- coding: utf-8 -*-

description = 'Selector area setup'
group = 'lowlevel'
display_order = 20

excludes = ['virtual_selector']

sel_presets = configdata('config_selector.SELECTOR_PRESETS')

tango_base = 'tango://phys.kws3.frm2:10000/kws3/'

# TODO (later): add sel_rot to switcher devices
devices = dict(
    selector = device('nicos.devices.generic.MultiSwitcher',
        description = 'select selector presets',
        blockingmove = False,
        moveables = ['sel_lambda'],
        mapping = {k: [v['lam']] for (k, v) in sel_presets.items()},
        fallback = 'unknown',
        precision = [0.05],
    ),

    sel_speed_valid = device('nicos.devices.tango.DigitalOutput',
        tangodevice = tango_base + 'fzjdp_digital/sel_speed_valid',
        lowlevel = True,
    ),
    sel_speed_status = device('nicos.devices.tango.DigitalInput',
        tangodevice = tango_base + 'fzjdp_digital/sel_speed_status',
        lowlevel = True,
    ),
    sel_speed_set = device('nicos.devices.tango.AnalogOutput',
        tangodevice = tango_base + 'fzjdp_analog/sel_speed_set',
        abslimits = (60, 300),
        lowlevel = True,
    ),
    sel_speed_read = device('nicos.devices.tango.AnalogInput',
        tangodevice = tango_base + 'fzjdp_analog/sel_speed_read',
        lowlevel = True,
    ),

    sel_speed = device('nicos_mlz.kws3.devices.selector.SelectorSpeed',
        description = 'selector speed',
        valid = 'sel_speed_valid',
        speedset = 'sel_speed_set',
        speedread = 'sel_speed_read',
        status = 'sel_speed_status',
        abslimits = (60, 300),
        precision = 0.5,
        unit = 'Hz',
    ),

    sel_lambda = device('nicos_mlz.kws1.devices.selector.SelectorLambda',
        description = 'Selector wavelength control',
        seldev = 'sel_speed',
        unit = 'A',
        fmtstr = '%.2f',
        constant = 3133.4 / 60,  # SelectorLambda uses RPM
        offset = -0.00195,
    ),

    sel_rot = device('nicos.devices.tango.Motor',
        description = 'selector rotation table',
        tangodevice = tango_base + 'fzjs7/sel_rot',
        unit = 'deg',
        precision = 0.01,
        lowlevel = True,
    ),
)

extended = dict(
    representative = 'selector',
)
