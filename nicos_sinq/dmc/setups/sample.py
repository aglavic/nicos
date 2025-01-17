description = 'Sample devices in the SINQ DMC.'

pvprefix = 'SQ:DMC:mcu2:'

devices = dict(
    a3s=device('nicos_sinq.devices.epics.motor.EpicsMotor',
               description='Sample omega motor',
               motorpv=f'{pvprefix}A3',
               errormsgpv=f'{pvprefix}A3-MsgTxt',
               can_disable=True,
               auto_enable=True,
               ),
    a3=device('nicos.core.device.DeviceAlias',
              description='Alias for sample rotation',
              devclass='nicos.core.device.Moveable'),
)
alias_config = {'a3': {'a3s': 10}}  # , 'se_om': 20}}
