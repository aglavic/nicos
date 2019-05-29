description = 'Devices for configuring the EMBL detectors Histogram Memory'

devices = dict(
    hm_connector = device('nicos_sinq.devices.sinqhm.connector.HttpConnector',
        description = "Connector for Histogram Memory Server",
        byteorder = configdata('config.HISTOGRAM_MEMORY_ENDIANESS'),
        baseurl = configdata('config.ZEBRAHM_URL'),
        base64auth = 'c3B5OjAwNw==',
        visibility = (),
    ),
    hm_b0_ax_x = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfAxis',
        description = 'Axis x',
        visibility = (),
        length = 256,
        mapping = 'calculate',
        preoffset = -2048,
        divisor = int(4096 / 256),
        label = 'X',
        unit = 'pixel',
        bins = [
            -95, -94.2578, -93.5156, -92.7734, -92.0312, -91.2891, -90.5469,
            -89.8047, -89.0625, -88.3203, -87.5781, -86.8359, -86.0938,
            -85.3516, -84.6094, -83.8672, -83.125, -82.3828, -81.6406, -80.8984,
            -80.1562, -79.4141, -78.6719, -77.9297, -77.1875, -76.4453,
            -75.7031, -74.9609, -74.2188, -73.4766, -72.7344, -71.9922, -71.25,
            -70.5078, -69.7656, -69.0234, -68.2812, -67.5391, -66.7969,
            -66.0547, -65.3125, -64.5703, -63.8281, -63.0859, -62.3438,
            -61.6016, -60.8594, -60.1172, -59.375, -58.6328, -57.8906, -57.1484,
            -56.4062, -55.6641, -54.9219, -54.1797, -53.4375, -52.6953,
            -51.9531, -51.2109, -50.4688, -49.7266, -48.9844, -48.2422, -47.5,
            -46.7578, -46.0156, -45.2734, -44.5312, -43.7891, -43.0469,
            -42.3047, -41.5625, -40.8203, -40.0781, -39.3359, -38.5938,
            -37.8516, -37.1094, -36.3672, -35.625, -34.8828, -34.1406, -33.3984,
            -32.6562, -31.9141, -31.1719, -30.4297, -29.6875, -28.9453,
            -28.2031, -27.4609, -26.7188, -25.9766, -25.2344, -24.4922, -23.75,
            -23.0078, -22.2656, -21.5234, -20.7812, -20.0391, -19.2969,
            -18.5547, -17.8125, -17.0703, -16.3281, -15.5859, -14.8438,
            -14.1016, -13.3594, -12.6172, -11.875, -11.1328, -10.3906, -9.64844,
            -8.90625, -8.16406, -7.42188, -6.67969, -5.9375, -5.19531, -4.45312,
            -3.71094, -2.96875, -2.22656, -1.48438, -0.742188, 0, 0.742188,
            1.48438, 2.22656, 2.96875, 3.71094, 4.45312, 5.19531, 5.9375,
            6.67969, 7.42188, 8.16406, 8.90625, 9.64844, 10.3906, 11.1328,
            11.875, 12.6172, 13.3594, 14.1016, 14.8438, 15.5859, 16.3281,
            17.0703, 17.8125, 18.5547, 19.2969, 20.0391, 20.7812, 21.5234,
            22.2656, 23.0078, 23.75, 24.4922, 25.2344, 25.9766, 26.7188,
            27.4609, 28.2031, 28.9453, 29.6875, 30.4297, 31.1719, 31.9141,
            32.6562, 33.3984, 34.1406, 34.8828, 35.625, 36.3672, 37.1094,
            37.8516, 38.5938, 39.3359, 40.0781, 40.8203, 41.5625, 42.3047,
            43.0469, 43.7891, 44.5312, 45.2734, 46.0156, 46.7578, 47.5, 48.2422,
            48.9844, 49.7266, 50.4688, 51.2109, 51.9531, 52.6953, 53.4375,
            54.1797, 54.9219, 55.6641, 56.4062, 57.1484, 57.8906, 58.6328,
            59.375, 60.1172, 60.8594, 61.6016, 62.3438, 63.0859, 63.8281,
            64.5703, 65.3125, 66.0547, 66.7969, 67.5391, 68.2812, 69.0234,
            69.7656, 70.5078, 71.25, 71.9922, 72.7344, 73.4766, 74.2188,
            74.9609, 75.7031, 76.4453, 77.1875, 77.9297, 78.6719, 79.4141,
            80.1562, 80.8984, 81.6406, 82.3828, 83.125, 83.8672, 84.6094,
            85.3516, 86.0938, 86.8359, 87.5781, 88.3203, 89.0625, 89.8047,
            90.5469, 91.2891, 92.0312, 92.7734, 93.5156, 94.2578, 95
        ]
    ),
    hm_b0_ax_y = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfAxis',
        description = 'Axis Y',
        visibility = (),
        length = 128,
        mapping = 'calculate',
        preoffset = -2048,
        divisor = int(4096 / 128),
        label = 'Y',
        unit = 'mm',
        bins = [
            -95.0, -93.515625, -92.03125, -90.546875, -89.0625, -87.578125,
            -86.09375, -84.609375, -83.125, -81.640625, -80.15625, -78.671875,
            -77.1875, -75.703125, -74.21875, -72.734375, -71.25, -69.765625,
            -68.28125, -66.796875, -65.3125, -63.828125, -62.34375, -60.859375,
            -59.375, -57.890625, -56.40625, -54.921875, -53.4375, -51.953125,
            -50.46875, -48.984375, -47.5, -46.015625, -44.53125, -43.046875,
            -41.5625, -40.078125, -38.59375, -37.109375, -35.625, -34.140625,
            -32.65625, -31.171875, -29.6875, -28.203125, -26.71875, -25.234375,
            -23.75, -22.265625, -20.78125, -19.296875, -17.8125, -16.328125,
            -14.84375, -13.359375, -11.875, -10.390625, -8.90625, -7.421875,
            -5.9375, -4.453125, -2.96875, -1.484375, 0.0, 1.484375, 2.96875,
            4.453125, 5.9375, 7.421875, 8.90625, 10.390625, 11.875, 13.359375,
            14.84375, 16.328125, 17.8125, 19.296875, 20.78125, 22.265625, 23.75,
            25.234375, 26.71875, 28.203125, 29.6875, 31.171875, 32.65625,
            34.140625, 35.625, 37.109375, 38.59375, 40.078125, 41.5625,
            43.046875, 44.53125, 46.015625, 47.5, 48.984375, 50.46875,
            51.953125, 53.4375, 54.921875, 56.40625, 57.890625, 59.375,
            60.859375, 62.34375, 63.828125, 65.3125, 66.796875, 68.28125,
            69.765625, 71.25, 72.734375, 74.21875, 75.703125, 77.1875,
            78.671875, 80.15625, 81.640625, 83.125, 84.609375, 86.09375,
            87.578125, 89.0625, 90.546875, 92.03125, 93.515625, 95
        ]
    ),
    hm_tof_array = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfArray',
        data = [0, 20000],
        tag = 'tof',
        formatter = '%9d',
        dim = [
            2,
        ],
        description = 'TOF Array',
        visibility = (),
    ),
    hm_ax_tof = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfAxis',
        description = 'TOF axis',
        visibility = (),
        mapping = 'boundary',
        array = 'hm_tof_array',
        label = 'TOF',
        unit = 'ms'
    ),
    hm_bank0 = device('nicos_sinq.devices.sinqhm.configurator.HistogramConfBank',
        description = 'EMBL HM',
        visibility = (),
        bankid = 0,
        axes = ['hm_b0_ax_x', 'hm_b0_ax_y', 'hm_ax_tof']
    ),
    hm_configurator = device('nicos_sinq.devices.sinqhm.configurator.ConfiguratorBase',
        description = 'Configurator for the histogram memory',
        filler = 'psd',
        mask = '0x00F00000',
        active = '0x00E00000',
        increment = 1,
        banks = ['hm_bank0'],
        connector = 'hm_connector'
    ),
)
