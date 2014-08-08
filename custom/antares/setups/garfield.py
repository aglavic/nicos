description = 'ANTARES garfield magnet'
group = 'optional'

includes = []

taco_host = 'amagnet'

devices = dict(
    garfield_onoff = device('antares.switches.ToggleSwitch',
                      description = 'Garfield magnet: polarity (+/-) switch',
                      tacodevice = '//%s/amagnet/beckhoff/onoff' % taco_host,
                      readback = '//%s/amagnet/beckhoff/honoff' % taco_host,
                      mapping = { 1 : 'on', 0 : 'off'},
                     ),
    garfield_polarity = device('antares.switches.ReadbackSwitch',
                      description = 'Garfield magnet: polarity (+/-) switch',
                      tacodevice = '//%s/amagnet/beckhoff/posneg' % taco_host,
                      readback = '//%s/amagnet/beckhoff/hpos' % taco_host,
                      mapping = { 1 : '+', 2 : '-'},
                      rwmapping = { 0 : 2 },
                     ),
    garfield_connection = device('antares.switches.ReadbackSwitch',
                      description = 'Garfield magnet: polarity (+/-) switch',
                      tacodevice = '//%s/amagnet/beckhoff/serpar' % taco_host,
                      readback = '//%s/amagnet/beckhoff/hpar' % taco_host,
                      mapping = { 1 : 'par', 2 : 'ser'},
                      rwmapping = { 0 : 2 },
                     ),
    garfield_temp1 = device('devices.taco.AnalogInput',
                         description = 'Taco device for temperature 1',
                         tacodevice = '//%s/amagnet/beckhoff/temp1' % taco_host,
                         unit = 'K',
                        ),
    garfield_temp2 = device('devices.taco.AnalogInput',
                         description = 'Taco device for temperature 2',
                         tacodevice = '//%s/amagnet/beckhoff/temp2' % taco_host,
                         unit = 'K',
                        ),

    garfield_temp3 = device('devices.taco.AnalogInput',
                         description = 'Taco device for temperature 3',
                         tacodevice = '//%s/amagnet/beckhoff/temp3' % taco_host,
                         unit = 'K',
                        ),

    garfield_temp4 = device('devices.taco.AnalogInput',
                         description = 'Taco device for temperature 4',
                         tacodevice = '//%s/amagnet/beckhoff/temp4' % taco_host,
                         unit = 'K',
                        ),
    garfield_T = device('devices.taco.TemperatureController',
                         description = 'Taco device for the magnet temperature',
                         tacodevice = '//%s/amagnet/ls340/control' % taco_host,
                         unit = 'K',
                         abslimits = (-300, 300),
                        ),
    garfield_F = device('devices.taco.CurrentSupply',
                         description = 'Taco device for the magnet power supply (current mode)',
                         tacodevice = '//%s/amagnet/lambda/out' % taco_host,
                         unit = 'A',
                         abslimits = (0, 200),
                        ),
)

startupcode = '''
'''
