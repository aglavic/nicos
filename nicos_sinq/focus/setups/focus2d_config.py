description = 'Devices for configuring FOCUS 2 D Histogram Memory'

includes = [
    'detector',
]

devices = dict(
    f2d_connector = device('nicos_sinq.devices.sinqhm.connector.HttpConnector',
        description = "Connector for Histogram Memory Server",
        byteorder = configdata('config.HISTOGRAM_MEMORY_ENDIANESS'),
        baseurl = configdata('config.F2DH_MEMORY_URL'),
        base64auth = 'c3B5OjAwNw==',
        visibility = ()
    ),
    f2d_b0_ax_x = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfAxis',
        description = 'Detector ID',
        visibility = (),
        length = 69,
        mapping = 'direct',
        label = 'Tube-ID',
        unit = '',
    ),
    f2d_array = device('nicos_sinq.focus.devices.detector.Focus2DArray',
        description = 'FOCUS 2D lookup array',
        lookup_file = 'nicos_sinq/focus/set2D_HM.dat',
        dim = [69, 512, 4],
        tag = 'f2d_array',
    ),
    f2d_b0_ax_y = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfAxis',
        description = 'Tube segment ID',
        visibility = (),
        length = 64,
        mapping = 'lookuptable',
        label = 'Tube segment ID',
        unit = '',
        array = 'f2d_array',
    ),
    f2d_bank = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfBank',
        description = 'FOCUS 2D bank',
        visibility = (),
        bankid = 0,
        axes = ['f2d_b0_ax_x', 'f2d_b0_ax_y', 'hm_ax_tof']
    ),
    f2d_configurator = device('nicos_sinq.devices.sinqhm.configurator.ConfiguratorBase',
        description = 'Configurator for FOCUS  2D detector',
        filler = 'tofmap',
        mask = '0x00F0000',
        active = '0x00200000',
        increment = 1,
        banks = ['f2d_bank'],
        connector = 'f2d_connector'
    ),
    f2d_coords = device('nicos_sinq.focus.devices.detector.Focus2DData',
        description = 'Arrays to store with 2D data',
        xdim = 69,
        ydim = 512,
        xval = [],
        yval = [],
        distval = [],
        eqval = [],
        azval = [],
        tthval = [],
    ),
)
