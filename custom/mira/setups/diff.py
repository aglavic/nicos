description = 'MIRA2 diffraction setup'
group = 'basic'

includes = ['base', 'mono2', 'detector', 'alias_sth']

modules = ['commands.tas']

devices = dict(
    Sample = device('devices.tas.TASSample',
                    description = 'sample object',
                   ),

    mira   = device('devices.tas.TAS',
                    description = 'instrument, moves in HKL space',
                    instrument = 'MIRA',
                    responsible = 'Robert Georgii <robert.georgii@frm2.tum.de>',
                    cell = 'Sample',
                    phi = 'phi',
                    psi = 'sth',
                    mono = 'mono',
                    ana = 'vana',
                    alpha = None,
                    scatteringsense = (-1, 1, -1),
                    axiscoupling = False,
                    psi360 = False,
                   ),

    vana   = device('devices.tas.Monochromator',
                    description = 'virtual analyzer',
                    unit = 'A-1',
                    dvalue = 3.355,
                    theta = 'vath',
                    twotheta = 'vatt',
                    focush = None,
                    focusv = None,
                    abslimits = (0.1, 10),
                   ),

    vath   = device('devices.generic.VirtualMotor',
                    description = 'virtual analysator theta',
                    unit = 'deg',
                    abslimits = (-180, 180),
                    precision = 0.05,
                   ),

    vatt   = device('devices.generic.VirtualMotor',
                    description = 'virtual analysator two-theta',
                    unit = 'deg',
                    abslimits = (-180, 180),
                    precision = 0.05,
                   ),

    ki     = device('devices.tas.Wavevector',
                    description = 'incoming wavevector, also sets constant-ki mode when moved',
                    unit = 'A-1',
                    base = 'mono',
                    tas = 'mira',
                    scanmode = 'CKI',
                   ),

    Ei     = device('devices.tas.Energy',
                    description = 'incoming energy, also sets constant-ki mode when moved',
                    unit = 'meV',
                    base = 'mono',
                    tas = 'mira',
                    scanmode = 'CKI',
                   ),

    lam    = device('devices.tas.Wavelength',
                    description = 'incoming wavelength for diffraction',
                    unit = 'AA',
                    base = 'mono',
                    tas = 'mira',
                    scanmode = 'CKI',
                   ),
)

startupcode = '''
#SetDetectors(det)
'''
