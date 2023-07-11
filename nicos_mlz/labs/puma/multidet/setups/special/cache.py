description = 'setup for the cache server'
group = 'special'

devices = dict(
    DB = device('nicos.services.cache.server.FlatfileCacheDatabase',
        storepath = '/localdata/cache'
    ),
    Server = device('nicos.services.cache.server.CacheServer',
        db = 'DB',
        server = 'pumadma.puma.frm2',
        loglevel = 'info'
    ),
)
