description = 'setup for the electronic logbook'

group = 'special'

sysconfig = dict(
    cache = None,
)

devices = dict(
    Logbook = device('nicos.services.elog.Logbook',
        prefix = 'logbook/',
        cache = 'tofhw.toftof.frm2.tum.de:14869',
    ),
)
