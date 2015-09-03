description = 'Setup for RESEDA frequencies and calculations'

group = 'lowlevel'

nethost = 'resedasrv'

devices = dict(

    F0 = device('devices.taco.AnalogInput',
                description = 'Frequency Generator F0',
                tacodevice = '//%s/reseda/hp33250a_1/freq' % (nethost,),
                pollinterval = 5,
                maxage = 8,
               ),

    F1 = device('devices.taco.AnalogInput',
                description = 'Frequency Generator F1',
                tacodevice = '//%s/reseda/hp33250a_2/freq' % (nethost,),
                pollinterval = 5,
                maxage = 8,
               ),

    F2 = device('devices.taco.AnalogInput',
                description = 'Frequency Generator F2',
                tacodevice = '//%s/reseda/hp33250a_3/freq' % (nethost,),
                pollinterval = 5,
                maxage = 8,
               ),

    Fu0 = device('devices.taco.AnalogInput',
                 description = 'Frequency Generator F0',
                 tacodevice = '//%s/reseda/hp33250a_1/amp' % (nethost,),
                 pollinterval = 5,
                 maxage = 8,
                ),

    Fu1 = device('devices.taco.AnalogInput',
                 description = 'Frequency Generator F1',
                 tacodevice = '//%s/reseda/hp33250a_2/amp' % (nethost,),
                 pollinterval = 5,
                 maxage = 8,
                ),

    Fu2 = device('devices.taco.AnalogInput',
                 description = 'Frequency Generator F2',
                 tacodevice = '//%s/reseda/hp33250a_3/amp' % (nethost,),
                 pollinterval = 5,
                 maxage = 8,
                ),

    RF0 = device('reseda.frequencies.Frequencies',
                 description = 'Interface F0',
                 tacodevice = '//%s/reseda/nigpib/keithley0' % (nethost,),
                 pollinterval = 5,
                 maxage = 8,
                ),

    RF1 = device('reseda.frequencies.Frequencies',
                 description = 'Interface F1',
                 tacodevice = '//%s/reseda/nigpib/keithley1' % (nethost,),
                 pollinterval = 5,
                 maxage = 8,
                ),

    RF2 = device('reseda.frequencies.Frequencies',
                 description = 'Interface F2',
                 tacodevice = '//%s/reseda/nigpib/keithley2' % (nethost,),
                 pollinterval = 5,
                 maxage = 8,
                ),

    length = device('devices.generic.cache.CacheReader',
                    description = 'Read from data.txt',
                    unit = 'mm',
                   ),

    B31_c = device('devices.taco.AnalogInput',
                   description = 'B22',
                   tacodevice = '//%s/reseda/ics4861a/ain3' % (nethost,),
                   pollinterval = 10,
                   # channel = 1,
                   maxage = 15,
                  ),

    Sel = device('reseda.selector.Selector',
                 description = 'Selector',
                 tacodevice = '//%s/reseda/rs232/sel' % (nethost,),
                 pollinterval = 300,
                 maxage = 600,
                ),

    tiltangle = device('devices.generic.cache.CacheReader',
                       description = 'Readed from data.txt',
                       unit = '',
                      ),

    Lambda = device('reseda.selector.Wavelength',
                    description = 'Calculation of wavelength',
                    selector = 'Sel',
                    tiltangle = 'tiltangle',
                    pollinterval = 32,
                    maxage = 61,
                   ),

    m1 = device('devices.taco.AnalogInput',
                description = 'TwoTheta 1',
                tacodevice = '//%s/reseda/husco1/motor7' % (nethost,),
                pollinterval = 5,
                maxage = 8,
               ),

    m2 = device('devices.taco.AnalogInput',
                description = 'TwoTheta 2',
                tacodevice = '//%s/reseda/husco1/motor8' % (nethost,),
                pollinterval = 5,
                maxage = 8,
               ),

    Q1 = device('reseda.scatteringvector.ScatteringVector',
                description = 'Calculation of scattering vector(m1)',
                wavelength = 'Lambda',
                twotheta = 'm1',
                pollinterval = 32,
                maxage = 61,
               ),

    Q2 = device('reseda.scatteringvector.ScatteringVector',
                description = 'Calculation of scattering vector(m2)',
                wavelength = 'Lambda',
                twotheta = 'm2',
                pollinterval = 32,
                maxage = 61,
               ),

    TauT = device('reseda.tau.tauTwoarms',
                  description = 'Calculation of tau for standard settings',
                  wavelength = 'Lambda',
                  current = 'B31_c',
                  fu0 = 'Fu0',
                  frequency = 'F0',
                  pollinterval = 32,
                  maxage = 64,
                 ),

    TauM = device('reseda.tau.tauMieze',
                  description = 'Calculation of tau MIEZE',
                  length = 'length',
                  frequency0 = 'F0',
                  frequency1 = 'F1',
                  wavelength = 'Lambda',
                  pollinterval = 32,
                  maxage = 64,
                 ),

)
