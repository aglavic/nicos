description = 'setup for the NICOS watchdog'
group = 'special'

# The entries in this list are dictionaries. Possible keys:
#
# 'setup' -- setup that must be loaded (default '' to mean all setups)
# 'condition' -- condition for warning (a Python expression where cache keys
#    can be used: t_value stands for t/value etc.
# 'gracetime' -- time in sec allowed for the condition to be true without
#    emitting a warning (default 5 sec)
# 'message' -- warning message to display
# 'priority' -- 1 or 2, where 2 is more severe (default 1)
# 'action' -- code to execute if condition is true (default no code is executed)

watchlist = [
    dict(condition = 'LogSpace_status[0] == WARN',
         message = 'Disk space for log files becomes too low.',
         type = 'critical',
         gracetime = 30,
    ),
    dict(
        condition = '(sixfold_value == "closed" or nl2a_value == "closed") '
        'and reactorpower_value > 19.1',
        message = 'NL2a or sixfold shutter closed',
        type = 'critical',
    ),
    dict(
        condition = 'ch_value < 140',
        message = 'Choppers are down! DO SOMETHING!',
    ),
    dict(
        condition = 'flow_in_ch_cooling_value < 10',
        message = 'Cooling water flow is less than 10 l/min',
        priority = 1,
    ),
    dict(
        condition = 't_in_ch_cooling_value > 25',
        message = 'Cooling water temperature greater than 25 C',
        priority = 2,
    ),
    dict(
        condition = 'leak_ch_cooling_value > 3',
        message = 'There is a leak in the chopper cooling system',
        priority = 2,
    ),
]

# The Watchdog device has two lists of notifiers, one for priority 1 and
# one for priority 2.

includes = ['notifiers']

devices = dict(
    Watchdog = device('nicos.services.watchdog.Watchdog',
        cache = 'tofhw.toftof.frm2:14869',
        notifiers = {'default': ['emailer']},
        watch = watchlist,
        mailreceiverkey = 'emailer/receivers',
    ),
)
