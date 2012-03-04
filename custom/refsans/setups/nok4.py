NOK = 'NOK4'
nok = NOK.lower()
nethost = '//refsanssrv.refsans.frm2/'

description = '%s setup' % (NOK)

includes = ['nokref', 'motorbus', ]

devices = {
        nok + 'portr' : device('nicos.taco.io.AnalogInput',
                               description = 'Voltage input of the %s coder (reactor side)' % (NOK),
                               tacodevice = nethost + 'test/wb_a/2_0', 
                               lowlevel = True,
                              ),
        nok + 'ports' : device('nicos.taco.io.AnalogInput',
                               description = 'Voltage input of the %s coder (sample side)' % (NOK),
                               tacodevice = nethost + 'test/wb_a/2_1',
                               lowlevel = True,
                              ),
        nok + 'obsr'  : device('nicos.refsans.nok.Coder',
                               description = '%s potentiometer coder (reactor side)' % (NOK),
                               mul = 1.002569,
                               off = 36.179259,
                               snr = 6509,
                               sensitivity = 3.852,
                               port = nok + 'portr',
                               ref = 'nrefa2',
                               lowlevel = True,
                              ),
        nok + 'obss'  : device('nicos.refsans.nok.Coder',
                               description = '%s potentiometer coder (sample side)' % (NOK),
                               mul = 0.998362,
                               off = 4.822946,
                               snr = 6504,
                               sensitivity = 3.856,
                               port = nok + 'ports',
                               ref = 'nrefa2',
                               lowlevel = True,
                              ),
        nok + 'motorr' : device('nicos.taco.motor.Motor',
                               description = 'Motor of the %s (reactor side)' % NOK,
                               tacodevice = nethost + 'test/' + nok + '/mr',
                               lowlevel = True,
                              ),
        nok + 'motors' : device('nicos.taco.motor.Motor',
                               description = 'Motor of the %s (sample side)' % NOK,
                               tacodevice = nethost + 'test/' + nok + '/ms',
                               lowlevel = True,
                              ),
         nok + 'sllr' : device('nicos.taco.io.DigitalInput',
                              description = 'low limit switch of %s (reactor side)' % NOK,
                              tacodevice = nethost + 'test/' + nok + '/srll',
                              lowlevel = True,
                             ),
         nok + 'shlr' : device('nicos.taco.io.DigitalInput',
                              description = 'high limit switch of %s (reactor side)' % NOK,
                              tacodevice = nethost + 'test/' + nok + '/srhl',
                              lowlevel = True,
                             ),
         nok + 'srefr' : device('nicos.taco.io.DigitalInput',
                               description = 'reference switch of %s (reactor side)' % NOK,
                               tacodevice = nethost + 'test/' + nok + '/srref',
                               lowlevel = True,
                              ),
         nok + 'slls' : device('nicos.taco.io.DigitalInput',
                              description = 'low limit switch of %s (sample side)' % NOK,
                              tacodevice = nethost + 'test/' + nok + '/ssll',
                              lowlevel = True,
                             ),
         nok + 'shls' : device('nicos.taco.io.DigitalInput',
                              description = 'high limit switch of %s (sample side)' % NOK,
                              tacodevice = nethost + 'test/' + nok + '/sshl',
                              lowlevel = True,
                             ),
         nok + 'srefs' : device('nicos.taco.io.DigitalInput',
                               description = 'reference switch of %s (sample side)' % NOK,
                               tacodevice = nethost + 'test/' + nok + '/ssref',
                               lowlevel = True,
                              ),
         nok + 'axisr' : device('nicos.refsans.nok.Axis',
                               description = '%s Axis (reactor side)' % NOK,
                               motor = nok + 'motorr', 
                               coder = nok + 'motorr', 
                               obs = [nok + 'obsr', ],
                               bus = 'motorbus2',
                               sll = nok + 'sllr',
                               shl = nok + 'shlr',
                               sref = nok + 'srefr',
                               backlash = -2.0,
                               precision = 0.05,
                               refpoint = 20.983,
                              ),
         nok + 'axiss' : device('nicos.refsans.nok.Axis',
                               description = '%s Axis (sample side)' % NOK,
                               motor = nok + 'motors', 
                               coder = nok + 'motors', 
                               obs = [nok + 'obss', ],
                               bus = 'motorbus2',
                               sll = nok + 'slls',
                               shl = nok + 'shls',
                               sref = nok + 'srefs',
                               backlash = -2.0,
                               precision = 0.05,
                               refpoint = 9.703,
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



