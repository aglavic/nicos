description = 'Event Receiver setup.'

pv_root = 'LabS-Utgard-VIP'

devices = dict(
    EVR_time = device('nicos.devices.epics.EpicsStringReadable',
                readpv = '{}Time:Valid-Sts'.format(pv_root),
                description='Status of the EVR timing'),
    EVR_link = device('nicos.devices.epics.EpicsStringReadable',
                readpv = '{}Link-Sts'.format(pv_root),
                description='Status of link to EVG'),
)
