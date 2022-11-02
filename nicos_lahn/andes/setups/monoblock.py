description = 'monoblocks setup'

group = 'lowlevel'

tango_base = 'tango://lahn:10000/andes/'

devices = dict(
    y1=device('nicos.devices.entangle.Motor',
              description='crystal translation',
              tangodevice=tango_base + 'exchange/y1',
              fmtstr='%.1f',
              requires={'level': 'admin'},
              visibility=(),
              ),
    xi1=device('nicos.devices.entangle.Motor',
               description='crystal inclination',
               tangodevice=tango_base + 'exchange/xi1',
               fmtstr='%.1f',
               requires={'level': 'admin'},
               visibility=(),
               ),
    alpha1=device('nicos.devices.entangle.Motor',
                  description='crystal curved',
                  tangodevice=tango_base + 'exchange/alpha1',
                  fmtstr='%.2f',
                  requires={'level': 'admin'},
                  visibility=(),
                  ),
    y2=device('nicos.devices.entangle.Motor',
              description='crystal translation',
              tangodevice=tango_base + 'exchange/y2',
              fmtstr='%.1f',
              requires={'level': 'admin'},
              visibility=(),
              ),
    xi2=device('nicos.devices.entangle.Motor',
               description='crystal inclination',
               tangodevice=tango_base + 'exchange/xi2',
               fmtstr='%.1f',
               requires={'level': 'admin'},
               visibility=(),
               ),
    alpha2=device('nicos.devices.entangle.Motor',
                  description='crystal curved',
                  tangodevice=tango_base + 'exchange/alpha2',
                  fmtstr='%.2f',
                  requires={'level': 'admin'},
                  visibility=(),
                  ),
    y3=device('nicos.devices.entangle.Motor',
              description='crystal translation',
              tangodevice=tango_base + 'exchange/y3',
              fmtstr='%.1f',
              requires={'level': 'admin'},
              visibility=(),
              ),
    xi3=device('nicos.devices.entangle.Motor',
               description='crystal inclination',
               tangodevice=tango_base + 'exchange/xi3',
               fmtstr='%.1f',
               requires={'level': 'admin'},
               visibility=(),
               ),
    alpha3=device('nicos.devices.entangle.Motor',
                  description='crystal curved',
                  tangodevice=tango_base + 'exchange/alpha3',
                  fmtstr='%.2f',
                  requires={'level': 'admin'},
                  visibility=(),
                  ),
    mb1=device('nicos_lahn.andes.devices.monoexchange.MonoBlock',
               description='moveables devices block',
               tran='y1',
               incl='xi1',
               curv='alpha1',
               fmtstr='tran: %.1f, incl: %.1f, curv: %.1f',
               visibility=(),
               ),
    mb2=device('nicos_lahn.andes.devices.monoexchange.MonoBlock',
               description='moveables devices block',
               tran='y2',
               incl='xi2',
               curv='alpha2',
               fmtstr='tran: %.1f, incl: %.1f, curv: %.1f',
               visibility=(),
               ),
    mb3=device('nicos_lahn.andes.devices.monoexchange.MonoBlock',
               description='moveables devices block',
               tran='y3',
               incl='xi3',
               curv='alpha3',
               fmtstr='tran: %.1f, incl: %.1f, curv: %.1f',
               visibility=(),
               ),
    Si=device('nicos.devices.generic.DeviceAlias',
              alias='mb1',
              ),
    Ge=device('nicos.devices.generic.DeviceAlias',
              alias='mb2',
              ),
    PG=device('nicos.devices.generic.DeviceAlias',
              alias='mb3',
              ),
)
