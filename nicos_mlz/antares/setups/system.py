#  -*- coding: utf-8 -*-

description = 'system setup'

sysconfig = dict(
    cache = 'antareshw.antares.frm2',
    instrument = 'ANTARES',
    experiment = 'Exp',
    datasinks = ['conssink', 'filesink', 'daemonsink'],
    notifiers = ['email', 'smser'],
)

modules = ['nicos.commands.basic', 'nicos.commands.standard',
           'nicos_mlz.antares.commands']

includes = ['notifiers']

devices = dict(
    Sample = device('nicos.devices.experiment.Sample',
        description = 'Default Sample',
    ),
    Exp = device('nicos_mlz.antares.devices.Experiment',
        description = 'Antares Experiment',
        dataroot = '/data/FRM-II',
        sample = 'Sample',
        mailsender = 'antares@frm2.tum.de',
        serviceexp = 'service',
        servicescript = '',
        templates = 'templates',
        sendmail = False,
        zipdata = False,
        managerights = dict(
            enableDirMode = 0o770,
            enableFileMode = 0o660,
            disableDirMode = 0o550,
            disableFileMode = 0o440,
        ),
    ),
    ANTARES = device('nicos.devices.instrument.Instrument',
        description = 'Antares Instrument',
        instrument = 'ANTARES',
        responsible = 'Michael Schulz <michael.schulz@frm2.tum.de>',
        doi = 'http://dx.doi.org/10.17815/jlsrf-1-42',
        operators = ['Technische Universität München (TUM)'],
        website = 'http://www.mlz-garching.de/antares',
    ),
    filesink = device('nicos.devices.datasinks.AsciiScanfileSink',
        description = 'Scanfile storing device',
        filemode = 0o440,
    ),
    conssink = device('nicos.devices.datasinks.ConsoleScanSink',
        description = 'Device handling console output',
    ),
    daemonsink = device('nicos.devices.datasinks.DaemonSink',
        description = 'Data handling inside the daemon',
    ),
    Space = device('nicos.devices.generic.FreeSpace',
        description = 'Free Space in the RootDir of AntaresHW',
        path = '/',
        minfree = 5,
    ),
    HomeSpace = device('nicos.devices.generic.FreeSpace',
        description = 'Free Space in the home directory of user antares',
        path = '/home/antares/antares',
        minfree = 1,
    ),
    DataSpace = device('nicos.devices.generic.FreeSpace',
        description = 'Free Space on the DataStorage',
        path = '/data',
        minfree = 500,
    ),
    VarSpace = device('nicos.devices.generic.FreeSpace',
        description = 'Free Space on /var',
        path = '/var',
        minfree = 3,
    ),
    LogSpace = device('nicos.devices.generic.FreeSpace',
        description = 'Free space on the log drive',
        path = '/antarescontrol/log',
        visibility = (),
        warnlimits = (0.5, None),
    ),
    BarcodeReader = device('nicos_mlz.devices.barcodes.BarcodeInterpreter',
        description = 'Receives and processes barcodes from a reader',
        tangodevice = 'tango://antareshw.antares.frm2:10000/antares/barcodes/reader',
        commandmap = {
        },
    ),
)
