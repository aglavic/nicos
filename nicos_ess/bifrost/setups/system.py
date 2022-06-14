description = 'system setup'

group = 'lowlevel'

sysconfig = dict(
    cache='localhost',
    instrument='BIFROST',
    experiment='Exp',
    datasinks=['conssink', 'daemonsink', 'liveview'],
)

modules = ['nicos.commands.standard', 'nicos_ess.commands']

devices = dict(
    BIFROST=device(
        'nicos.devices.instrument.Instrument',
        description='instrument object',
        facility='European Spallation Source (ERIC)',
        instrument='BIFROST',
        responsible='Ebad Kamil <ebad.kamil@ess.eu>',
        website='https://europeanspallationsource.se/instruments/bifrost'),
    Sample=device(
        'nicos.devices.sample.Sample',
        description='The currently used sample',
    ),
    Exp=device('nicos_ess.devices.experiment.EssExperiment',
               description='experiment object',
               dataroot='/opt/nicos-data',
               filewriter_root='/opt/nicos-data/bifrost',
               sample='Sample',
               cache_filepath='/opt/nicos-data/bifrost/cached_proposals.json'),
    conssink=device(
        'nicos_ess.devices.datasinks.console_scan_sink.ConsoleScanSink'),
    daemonsink=device('nicos.devices.datasinks.DaemonSink', ),
    liveview=device('nicos.devices.datasinks.LiveViewSink', ),
    Space=device(
        'nicos.devices.generic.FreeSpace',
        description='The amount of free space for storing data',
        path=None,
        minfree=5,
    ),
    KafkaForwarderStatus=device(
        'nicos_ess.devices.forwarder.EpicsKafkaForwarder',
        description='Monitors the status of the Forwarder',
        statustopic="status_topic",
        brokers=["localhost"],
    ),
)
