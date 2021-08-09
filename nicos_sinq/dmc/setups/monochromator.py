description = 'Monochromator devices for SINQ DMC.'

pvprefix = 'SQ:DMC:mcu1:'

devices = dict(
    a1=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Monochromator rotation (mth)',
               motorpv=f'{pvprefix}A1',
               errormsgpv=f'{pvprefix}A1-MsgTxt',
               precision=0.01,
#               lowlevel=True,
               ),

    a2=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Monochromator takeoff angle (m2t)',
               motorpv=f'{pvprefix}A2',
               errormsgpv=f'{pvprefix}A2-MsgTxt',
               precision=0.01,
#               lowlevel=True,
               ),
    mtl=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Monochromator translation lower',
               motorpv=f'{pvprefix}MTL',
               errormsgpv=f'{pvprefix}MTL-MsgTxt',
               precision=0.01,
#               lowlevel=True,
#               requires = {'level': 'admin'},
               ),
    mtu=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Monochromator translation upper',
               motorpv=f'{pvprefix}MTU',
               errormsgpv=f'{pvprefix}MTU-MsgTxt',
               precision=0.01,
#               lowlevel=True,
#               requires = {'level': 'admin'},
               ),

    mgl=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Monochromator goniometer lower',
               motorpv=f'{pvprefix}MGL',
               errormsgpv=f'{pvprefix}MGL-MsgTxt',
#               lowlevel=True,
#               requires = {'level': 'admin'},
               ),

    mgu=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Monochromator goniometer upper',
               motorpv=f'{pvprefix}MGU',
               errormsgpv=f'{pvprefix}MGU-MsgTxt',
#               lowlevel=True,
#               requires = {'level': 'admin'},
               ),
    mcv=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Monochromator curvature',
               motorpv=f'{pvprefix}MCV',
               errormsgpv=f'{pvprefix}MCV-MsgTxt',
               ),
    wavelength = device('nicos_sinq.devices.mono.SinqMonochromator',
        description = 'PG analyser (default)',
        unit = 'A',
        theta = 'a1',
        twotheta = 'a2',
        focush = None,
        focusv = 'mcv',
        order=1,
        abslimits = (2, 5),
        vfocuspars = [-0.025942, 5.351660],
        dvalue = 3.3537,
        scatteringsense = 1,
        crystalside=1,
    ),
)
