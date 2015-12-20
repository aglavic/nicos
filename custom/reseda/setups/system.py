description = 'system setup'

sysconfig = dict(
    cache = 'resedahw',
    instrument = None,
    experiment = 'Exp',
    datasinks = ['conssink', 'filesink', 'daemonsink'],
    notifiers = [],
)

modules = ['commands.standard', 'commands.taco']

includes = ['notifiers', ]

devices = dict(
    Sample   = device('devices.tas.TASSample',
                      description = 'The sample',
                     ),

    Exp      = device('frm2.experiment.Experiment',
                      description = 'The currently running experiment',
                      dataroot = '/data',
                      sendmail = True,
                      serviceexp = '0',
                      sample = 'Sample',
                      mailsender = 'reseda@frm2.tum.de',
                      propdb = '/etc/proposaldb',
                     ),

    filesink = device('devices.datasinks.AsciiDatafileSink',
                      lowlevel = True,
                     ),

    conssink = device('devices.datasinks.ConsoleSink',
                      lowlevel = True,
                     ),

    daemonsink = device('devices.datasinks.DaemonSink',
                        lowlevel = True,
                       ),

    Space    = device('devices.generic.FreeSpace',
                      description = 'The amount of free space for storing data',
                      path = None,
                      minfree = 5,
                     ),
)

startupcode = '''
if not Exp.proposal:
    SetMode('master')
    NewExperiment(0)
'''
