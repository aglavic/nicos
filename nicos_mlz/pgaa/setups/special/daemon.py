description = 'setup for the execution daemon'
group = 'special'

devices = dict(
    UserDBAuth = device('nicos_mlz.devices.ghost.Authenticator',
         description = 'FRM II user office authentication',
         instrument = 'PGAA',
         ghosthost = 'ghost.mlz-garching.de',
         aliases = {
         },
         loglevel = 'info',
    ),
    LDAPAuth = device('nicos.services.daemon.auth.ldap.Authenticator',
        uri = [
            'ldap://pgaasrv.pgaa.frm2.tum.de',
        ],
        bindmethod = 'tls_before_bind',
        userbasedn = 'ou=People,dc=pgaa,dc=frm2,dc=tum,dc=de',
        groupbasedn = 'ou=Group,dc=pgaa,dc=frm2,dc=tum,dc=de',
        grouproles = {
            'pgaa': 'admin',
        },
    ),
    LDAPAuthBU = device('nicos.services.daemon.auth.ldap.Authenticator',
        uri = [
            'ldap://phaidra.admin.frm2.tum.de',
            'ldap://ariadne.admin.frm2.tum.de',
            'ldap://sarpedon.admin.frm2.tum.de',
            'ldap://minos.admin.frm2.tum.de',
        ],
        bindmethod = 'tls_before_bind',
        userbasedn = 'ou=People,dc=frm2,dc=tum,dc=de',
        groupbasedn = 'ou=Group,dc=frm2,dc=tum,dc=de',
        grouproles = {
            'pgaa': 'admin',
            'ictrl': 'admin',
            'se': 'user',
        }
    ),
    Daemon = device('nicos.services.daemon.NicosDaemon',
        server = '0.0.0.0',
        authenticators = ['UserDBAuth', 'LDAPAuth', 'LDAPAuthBU',],
        loglevel = 'info',
    ),
)
