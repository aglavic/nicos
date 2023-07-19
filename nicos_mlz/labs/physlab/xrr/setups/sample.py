description = 'sample stage'
group = 'optional'
display_order = 70

tango_base = configdata('instrument.values')['tango_base'] + 'box/'

devices = dict(
    phi_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'bruker/phi',
        unit = 'deg',
        precision = 5e-3,
        fmtstr = '%.4f',
        visibility = (),
    ),
    phi = device('nicos.devices.generic.Axis',
        description = 'sample rotation around base normal',
        motor = 'phi_m',
        precision = 5e-3,
    ),
    chi_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'bruker/chi',
        unit = 'deg',
        precision = 2.5e-4,
        fmtstr = '%.4f',
        visibility = (),
    ),
    chi = device('nicos.devices.generic.Axis',
        description = 'sample tilt around beam axis',
        motor = 'chi_m',
        precision = 2.5e-4,
    ),
    theta_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'bruker/theta',
        unit = 'deg',
        precision = 1e-3,
        fmtstr = '%.3f',
        visibility = (),
    ),
    theta = device('nicos.devices.generic.Axis',
        description = 'sample theta angle',
        motor = 'theta_m',
        precision = 1e-3,
    ),
    ctt = device('nicos_mlz.labs.physlab.devices.coupled.CoupledMotor',
        description = 'Coupled Theta / 2Theta axis',
        maxis = 'ttheta',
        caxis = 'theta',
        unit = 'deg',
        fmtstr = '%.3f',
    ),
    ttheta_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'bruker/ttheta',
        unit = 'deg',
        precision = 1e-3,
        fmtstr = '%.3f',
        visibility = (),
    ),
    ttheta = device('nicos.devices.generic.Axis',
        description = 'sample two-theta angle',
        motor = 'ttheta_m',
        precision = 1e-3,
    ),
    knife_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'bruker/knife',
        unit = 'mm',
        precision = 5e-4,
        fmtstr = '%.4f',
        visibility = (),
    ),
    knife = device('nicos.devices.generic.Axis',
        description = 'Single edge (knife)',
        motor = 'knife_m',
        precision = 5e-4,
    ),
    z_m = device('nicos.devices.entangle.Motor',
        tangodevice = tango_base + 'bruker/z',
        unit = 'mm',
        precision = 1.5e-4,
        fmtstr = '%.4f',
        visibility = (),
    ),
    z = device('nicos.devices.generic.Axis',
        description = 'sample z translation',
        motor = 'z_m',
        precision = 1.5e-4,
    ),
)
