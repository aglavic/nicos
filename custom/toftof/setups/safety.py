description = 'safety system and shutter'

group = 'lowlevel'

includes = []

nethost = 'toftofsrv.toftof.frm2'

devices = dict(
    saf      = device('toftof.safety.SafetyInputs',
                      description = 'State of the safety control',
                      i7053 = ['i7053_1', 'i7053_2', 'i7053_3'],
                      fmtstr = '0x%012x',
                     ),
    i7053_1  = device('devices.taco.DigitalInput',
                      lowlevel = True,
                      tacodevice = '//%s/toftof/sec/70531' % (nethost,),
                      fmtstr = '0x%04x',
                     ),
    i7053_2  = device('devices.taco.DigitalInput',
                      lowlevel = True,
                      tacodevice = '//%s/toftof/sec/70532' % (nethost,),
                      fmtstr = '0x%04x',
                     ),
    i7053_3  = device('devices.taco.DigitalInput',
                      lowlevel = True,
                      tacodevice = '//%s/toftof/sec/70533' % (nethost,),
                      fmtstr = '0x%04x',
                     ),
    shopen   = device('devices.taco.io.DigitalOutput',
                      tacodevice = '//%s/toftof/shutter/open' % (nethost,),
                      lowlevel = True,
                     ),
    shclose  = device('devices.taco.io.DigitalOutput',
                      tacodevice = '//%s/toftof/shutter/close' % (nethost,),
                      lowlevel = True,
                     ),
    shstatus = device('devices.taco.io.DigitalOutput',
                      tacodevice = '//%s/toftof/shutter/status' % (nethost,),
                      lowlevel = True,
                     ),
    shutter  = device('toftof.safety.Shutter',
                      description = 'Instrument shutter',
                      open = 'shopen',
                      close = 'shclose',
                      status = 'shstatus',
                      unit = '',
                     ),
)
