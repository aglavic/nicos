# -*- coding: utf-8 -*-

description = 'GALAXI PIN diodes'

group = 'optional'

display_order = 20

tango_base = 'tango://phys.galaxi.kfa-juelich.de:10000/galaxi/'
tango_analog = tango_base + 'plc_io/'
tango_digital = tango_base + 'fzjdp_digital/'

devices = dict(
    pintimer = device('nicos.devices.entangle.AnalogOutput',
        description = 'Timer for PIN diode counting',
        tangodevice = tango_analog + 'pin_diode_timer',
        unit = 's',
        fmtstr = '%d',
    ),
    pinstate = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Status of PIN diode counting',
        tangodevice = tango_digital + 'StatIntegralPin',
        mapping = {
            'counting': 1,
            'ready': 0
        },
        unit = '',
        fmtstr = '%s',
        lowlevel = True,
    ),
    pincontrol = device('nicos.devices.entangle.DigitalInput',
        description = 'Status control of PIN diode counting',
        tangodevice = tango_digital + 'StatIntegralPin2',
        lowlevel = True,
        unit = '',
    ),
    singledetectors = device('nicos_jcns.galaxi.devices.pindiode.SingleDetectors',
        description = 'Integrated PIN diode values',
        pintimer = 'pintimer',
        pinstate = 'pinstate',
        pincontrol = 'pincontrol',
        pindiodes = [
            'ionichamber1_int', 'ionichamber2_int', 'pindiode1_int',
            'pindiodecal_int', 'pindiodesample_int'
        ],
        fmtstr = '%d',
        unit = 'cts',
    ),
    ionichamber1 = device('nicos.devices.entangle.AnalogInput',
        description = 'Ionisation chamber 1',
        tangodevice = tango_analog + 'ionisation_chamber1',
        fmtstr = '%d',
        unit = 'cts',
    ),
    ionichamber1_int = device('nicos.devices.entangle.AnalogInput',
        description = 'Integral of ionisation chamber 1',
        tangodevice = tango_analog + 'ionisation_chamber1_int',
        fmtstr = '%d',
        unit = 'cts',
    ),
    ionichamber1_off = device('nicos.devices.entangle.AnalogOutput',
        description = 'Offset ionisation chamber 1',
        tangodevice = tango_analog + 'ionisation_chamber1_offset',
        fmtstr = '%d',
        unit = 'cts',
    ),
    ionichamber2 = device('nicos.devices.entangle.AnalogInput',
        description = 'Ionisation chamber 2',
        tangodevice = tango_analog + 'ionisation_chamber2',
        fmtstr = '%d',
        unit = 'cts',
    ),
    ionichamber2_int = device('nicos.devices.entangle.AnalogInput',
        description = 'Integral of ionisation chamber 2',
        tangodevice = tango_analog + 'ionisation_chamber2_int',
        fmtstr = '%d',
        unit = 'cts',
    ),
    ionichamber2_off = device('nicos.devices.entangle.AnalogOutput',
        description = 'Offset of ionisation chamber 2',
        tangodevice = tango_analog + 'ionisation_chamber2_offset',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiode1_move = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Moving of PIN diode in chamber 1',
        tangodevice = tango_digital + 'AbsorberPlate16',
        mapping = {
            'in': 1,
            'out': 0
        },
        fmtstr = '%s',
    ),
    pindiode1 = device('nicos.devices.entangle.AnalogInput',
        description = 'PIN diode in chamber 1',
        tangodevice = tango_analog + 'pin_diode_chamber1',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiode1_int = device('nicos.devices.entangle.AnalogInput',
        description = 'Integral of PIN diode in chamber 1',
        tangodevice = tango_analog + 'pin_diode_chamber1_int',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiode1_off = device('nicos.devices.entangle.AnalogOutput',
        description = 'Offset of PIN diode in chamber 1',
        tangodevice = tango_analog + 'pin_diode_chamber1_offset',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiodesample_move = device('nicos.devices.entangle.NamedDigitalOutput',
        description = 'Moving of PIN diode behind sample place',
        tangodevice = tango_digital + 'PinDiode',
        mapping = {
            'in': 1,
            'out': 2
        },
        fmtstr = '%s',
    ),
    pindiodesample = device('nicos.devices.entangle.AnalogInput',
        description = 'PIN diode behind sample place',
        tangodevice = tango_analog + 'pin_diode_sample',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiodesample_int = device('nicos.devices.entangle.AnalogInput',
        description = 'Integral of PIN diode behind sample place',
        tangodevice = tango_analog + 'pin_diode_sample_int',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiodesample_off = device('nicos.devices.entangle.AnalogOutput',
        description = 'Offset of PIN diode behind sample place',
        tangodevice = tango_analog + 'pin_diode_sample_offset',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiodecal = device('nicos.devices.entangle.AnalogInput',
        description = 'Calibrated PIN diode at sample place',
        tangodevice = tango_analog + 'pin_diode_calibrated',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiodecal_int = device('nicos.devices.entangle.AnalogInput',
        description = 'Integral of calibrated PIN diode at sample place',
        tangodevice = tango_analog + 'pin_diode_calibrated_int',
        fmtstr = '%d',
        unit = 'cts',
    ),
    pindiodecal_off = device('nicos.devices.entangle.AnalogOutput',
        description = 'Offset of calibrated PIN diode at sample place',
        tangodevice = tango_analog + 'pin_diode_calibrated_offset',
        fmtstr = '%d',
        unit = 'cts',
    ),
)
