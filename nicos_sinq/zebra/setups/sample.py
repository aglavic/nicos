description = 'Devices for the sample table'

pvpref = 'SQ:ZEBRA:mcu'

devices = dict(
    om_raw = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample rotation',
        motorpv = pvpref + '1:SOM',
        errormsgpv = pvpref + '1:SOM-MsgTxt',
        precision = 0.5,
        can_disable = True,
        auto_enable = True,
    ),
    om = device('nicos.core.device.DeviceAlias',
        description = 'Alias for om',
        alias = 'om_raw',
        devclass = 'nicos.core.device.Moveable'
    ),
    sx = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample X translation',
        motorpv = pvpref + '1:SX',
        errormsgpv = pvpref + '1:SX-MsgTxt',
        precision = 0.5,
        can_disable = True,
        auto_enable = True,
    ),
    sy = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample Y translation',
        motorpv = pvpref + '1:SY',
        errormsgpv = pvpref + '1:SY-MsgTxt',
        precision = 0.5,
        can_disable = True,
        auto_enable = True,
    ),
    sz = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample lift',
        motorpv = pvpref + '1:SZ',
        errormsgpv = pvpref + '1:SZ-MsgTxt',
        precision = 0.5,
        can_disable = True,
        auto_enable = True,
    ),
    stt = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Two Theta detector',
        motorpv = pvpref + '1:STT',
        errormsgpv = pvpref + '1:STT-MsgTxt',
        precision = 0.5,
        can_disable = True,
        auto_enable = True,
    ),
    chi = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'CHI rotation',
        motorpv = pvpref + '2:SCH',
        errormsgpv = pvpref + '2:SCH-MsgTxt',
        precision = 0.5,
        can_disable = True,
        auto_enable = True,
    ),
    phi = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'PHI rotation',
        motorpv = pvpref + '2:SPH',
        errormsgpv = pvpref + '2:SPH-MsgTxt',
        precision = 0.5,
        userlimits = (-180, 180),
        can_disable = True,
        auto_enable = True,
    ),
)
"""
    Not available most of the time
    sgl = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample lower goniometer',
        motorpv = pvpref + '1:SGL',
        errormsgpv = pvpref + '1:SGL-MsgTxt',
        precision = 0.5,
        can_disable = True,
        auto_enable = True,
    ),
    sgu = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample upper goniometer',
        motorpv = pvpref + '1:SGU',
        errormsgpv = pvpref + '1:SGU-MsgTxt',
        precision = 0.5,
        can_disable = True,
        auto_enable = True,
    ),
"""
alias_config = {'om': {'om_raw': 10, 'se_om': 20}}
