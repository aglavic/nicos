description = 'system setup'

group = 'lowlevel'

sysconfig = dict(
    cache = 'localhost',
    instrument = 'FOCUS',
    experiment = 'Exp',
    datasinks = ['conssink', 'dmnsink', 'livesink', 'nxsink', 'quiecksink'],
)

modules = [
    'nicos.commands.standard', 'nicos_sinq.commands.sics',
    'nicos_sinq.commands.epicscommands', 'nicos_sinq.commands.tableexe',
    'nicos_sinq.focus.commands.focus'
]

devices = dict(
    FOCUS = device('nicos.devices.instrument.Instrument',
        description = 'instrument object',
        instrument = 'SINQ FOCUS',
        responsible = 'Fanni Juranyi <fanni.juranyi@psi.ch>',
        operators = ['Paul-Scherrer-Institut (PSI)'],
        facility = 'SINQ, PSI',
        website = 'https://www.psi.ch/sinq/focus/',
    ),
    Sample = device('nicos.devices.experiment.Sample',
        description = 'The currently used sample',
    ),
    Exp = device('nicos_sinq.devices.experiment.SinqExperiment',
        description = 'experiment object',
        dataroot = configdata('config.DATA_PATH'),
        sendmail = False,
        serviceexp = 'Service',
        sample = 'Sample',
        forcescandata = True,
    ),
    Space = device('nicos.devices.generic.FreeSpace',
        description = 'The amount of free space for storing data',
        path = None,
        minfree = 5,
    ),
    conssink = device('nicos.devices.datasinks.ConsoleScanSink'),
    dmnsink = device('nicos.devices.datasinks.DaemonSink'),
    livesink = device('nicos.devices.datasinks.LiveViewSink',
        description = 'Sink for forwarding live data to the GUI',
    ),
    nxfw = device('nicos.devices.generic.ManualSwitch',
        description = 'Switch for enabling/disabling NeXus file writing',
        states = ['on', 'off']
    ),
    nxsink = device('nicos_sinq.devices.datasinks.SwitchableNexusSink',
        file_switch = 'nxfw',
        description = 'Sink for NeXus file writer',
        filenametemplate = ['focus%(year)sn%(scancounter)06d.hdf'],
        templateclass =
        'nicos_sinq.focus.nexus.nexus_templates.FOCUSTemplateProvider',
    ),
    quiecksink = device('nicos_sinq.devices.datasinks.QuieckSink',
        description = 'Sink for sending UDP datafile '
        'notifications'
    ),
)
