description = 'setup for the right status monitor'
group = 'special'

# location: cabin, top right

_column1 = Column(
    Block('Heater long-term', [
        BlockRow(
            Field(plot='TPower', dev='t/heaterpower', width=40, height=30,
                  plotwindow=24*3600),
        ),
        ],
        setups='htf01',
    ),
    Block('Heater short-term', [
        BlockRow(
            Field(plot='TPower2', dev='t/heaterpower', width=40, height=25,
                  plotwindow=1800),
        ),
        ],
        setups='htf01',
    ),
    Block('MIEZE', [
        BlockRow(
            Field(name='Echotime', dev='echotime', unit='ns', width=22),
        ),
        BlockRow(
            Field(dev='hrf1'),
            Field(name='freq1', dev='cbox1_fg_freq'),
            Field(name='amp1', dev='cbox1_fg_amp'),
            Field(name='coil1', dev='cbox1_coil_rms'),
        ),
        BlockRow(
            Field(dev='hrf2'),
            Field(name='freq2', dev='cbox2_fg_freq'),
            Field(name='amp2', dev='cbox2_fg_amp'),
            Field(name='coil2', dev='cbox2_coil_rms'),
        ),
        BlockRow(
            Field(name='fp1', dev='cbox1_fwdp'),
            Field(name='fp2', dev='cbox2_fwdp'),
            Field(name='rp1', dev='cbox1_revp'),
            Field(name='rp2', dev='cbox2_revp'),
        ),
        BlockRow(
            Field(dev='hsf1'),
            Field(dev='sf1'),
            Field(dev='hsf2'),
            Field(dev='sf2'),
        ),
        BlockRow(
            Field(name='f_chop', dev='psd_chop_freq', format='%g'),
            Field(name='f_timebin', dev='psd_timebin_freq', format='%g'),
        ),
        ],
        setups='mieze'
    ),
    Block('TAS display', [
        BlockRow(
            Field(widget='nicos.guisupport.tas.TasWidget', width=30, height=18,
                  mthdev='m2th', mttdev='m2tt', sthdev='sth', sttdev='stt',
                  athdev='ath', attdev='att'),
        ),
        ],
        setups='tas',
    ),
    Block('MIRA Magnet', [
        BlockRow(
            Field(dev='I'),
            Field(dev='B'),
        ),
        BlockRow(
            Field(name='T1', dev='miramagnet_T1', width=6, format='%d'),
            Field(name='T2', dev='miramagnet_T2', width=6, format='%d'),
        ),
        BlockRow(
            Field(name='T3', dev='miramagnet_T3', width=6, format='%d'),
            Field(name='T4', dev='miramagnet_T4', width=6, format='%d'),
        ),
        ],
        setups='miramagnet',
    ),
    Block('Garfield Magnet', [
        BlockRow(
            Field(name='on/off', dev='garfield_onoff'),
        ),
        BlockRow(
            Field(dev='I_garfield'),
        ),
        ],
        setups='garfield',
    ),
    SetupBlock('ccm5v5'),
    SetupBlock('ccm5v5', 'temperatures'),
    Block('SANS-1 Magnet', [
        BlockRow(
            Field(dev='B'),
            Field(name='T2', dev='ccmsans_T2', width=6),
            Field(name='T3', dev='ccmsans_T3', width=6),
        ),
        BlockRow(
            Field(name='T4', dev='ccmsans_T4', width=6),
            Field(name='T5', dev='ccmsans_T5', width=6),
            Field(name='T6', dev='ccmsans_T6', width=6),
        ),
        ],
        setups='ccmsans',
    ),
    Block('2.2T Magnet (HTS)', [
        BlockRow(
            Field(name='Target', dev='B_ccm2a'),
            Field(name='Readback', dev='B_ccm2a_readback'),
        ),
        ],
        setups='ccm2a',
    ),
    Block('12T Magnet', [
        BlockRow(
            Field(name='Field', dev='B_ccm12v'),
            Field(name='Current', dev='I_ccm12v_supply'),
        ),
        BlockRow(
            Field(name='T Stick', dev='T_ccm12v_stick'),
            Field(name='T VTI', dev='T_ccm12v_vti'),
            Field(name='T NV', dev='T_ccm12v_nv'),
        ),
        BlockRow(
            Field(name='LHe', dev='ccm12v_LHe'),
            Field(name='T magnet', dev='ccm12v_Tmag'),
        ),
        ],
        setups='ccm12v',
    ),
    Block('3He cell', [
        BlockRow(
            Field(name='Polarization', dev='pol', width=7),
            Field(name='Guide field', dev='He_GF'),
        ),
        ],
        setups='helios',
    ),
    Block('Y-Z table axes', [
        BlockRow(
            Field(dev='dty'),
            Field(dev='dtz'),
        ),
        ],
        setups='yztable',
    ),
    Block('Auxiliary currents', [
        BlockRow(
            Field(dev='Ipol1'),
            Field(dev='Ipol2'),
        ),
        ],
        setups='hpesupply',
    ),

    Block('TTi + Huber', [
        BlockRow(
            Field(dev='dct1'),
            Field(dev='dct2'),
            Field(dev='flip', width=5),
        ),
        BlockRow(
            Field(dev='tbl1'),
            Field(dev='tbl2'),
        ),
        ],
        setups='mezeiflip',
    ),
    Block('TTi + Huber 2', [
        BlockRow(
            Field(dev='dct3'),
            Field(dev='dct4'),
            Field(dev='flipx', width=5),
        ),
        ],
        setups='mezeiflip2',
    ),
    Block('Guidefield coil', [
        BlockRow(
            Field(dev='dct5'),
            Field(dev='dct6'),
        ),
        ],
        setups='gfcoil',
    ),
    Block('HV Stick', [
        BlockRow(
            Field(dev='HV'),
        ),
        ],
        setups='hvstick',
    ),
    Block('Gas pressure cell', [
        BlockRow(
            Field(dev='diptron3plus'),
            Field(dev='sentronicplus'),
        ),
        ],
        setups='gascell',
    ),
)

