description = 'User devices'

display_order = 90

pvprefix = 'SQ:ICON:user:'

precision_val = 10
window_val = 5
timeout_val = 20

devices = dict(
    user_dev_01 = device('nicos.devices.epics.pyepics.EpicsWindowTimeoutDevice',
        description = 'User device 1',
        writepv = pvprefix + 'Dev01',
        readpv = pvprefix + 'Dev01RBV',
        precision = precision_val,
        window = window_val,
        timeout = timeout_val,
        abslimits = (-1e9, 1e9),
    ),
    user_dev_02 = device('nicos.devices.epics.pyepics.EpicsWindowTimeoutDevice',
        description = 'User device 1',
        writepv = pvprefix + 'Dev02',
        readpv = pvprefix + 'Dev02RBV',
        precision = precision_val,
        window = window_val,
        timeout = timeout_val,
        abslimits = (-1e9, 1e9),
    ),
    user_dev_03 = device('nicos.devices.epics.pyepics.EpicsWindowTimeoutDevice',
        description = 'User device 1',
        writepv = pvprefix + 'Dev03',
        readpv = pvprefix + 'Dev03RBV',
        precision = precision_val,
        window = window_val,
        timeout = timeout_val,
        abslimits = (-1e9, 1e9),
    ),
    user_dev_04 = device('nicos.devices.epics.pyepics.EpicsWindowTimeoutDevice',
        description = 'User device 1',
        writepv = pvprefix + 'Dev04',
        readpv = pvprefix + 'Dev04RBV',
        precision = precision_val,
        window = window_val,
        timeout = timeout_val,
        abslimits = (-1e9, 1e9),
    ),
    user_dev_05 = device('nicos.devices.epics.pyepics.EpicsWindowTimeoutDevice',
        description = 'User device 1',
        writepv = pvprefix + 'Dev05',
        readpv = pvprefix + 'Dev05RBV',
        precision = precision_val,
        window = window_val,
        timeout = timeout_val,
        abslimits = (-1e9, 1e9),
    ),
    user_dev_06 = device('nicos.devices.epics.pyepics.EpicsWindowTimeoutDevice',
        description = 'User device 1',
        writepv = pvprefix + 'Dev06',
        readpv = pvprefix + 'Dev06RBV',
        precision = precision_val,
        window = window_val,
        timeout = timeout_val,
        abslimits = (-1e9, 1e9),
    ),
    user_dev_07 = device('nicos.devices.epics.pyepics.EpicsWindowTimeoutDevice',
        description = 'User device 1',
        writepv = pvprefix + 'Dev07',
        readpv = pvprefix + 'Dev07RBV',
        precision = precision_val,
        window = window_val,
        timeout = timeout_val,
        abslimits = (-1e9, 1e9),
    ),
    user_dev_08 = device('nicos.devices.epics.pyepics.EpicsWindowTimeoutDevice',
        description = 'User device 1',
        writepv = pvprefix + 'Dev08',
        readpv = pvprefix + 'Dev08RBV',
        precision = precision_val,
        window = window_val,
        timeout = timeout_val,
        abslimits = (-1e9, 1e9),
    ),
)
