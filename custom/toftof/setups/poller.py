description = 'setup for the poller'
group = 'special'

sysconfig = dict(
    cache = 'cpci1.toftof.frm2'
)

devices = dict(
    Poller = device('nicos.poller.Poller',
                    autosetup = False,  # important! do not poll everything
                    poll = ['chopper', 'reactor', 'vacuum', 'voltage'] +
                           ['he3', 'htf', 'ls', 'biofurnace', 'cryo_ccr', ],
                    alwayspoll = [],
                    blacklist = []),
)
