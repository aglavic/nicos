description = 'sample table'
group = 'lowlevel'

devices = dict(
    phi      = device('devices.taco.HoveringAxis',
                      description = 'sample two-theta',
                      tacodevice = '//mirasrv/mira/axis/phi',
                      abslimits = (-120, 120),
                      startdelay = 1,
                      stopdelay = 2,
                      switch = 'air_sample',
                      switchvalues = (0, 1),
                      fmtstr = '%.3f'),

    air_mono   = device('devices.taco.DigitalOutput',
                        tacodevice = '//mirasrv/mira/phytronio/air_mono',
                        lowlevel = True),

    air_sample = device('mira.refcountio.RefcountDigitalOutput',
                        tacodevice = '//mirasrv/mira/phytronio/air_sample',
                        lowlevel = True),

    air_ana    = device('mira.refcountio.RefcountDigitalOutput',
                        tacodevice = '//mirasrv/mira/phytronio/air_det',
                        lowlevel = True),

    om       = device('mira.axis.PhytronAxis',
                      description = 'sample theta',
                      tacodevice = '//mirasrv/mira/axis/om',
                      abslimits = (-180, 180),
                      fmtstr = '%.3f'),
    stx      = device('mira.axis.PhytronAxis',
                      description = 'sample translation along the beam',
                      tacodevice = '//mirasrv/mira/axis/stx',
                      abslimits = (-25, 25),
                      fmtstr = '%.2f'),
    sty      = device('mira.axis.PhytronAxis',
                      description = 'horizontal sample translation',
                      tacodevice = '//mirasrv/mira/axis/sty',
                      abslimits = (-25, 25),
                      fmtstr = '%.2f'),
    stz      = device('mira.axis.PhytronAxis',
                      description = 'vertical sample translation',
                      tacodevice = '//mirasrv/mira/axis/stz',
                      abslimits = (0, 40),
                      fmtstr = '%.2f'),
    sgx      = device('mira.axis.PhytronAxis',
                      description = 'sample tilt around beam axis',
                      tacodevice = '//mirasrv/mira/axis/sgx',
                      abslimits = (-5, 5),
                      fmtstr = '%.2f'),
    sgy      = device('mira.axis.PhytronAxis',
                      description = 'sample tilt orthogonal to beam axis',
                      tacodevice = '//mirasrv/mira/axis/sgy',
                      abslimits = (-5, 5),
                      fmtstr = '%.2f'),
)
