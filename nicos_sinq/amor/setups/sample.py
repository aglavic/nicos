description = 'Sample devices in the SINQ AMOR.'

group = 'lowlevel'

pvprefix = 'SQ:AMOR:mota:'

devices = dict(
    som=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Sample omega motor',
               motorpv=pvprefix + 'som',
               errormsgpv=pvprefix + 'som-MsgTxt',
               ),
    soz=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Sample z lift of base motor',
               motorpv=pvprefix + 'soz',
               errormsgpv=pvprefix + 'soz-MsgTxt',
               ),
    stz=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Sample z translation on sample table motor',
               motorpv=pvprefix + 'stz',
               errormsgpv=pvprefix + 'stz-MsgTxt',
               ),
    sch=device('nicos_ess.devices.epics.motor.EpicsMotor',
               epicstimeout=3.0,
               description='Sample chi motor',
               motorpv=pvprefix + 'sch',
               errormsgpv=pvprefix + 'sch-MsgTxt',
               ),
    hsy_switch=device(
        'nicos_sinq.amor.devices.epics_amor_magnet.EpicsAmorMagnetSwitch',
        description='Switch to turn magnet on/off',
        readpv='SQ:AMOR:FMA:PowerStatusRBV',
        writepv='SQ:AMOR:FMA:PowerStatus',
        mapping={'on': 1, 'off': 0},
        ),
    hsy=device('nicos_sinq.amor.devices.epics_amor_magnet.EpicsAmorMagnet',
               epicstimeout=3.0,
               description='Sample magnet',
               basepv='SQ:AMOR:FMA',
               pvdelim=':',
               precision=0.1,
               timeout=None,
               window=3.0,
               fieldfactor=150.0/10000.0,
               unit='Oe',
               switch='hsy_switch'
               ),
)
