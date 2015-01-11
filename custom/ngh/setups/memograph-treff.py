description = 'memograph readout'
devices = dict(
    t_in_memograph_treff = device('frm2.memograph.MemographValue',
                                  hostname = 'memograph04.care.frm2',
                                  group = 2,
                                  valuename = 'T_in TREFF',
                                  description = 'inlet temperature memograph',
                                 ),
    t_out_memograph_treff = device('frm2.memograph.MemographValue',
                                   hostname = 'memograph04.care.frm2',
                                   group = 2,
                                   valuename = 'T_out TREFF',
                                   description = 'outlet temperature memograph',
                                  ),
    t_diff_memograph_treff = device('frm2.memograph.MemographValue',
                                    hostname = 'memograph04.care.frm2',
                                    group = 2,
                                    valuename = 'T_diff TREFF',
                                    description = 'temperature difference memograph',
                                   ),
    p_in_memograph_treff = device('frm2.memograph.MemographValue',
                                  hostname = 'memograph04.care.frm2',
                                  group = 2,
                                  valuename = 'P_in TREFF',
                                  description = 'inlet pressure memograph',
                                 ),
    p_out_memograph_treff = device('frm2.memograph.MemographValue',
                                   hostname = 'memograph04.care.frm2',
                                   group = 2,
                                   valuename = 'P_out TREFF',
                                   description = 'outlet pressure memograph',
                                  ),
    flow_in_memograph_treff = device('frm2.memograph.MemographValue',
                                     hostname = 'memograph04.care.frm2',
                                     group = 2,
                                     valuename = 'FLOW_in TREFF',
                                     description = 'inlet flow memograph',
                                    ),
    leak_memograph_treff = device('frm2.memograph.MemographValue',
                                  hostname = 'memograph04.care.frm2',
                                  group = 2,
                                  valuename = 'Leak TREFF',
                                  description = 'leakage memograph',
                                 ),
    cooling_memograph_treff = device('frm2.memograph.MemographValue',
                                     hostname = 'memograph04.care.frm2',
                                     group = 2,
                                     valuename = 'Cooling TREFF',
                                     description = 'cooling power memograph',
                                    ),
)