_column2 = Column(
    Block('Eulerian cradle', [
        BlockRow(
            Field(dev='echi'),
            Field(dev='ephi'),
        ),
        # BlockRow(
        #     Field(dev='ec', name='Scattering plane', width=20, istext=True),
        # ),
        ],
        setups='euler',
    ),
    Block('Sample rotation (rsc03', [
        BlockRow(
            Field(dev='sth_rsc03'),
        ),
        ],
        setups='rsc03',
    ),
    Block('Cryostat (CCR5)', [
        BlockRow(
            Field(name='Setpoint', key='T_ccr5/setpoint', unitkey='T_ccr5/unit',
                  format='%.2f'),
            Field(name='A', dev='T_ccr5_A'),
            Field(name='B', dev='T_ccr5_B'),
            Field(name='C', dev='T_ccr5_C'),
        ),
        BlockRow(
            Field(name='P', key='t/p'),
            Field(name='I', key='t/i'),
            Field(name='D', key='t/d'),
            Field(name='p', dev='ccr5_p1'),
        ),
        ],
        setups='ccr5',
    ),
    Block('Cryostat (CCR11)', [
        BlockRow(
            Field(name='Setpoint', key='t/setpoint', unitkey='t/unit',
                  format='%.2f'),
            Field(name='Control', dev='T'),
            Field(dev='Ts', name='Sample'),
        ),
        BlockRow(
            Field(name='A', dev='T_ccr11_A'),
            Field(name='B', dev='T_ccr11_B'),
            Field(name='C', dev='T_ccr11_C'),
            Field(name='D', dev='T_ccr11_D'),
        ),
        BlockRow(
            Field(name='P', key='t/p'),
            Field(name='I', key='t/i'),
            Field(name='D', key='t/d'),
            Field(name='p', dev='ccr11_p1'),
        ),
        ],
        setups='ccr11',
    ),
    Block('Cryostat (CCR21)', [
        BlockRow(
            Field(name='Setpoint', key='t/setpoint', unitkey='t/unit',
                  format='%.2f'),
            Field(name='Control', dev='T'),
            Field(dev='Ts', name='Sample'),
        ),
        BlockRow(
            Field(name='A', dev='T_ccr21_A'),
            Field(name='B', dev='T_ccr21_B'),
            Field(name='C', dev='T_ccr21_C'),
            Field(name='D', dev='T_ccr21_D'),
        ),
        BlockRow(
            Field(name='P', key='t_ccr21_tube/p'),
            Field(name='I', key='t_ccr21_tube/i'),
            Field(name='D', key='t_ccr21_tube/d'),
            Field(name='p', dev='ccr21_p1'),
        ),
        ],
        setups='ccr21',
    ),
    Block('Furnace (HTF01)', [
        BlockRow(
            Field(name='Setpoint', key='t_htf01/setpoint', unitkey='t_htf01/unit',
                  format='%.2f'),
            Field(name='Temp', dev='T_htf01')),
        BlockRow(
            Field(name='P', key='t_htf01/p'),
            Field(name='I', key='t_htf01/i'),
            Field(name='D', key='t_htf01/d'),
        ),
        BlockRow(
            Field(name='Heater power', key='t_htf01/heaterpower', unit='%',
                  format='%.2f'),
            Field(name='Vacuum', dev='htf01_p'),
        ),
        ],
        setups='htf01',
    ),
    Block('Furnace (HTF20)', [
        BlockRow(
            Field(name='Setpoint', key='t_htf20/setpoint', unitkey='t_htf20/unit',
                  format='%.2f'),
            Field(name='Temp', dev='T_htf20'),
        ),
        BlockRow(
            Field(name='P', key='t_htf20/p'),
            Field(name='I', key='t_htf20/i'),
            Field(name='D', key='t_htf20/d'),
        ),
        BlockRow(
            Field(name='Heater output', key='t_htf20/heateroutput', unit='%',
                  format='%.2f'),
            Field(name='Vacuum', dev='vacuum_htf20'),
        ),
        ],
        setups='htf20',
    ),
    Block('Furnace (HTF03)', [
        BlockRow(
            Field(name='Setpoint', key='t_htf03/setpoint', unitkey='t_htf03/unit',
                  format='%.2f'),
            Field(name='Temp', dev='T_htf03'),
        ),
        BlockRow(
            Field(name='P', key='t_htf03/p'),
            Field(name='I', key='t_htf03/i'),
            Field(name='D', key='t_htf03/d'),
        ),
        BlockRow(
            Field(name='Heater power', key='t_htf03/heaterpower', unit='%',
                  format='%.2f'),
            Field(name='Vacuum', dev='htf03_p'),
        ),
        ],
        setups='htf03',
    ),
    Block('Furnace (IRF01)', [
        BlockRow(
            Field(name='Setpoint', key='t_irf01/setpoint', unitkey='t_irf01/unit',
                  format='%.2f'),
            Field(name='Temp', dev='T_irf01'),
        ),
        BlockRow(
            Field(name='P', key='t_irf01/p'),
            Field(name='I', key='t_irf01/i'),
            Field(name='D', key='t_irf01/d'),
        ),
        BlockRow(
            Field(name='Heater power', key='t_irf01/heaterpower', unit='%',
                  format='%.2f'),
        ),
        ],
        setups='irf01',
    ),
    SetupBlock('cci3he01'), SetupBlock('cci3he01', 'pressures'),
    SetupBlock('cci3he02'), SetupBlock('cci3he02', 'pressures'),
    SetupBlock('cci3he03'), SetupBlock('cci3he03', 'pressures'),
    SetupBlock('cci3he10'), SetupBlock('cci3he10', 'pressures'),
    SetupBlock('ccidu01'), SetupBlock('ccidu01', 'pressures'),
    SetupBlock('ccidu02'), SetupBlock('ccidu02', 'pressures'),
    Block('Humidity Julabo', [
        BlockRow(
            Field(name='Setpoint', key='t_julabo/setpoint', unitkey='t/unit',
                  format='%.2f'),
            Field(name='T', dev='T_julabo'),
        ),
        ],
        setups='julabo',
    ),
)

_column3 = Column(
    # Block('Temperature long-term', [
    #     BlockRow(
    #         Field(plot='TT', dev='T', width=40, height=30, plotwindow=24*3600),
    #         Field(plot='TT', dev='Ts'),
    #         Field(plot='TT', key='t/setpoint'),
    #     ),
    #     ],
    # ),
    # Block('Temperature short-term', [
    #     BlockRow(
    #         Field(plot='TT2', dev='T', width=40, height=25, plotwindow=1800),
    #         Field(plot='TT2', dev='Ts'),
    #         Field(plot='TT2', key='t/setpoint'),
    #     ),
    #     ],
    # ),
)

devices = dict(
    Monitor = device('nicos.services.monitor.qt.Monitor',
        title = 'MIRA Sample environment',
        loglevel = 'info',
        cache = 'miractrl.mira.frm2:14869',
        prefix = 'nicos/',
        font = 'Droid Sans',
        valuefont = 'Droid Sans Mono',
        fontsize = 22,
        padding = 5,
        layout = [[_column1, _column2, _column3]]
    )
)
