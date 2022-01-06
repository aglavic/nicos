description = 'setup for the execution daemon'
group = 'special'

devices = dict(
    # fixed list of users:
    # first entry is the user name, second the hashed password, third the user
    # level
    # The user level are 'guest, 'user', and 'admin', ascending ordered in
    # respect to the rights
    # The entries for the password hashes are generated from randomized
    # passwords and not reproduceable, please don't forget to create new ones:
    # start python
    # >>> import hashlib
    # >>> hashlib.md5('password').hexdigest()
    # or
    # >>> hashlib.sha1('password').hexdigest()
    Auth=device('nicos.services.daemon.auth.list.Authenticator',
                # the hashing maybe 'md5' or 'sha1'
                hashing='sha1',
                passwd=[('spy', '15346b593c4d0cf05fb6e67a5669d852e6550481',
                         'guest'),
                        ('user', '88380931080d6a2a097133d0704ea789814c8dea',
                         'user'),
                        ('admin', '76702e9ada292df094a875e5f72e9f778099d477',
                         'admin'),
                        ('perl_client', '8aecf7021fe5212f5e4af74f3c075c2b875929fe',
                         'user'),
                        ],
                ),
    Daemon=device('nicos.services.daemon.NicosDaemon',
                  server='',
                  authenticators=['Auth', ],  # and/or 'UserDB'
                  loglevel='info',
                  ),
)

startupcode = '''
import nicos.devices.epics
'''
