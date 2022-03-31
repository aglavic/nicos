description = 'system setup'

group = 'lowlevel'

sysconfig = dict(
    cache='localhost',
    instrument='LoKI',
    experiment='Exp',
    datasinks=['conssink', 'filesink', 'daemonsink'],
)

modules = ['nicos.commands.standard']

devices = dict(
    LoKI=device('nicos.devices.instrument.Instrument',
        description='instrument object',
        instrument='LoKI',
        responsible='J. Houston <judith.houston@ess.eu>',
        website='https://europeanspallationsource.se/instruments/loki'
    ),

    Sample=device('nicos.devices.sample.Sample',
        description='The currently used sample',
    ),

    Exp=device('nicos_ess.devices.experiment.EssExperiment',
        description='experiment object',
        dataroot='/opt/nicos-data/loki',
        sample='Sample',
        cache_filepath='/opt/nicos-data/loki/cached_proposals.json'
    ),

    filesink=device('nicos.devices.datasinks.AsciiScanfileSink',),

    conssink=device('nicos.devices.datasinks.ConsoleScanSink',),

    daemonsink=device('nicos.devices.datasinks.DaemonSink',),

    Space=device('nicos.devices.generic.FreeSpace',
        description='The amount of free space for storing data',
        path=None,
        minfree=5,
    ),
)

startupcode = '''
'''
