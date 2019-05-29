description = 'Devices for configuring Histogram Memory'
excludes=['hm_config']

devices = dict(
    hm_connector=device(
        'nicos_sinq.devices.sinqhm.connector.HttpConnector',
        description="Connector for Histogram Memory Server",
        byteorder=configdata('config.HISTOGRAM_MEMORY_ENDIANESS'),
        baseurl=configdata('config.HISTOGRAM_MEMORY_URL'),
        base64auth='c3B5OjAwNw==',
        visibility=(),
    ),
    hm_b0_ax_x=device(
        'nicos_sinq.devices.sinqhm.configurator.HistogramConfAxis',
        description='First bank axis two theta',
        visibility=(),
        length=1601,
        mapping='direct',
        label='Two Theta',
        unit='degree',
    ),
    hm_ax_tof=device(
        'nicos_sinq.devices.sinqhm.configurator.HistogramConfAxis',
        description='TOF axis',
        visibility=(),
        mapping='calculate',
        preoffset=0,
        length=100,
        divisor=10,
        label='TOF',
        unit='arbitrary'
    ),
    hm_bank0=device(
        'nicos_sinq.devices.sinqhm.configurator.HistogramConfBank',
        description='HM First Bank',
        visibility=(),
        bankid=0,
        axes=['hm_b0_ax_x','hm_ax_tof']
    ),
    hm_configurator=device(
        'nicos_sinq.devices.sinqhm.configurator.ConfiguratorBase',
        description='Configurator for the histogram memory',
        filler='hrpt',
        mask='0x00700000',
        active='0x00600000',
        increment=1,
        banks=['hm_bank0'],
        connector='hm_connector'
    ),
)
