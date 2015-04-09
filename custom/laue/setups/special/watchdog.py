# This setup file configures the nicos poller service.

description = 'setup for the NICOS watchdog'
group = 'special'

# watchlist:
# The entries in this list are dictionaries. Possible keys:
#
# 'setup' -- setup that must be loaded (default '' to mean all setups)
# 'condition' -- condition for warning (a Python expression where cache keys
#    can be used: t_value stands for t/value etc.
# 'gracetime' -- time in sec allowed for the condition to be true without
#    emitting a warning (default 5 sec)
# 'message' -- warning message to display
# 'type' -- for defining different types of warnings; this corresponds to the
#     configured notifiers (default 'default')
#     type '' does not emit warnings (useful together with 'pausecount'
#     for conditions that should block counting but are not otherwise errors)
# 'pausecount' -- if True, the count loop should be paused on the condition
#     (default False)
# 'action' -- code to execute if condition is true (default no code is executed)
watchlist = [
     dict(condition = 'reactorpower_value < 10',
          precondition = 'reactorpower_value >19',
          precondtime = 600,
          message = 'Reactor power too low',
          type = 'critical',
          action = 'abort()',
          gracetime = 300,
         ),
]

notifiers = {
    'default':  ['mailer'],
    'critical': ['mailer', 'smser'],
}

devices = dict(
    # Configure source and copy addresses to an existing address.
    mailer   = device('devices.notifiers.Mailer',
                      sender = 'noreply@frm2.tum.de',
                      receivers = ['bjoern.pedersen@frm2.tum.de'],
                      subject = 'NICOS Warning',
                     ),

    # Configure SMS receivers if wanted and registered with IT.
    smser    = device('devices.notifiers.SMSer',
                      server = 'triton.admin.frm2',
                      receivers = [],
                     ),

    Watchdog = device('services.watchdog.Watchdog',
                      # use only 'localhost' if the cache is really running on
                      # the same machine, otherwise use the official computer
                      # name
                      cache = 'lauectrl.laue.frm2',
                      notifiers = notifiers,
                      mailreceiverkey = 'email/receivers',
                      watch = watchlist,
                     ),
)
