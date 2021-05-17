description = 'system setup'

group = 'lowlevel'

sysconfig = dict(
    cache='localhost',
    instrument='LoKI',
    experiment='Exp',
    datasinks=['conssink', 'filesink', 'daemonsink'],
)

modules = ['nicos.commands.standard', 'nicos_ess.loki.commands.scripting']

devices = dict(
    LoKI=device('nicos.devices.instrument.Instrument',
                description='instrument object',
                instrument='LoKI',
                responsible='J. Houston <judith.houston@ess.eu>',
                website='https://europeanspallationsource.se/instruments/loki'
                ),

    Sample=device('nicos_ess.loki.devices.sample.LokiSample',
                  description='The currently used sample',
                  ),

    Exp=device('nicos.devices.experiment.Experiment',
               description='experiment object',
               dataroot='/opt/nicos-data',
               sendmail=False,
               serviceexp='p0',
               sample='Sample',
               ),

    Aperture=device('nicos_ess.loki.devices.'
                    'experiment_configuration.Aperture',
                    x='0.0',
                    y='0.0',
                    width='0.0',
                    height='0.0',
                    lowlevel=True,
                    ),

    filesink=device('nicos.devices.datasinks.AsciiScanfileSink', ),

    conssink=device('nicos.devices.datasinks.ConsoleScanSink', ),

    daemonsink=device('nicos.devices.datasinks.DaemonSink', ),

    Space=device('nicos.devices.generic.FreeSpace',
                 description='The amount of free space for storing data',
                 path=None,
                 minfree=5,
                 ),

    positioner=device('nicos.devices.generic.DeviceAlias',
                      devclass='nicos.core.device.Moveable',
                      ),
)

startupcode = '''
'''
