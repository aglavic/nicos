description = 'Initialisation for asyn controllers for directly speaking to hardware'

devices = dict(
    port14 = device('nicos_ess.devices.epics.extensions.EpicsCommandReply',
        description = 'Controller of the devices connected to serial 14',
        commandpv = 'SQ:SANS:tiwi' + '.AOUT',
        replypv = 'SQ:SANS:tiwi' + '.AINP',
    ),
)
