description = 'Email and SMS notifiers'

group = 'lowlevel'

devices = dict(
    # Configure source and copy addresses to an existing address.
    email = device('nicos.devices.notifiers.Mailer',
        sender = 'pgaa@frm2.tum.de',
        copies = [
            ('zsolt.revay@frm2.tum.de', 'all'),
            ('revayzs@gmail.com', 'all'),
            ('christian.stieghorst@frm2.tum.de', 'all')
        ],
        mailserver = 'mailhost.frm2.tum.de',
        subject = 'PGAA',
        lowlevel = True,
    ),

    # Configure SMS receivers if wanted and registered with IT.
    smser = device('nicos.devices.notifiers.SMSer',
        server = 'triton.admin.frm2',
        receivers = [],
        lowlevel = True,
    ),
)
