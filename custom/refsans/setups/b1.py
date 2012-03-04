NOK = 'B1'
nok = NOK.lower()
nethost = '//refsanssrv.refsans.frm2/'

description = '%s setup' % (NOK)

includes = ['nokref',]

devices = {
        nok + 'portr' : device('nicos.taco.io.AnalogInput',
                               description = 'Voltage input of the %s coder (reactor side)' % (NOK),
                               tacodevice = nethost + 'test/wb_a/2_2', 
                               lowlevel = True,
                              ),
        nok + 'ports' : device('nicos.taco.io.AnalogInput',
                               description = 'Voltage input of the %s coder (sample side)' % (NOK),
                               tacodevice = nethost + 'test/wb_a/2_3',
                               lowlevel = True,
                              ),
        nok + 'obsr'  : device('nicos.refsans.nok.Coder',
                               description = '%s potentiometer coder (reactor side)' % (NOK),
                               mul = 1.000022,
                               off = 20.953222,
                               snr = 7787,
                               length = 500,
                               sensitivity = 1.922,
                               port = nok + 'portr',
                               ref = 'nrefa2',
                              ),
        nok + 'obss'  : device('nicos.refsans.nok.Coder',
                               description = '%s potentiometer coder (sample side)' % (NOK),
                               mul = 0.999742,
                               off = 13.321479,
                               snr = 7785,
                               length = 500,
                               sensitivity = 1.922,
                               port = nok + 'ports',
                               ref = 'nrefa2',
                              ),
#       nok1 = device('nicos.refsans.nok.Nok', 
#                      unit = 'mm',
#                      fmtstr = '%.5f',
#                      bus = 'motorbus2',
#                      motor = nethost + 'test/nok1/ngm',
#                      encoder = nethost + 'test/nok1/nge',
#                      refswitch = nethost + 'test/nok1/ngsref',
#                      lowlimitswitch = [nethost + 'test/nok1/ngsll',],
#                      highlimitswitch = [nethost + 'test/nok1/ngshl',],
#                      #refpos = [-14.419, ],
#                      refpos = [-14.729 ], #JFM07_06_2010
#                      backlash = 2,
#                      posinclination = 0,
#                      neginclination = 0,
#                     ),
         }



