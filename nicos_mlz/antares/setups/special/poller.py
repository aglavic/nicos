description = 'setup for the poller'
group = 'special'

sysconfig = dict(
    cache = 'antareshw.antares.frm2'
)

devices = dict(
    Poller = device('nicos.services.poller.Poller',
        description = 'Device polling service',
        alwayspoll = ['ubahn'],
        neverpoll = ['detector_hfr'],
        blacklist = ['tas'],
    ),
)
