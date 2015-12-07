description = 'basic PUMA triple-axis setup'


includes = ['sampletable', 'monochromator', 'analyser', 'lengths', 'reactor']

modules = ['commands.tas']

group = 'lowlevel'

sysconfig = dict(
    instrument = 'puma',
)

devices = dict(
    puma   = device('puma.spectro.PUMA',
                    description = 'DAS PUMA',
                    instrument = 'PUMA',
                    responsible = 'O. Sobolev <oleg.sobolev@frm2.tum.de>',
                    cell = 'Sample',
                    phi = 'phi',
                    psi = 'psi',
                    mono = 'mono',
                    ana = 'ana',
                    alpha = None,
                    scatteringsense = (-1, 1, -1),
                    energytransferunit = 'meV',
                    axiscoupling = True,
                   ),

    ki = device('devices.tas.Wavevector',
                description = 'incoming wavevector',
                unit = 'A-1',
                base = 'mono',
                tas = 'puma',
                scanmode = 'CKI',
               ),

    kf = device('devices.tas.Wavevector',
                description = 'final wavevector',
                unit = 'A-1',
                base = 'ana',
                tas = 'puma',
                scanmode = 'CKF'
               ),

    Ei = device('devices.tas.Energy',
                description = 'incoming energy',
                unit = 'meV',
                base = 'mono',
                tas = 'puma',
                scanmode = 'CKI'
               ),

    Ef = device('devices.tas.Energy',
                description = 'final energy',
                unit = 'meV',
                base = 'ana',
                tas = 'puma',
                scanmode = 'CKF',
               ),

    mono   = device('devices.generic.DeviceAlias',
                    alias = 'mono_pg002',
                    devclass = 'devices.tas.Monochromator',
                   ),

    mono_pg002 = device('devices.tas.Monochromator',
                        description = 'PG-002 monochromator',
                        order = 1,
                        unit = 'A-1',
                        theta = 'mth',
                        twotheta = 'mtt',
                        reltheta = True,
                        focush = 'mfhpg',
#                       focush = None,
                        focusv = 'mfvpg',
#                       focusv = None,
                        # focus value should equal mth (for arcane reasons...)
                        hfocuspars = [0.59065,7.33506,0.86068,-0.22745,0.02901],
                        vfocuspars = [0.59065,7.33506,0.86068,-0.22745,0.02901],
                        abslimits = (1, 7.5),
                        dvalue = 3.355,
                        scatteringsense = -1,
                       ),

#    mono_pg004 = device('devices.tas.Monochromator',
#                        description = 'PG-002 used as 004 monochromator',
#                        order = 2,
#                        unit = 'A-1',
#                        theta = 'mth',
#                        twotheta = 'mtt',
#                        reltheta = True,
#                        focush = 'mfhpg',
#                        focusv = 'mfvpg',
##                       focush = 'mfhcu',#
##                       focusv = 'mfvcu',
#                        hfocuspars = [0.59065,7.33506,0.86068,-0.22745,0.02901],
#                        vfocuspars = [0.59065,7.33506,0.86068,-0.22745,0.02901],
##                       hfocuspars = [1.34841,15.207,12.41842,-8.01148,2.13633],
##                       vfocuspars = [1.34841,15.207,12.41842,-8.01148,2.13633],
##                       abslimits = (1, 6),
#                        abslimits = (1, 10),
#                        dvalue = 3.355,
##                       dvalue = 1.278,
#                       ),

    mono_cu220 = device('devices.tas.Monochromator',
                        description = 'Cu-220 monochromator',
                        order = 1,
                        unit = 'A-1',
                        theta = 'mth',
                        twotheta = 'mtt',
                        reltheta = True,
                        focush = 'mfhcu',
                        focusv = 'mfvcu',
#                       focush = None,
#                       focusv = None,
                        # focus value should equal mth (for arcane reasons...)
                        hfocuspars = [1.34841,15.207,12.41842,-8.01148,2.13633],
                        vfocuspars = [1.34841,15.207,12.41842,-8.01148,2.13633],
                        abslimits = (3.5, 18.5),       # :FIXTHIS:
                        dvalue = 1.278,           # :FIXTHIS:
                        scatteringsense = -1,
                       ),

#    mono_cu111 = device('devices.tas.Monochromator',
#                        description = 'Cu-111 monochromator',
#                        order = 1,
#                        unit = 'A-1',
#                        theta = 'mth',
#                        twotheta = 'mtt',
#                        reltheta = True,
#                        focush = 'mfhcu1',    # :FIXTHIS:
#                        focusv = 'mfvcu1',    # :FIXTHIS:
#                        # focus value should equal mth (for arcane reasons...)
#                        hfocuspars = [0.24397,12.95642,0.88495,-0.31958,0.09283], # :FIXTHIS:
#                        vfocuspars = [0.24397,12.95642,0.88495,-0.31958,0.09283], # :FIXTHIS:
#                        abslimits = (1, 18),       # :FIXTHIS:
#                        dvalue = 2.08717,           # :FIXTHIS:
#                        scatteringsense = -1,
#                       ),

#    mono_ge311 = device('devices.tas.Monochromator',
#                        description = 'Germanium monochromator',
#                        order = 1,
#                        unit = 'A-1',
#                        theta = 'mth',
#                        twotheta = 'mtt',
#                        reltheta = True,
#                        focush = 'mfhge',
#                        focusv = 'mfvge',
##                       focush = None,
##                       focusv = None,
#                        hfocuspars = [0.40575,14.78787,3.10293,-1.6656,0.42283],
#                        vfocuspars = [0.40575,14.78787,3.10293,-1.6656,0.42283],
#                        abslimits = (1, 60),
#                        dvalue = 1.706,
#                       ),

    ana        = device('devices.generic.DeviceAlias',
                        description  = 'analyser alias device',
                        alias = 'ana_pg002',
                        devclass = 'devices.tas.Monochromator',
                       ),

    ana_pg002  = device('devices.tas.Monochromator',
                        description = 'analyser device',
                        unit = 'A-1',
                        theta = 'ath',
                        twotheta = 'att',
                        reltheta = True,
                        focush = 'afpg',
                        focusv = None,
                        hfocuspars = [0.59065,7.33506,0.86068,-0.22745,0.02901],
                        abslimits = (1, 5),
                        dvalue = 3.355,
                        scatteringsense = -1,
                       ),

    ana_ge311  = device('devices.tas.Monochromator',
                        description = 'Germanium monochromator',
                        order = 1,
                        unit = 'A-1',
                        theta = 'ath',
                        twotheta = 'att',
                        reltheta = True,
                        focush = None, # focush = 'afge',
                        focusv = None,
                        hfocuspars = [0.40575,14.78787,3.10293,-1.6656,0.42283],
                        abslimits = (1, 60),
                        dvalue = 1.706,
                        scatteringsense = -1,
                       ),
)

startupcode = '''
psi.alias = psi_puma
mono.alias = mono_pg002
'''
