description = 'pressure filter readout'

group = 'lowlevel'

devices = dict(
    # p_in_filter = device('nicos_mlz.sans1.devices.wut.WutValue',
    #     hostname = 'sans1wut-p-diff-fak40.sans1.frm2',
    #     port = '1',
    #     description = 'pressure in front of filter',
    #     fmtstr = '%.2F',
    #     loglevel = 'info',
    #     unit = 'bar',
    # ),
    # p_out_filter = device('nicos_mlz.sans1.devices.wut.WutValue',
    #     hostname = 'sans1wut-p-diff-fak40.sans1.frm2',
    #     port = '2',
    #     description = 'pressure behind of filter',
    #     fmtstr = '%.2F',
    #     loglevel = 'info',
    #     unit = 'bar',
    # ),
    # p_diff_filter = device('nicos_mlz.sans1.devices.wut.WutDiff',
    #     description = 'pressure in front of filter minus pressure behind filter',
    #     dev1 = 'p_in_filter',
    #     dev2 = 'p_out_filter',
    #     fmtstr = '%.2F',
    #     loglevel = 'info',
    #     unit = 'bar',
    # ),
)
