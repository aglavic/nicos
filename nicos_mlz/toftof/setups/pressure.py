description = 'Setup for the pressure cell'

group = 'optional'

nethost = 'toftofsrv.toftof.frm2.tum.de'

devices = dict(
    P = device('nicos.devices.taco.AnalogInput',
        description = 'Pressure cell device',
        tacodevice = '//%s/toftof/pressure/value' % nethost,
        unit = 'bar',
        pollinterval = 120,
    ),
)

startupcode = '''
AddEnvironment(P)
'''
