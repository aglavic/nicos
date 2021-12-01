description = 'KOMPASS diffraction mode setup'
group = 'basic'

includes = ['mono', 'guidefocus', 'selector', 'astrium', 'sample', 'alias_sth',
            'reactor',
            'detector',
            'vanalyzer',
           ]

modules = ['nicos.commands.tas']

devices = dict(
    Sample = device('nicos.devices.tas.TASSample',
        description = 'sample object',
    ),
    alphastorage = device('nicos_mlz.panda.devices.guidefield.AlphaStorage',
        description = 'Virtual device for handling \\alpha changes',
        abslimits = (-360, 360),
        unit = 'deg',
        lowlevel = True,
    ),
    Kompass = device('nicos.devices.tas.TAS',
        description = 'instrument object',
        instrument = 'KOMPASS',
        responsible = 'Dmitry Gorkov <dmitry.gorkov@frm2.tum.de>',
        cell = 'Sample',
        phi = 'stt',
        psi = 'sth',
        mono = 'mono',
        ana = 'ana',
        alpha = 'alphastorage',
        scatteringsense = (1, -1, 1),
        axiscoupling = False,
        psi360 = False,
    ),
    ki = device('nicos.devices.tas.Wavevector',
        description = 'incoming wavevector, also sets constant-ki mode when moved',
        unit = 'A-1',
        base = 'mono',
        tas = 'Kompass',
        scanmode = 'CKI',
    ),
    Ei = device('nicos.devices.tas.Energy',
        description = 'incoming energy, also sets constant-ki mode when moved',
        unit = 'meV',
        base = 'mono',
        tas = 'Kompass',
        scanmode = 'CKI',
    ),
    lam = device('nicos.devices.tas.Wavelength',
        description = 'incoming wavelength for diffraction',
        unit = 'AA',
        base = 'mono',
        tas = 'Kompass',
        scanmode = 'CKI',
    ),
)
