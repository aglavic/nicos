description = 'BATAN virtual triple-axis spectrometer SN1'
group = 'basic'

modules = ['nicos.commands.tas']

includes = ['source']

sysconfig = dict(
    instrument = 'tas',
    datasinks = ['filesink'],
)

devices = dict(
    tas = device('nicos.devices.tas.TAS',
        description = 'BATAN virtual triple-axis spectrometer SN1',
        instrument = 'VTAS',
        responsible = 'Iwan Sumirat <iwansumirat@gmail.com>',
        website = 'http://www.batan.go.id/index.php/id/fasilitas-pstbm',
        operators = ['BATAN SN1 developer team'],
        facility = 'Neutron Scattering Laboratory - National Nuclear Energy Agency of Indonesia, BATAN',
        energytransferunit = 'meV',
        scatteringsense = (1, -1, 1),
        axiscoupling = False,
        collimation = '60 40 40 60',
        cell = 'Sample',
        phi = 'phi',
        psi = 'sth',
        mono = 'mono',
        ana = 'ana',
        alpha = None,
    ),
    phi = device('nicos.devices.generic.VirtualMotor',
        description = 'sample scattering angle',
        abslimits = (-180, 180),
        unit = 'deg',
        speed = 1,
    ),
    alpha = device('nicos.devices.generic.VirtualMotor',
        description = 'angle between ki and q',
        abslimits = (0, 50),
        unit = 'deg',
    ),
    sth = device('nicos.devices.generic.DeviceAlias',
        alias = 'psi',
    ),
    psi = device('nicos.devices.generic.VirtualMotor',
        description = 'sample rotation angle',
        abslimits = (-180, 180),
        unit = 'deg',
        speed = 2,
    ),
    mono = device('nicos.devices.tas.Monochromator',
        description = 'monochromator wavevector',
        unit = 'A-1',
        dvalue = 3.355,
        theta = 'mth',
        twotheta = 'mtt',
        focush = None,
        focusv = None,
        abslimits = (0.1, 10),
        warnlimits = (1.0, 3.0),
        crystalside = -1,
    ),
    mth = device('nicos.devices.generic.VirtualMotor',
        description = 'monochromator rocking angle',
        unit = 'deg',
        abslimits = (0, 37),
        precision = 0.05,
        speed = 0.5,
    ),
    mtt = device('nicos.devices.generic.VirtualMotor',
        description = 'monochromator scattering angle',
        unit = 'deg',
        abslimits = (0, 75),
        precision = 0.05,
        speed = 0.5,
    ),
    ana = device('nicos.devices.tas.Monochromator',
        description = 'analyzer wavevector',
        unit = 'A-1',
        dvalue = 3.355,
        theta = 'ath',
        twotheta = 'att',
        focush = None,
        focusv = None,
        abslimits = (0.1, 10),
        crystalside = -1,
    ),
    ath = device('nicos.devices.generic.VirtualMotor',
        description = 'analyzer rocking angle',
        unit = 'deg',
        abslimits = (-180, 180),
        precision = 0.05,
        speed = 0.5,
    ),
    att = device('nicos.devices.generic.VirtualMotor',
        description = 'analyzer scattering angle',
        unit = 'deg',
        abslimits = (0, 90),
        precision = 0.05,
        speed = 0.5,
    ),
    ki = device('nicos.devices.tas.Wavevector',
        description = 'incoming wavevector',
        unit = 'A-1',
        base = 'mono',
        tas = 'tas',
        scanmode = 'CKI'
    ),
    kf = device('nicos.devices.tas.Wavevector',
        description = 'outgoing wavevector',
        unit = 'A-1',
        base = 'ana',
        tas = 'tas',
        scanmode = 'CKF',
    ),
    Ei = device('nicos.devices.tas.Energy',
        description = 'incoming energy',
        unit = 'meV',
        base = 'mono',
        tas = 'tas',
        scanmode = 'CKI',
    ),
    Ef = device('nicos.devices.tas.Energy',
        description = 'outgoing energy',
        unit = 'meV',
        base = 'ana',
        tas = 'tas',
        scanmode = 'CKF',
    ),
    Qmod = device('nicos.devices.tas.QModulus',
        description = 'absolute Q',
        unit = 'A-1',
        tas = 'tas',
    ),
    ssl = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-20, 40),
        lowlevel = True,
        unit = 'mm',
    ),
    ssr = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-40, 20),
        lowlevel = True,
        unit = 'mm',
    ),
    ssb = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-50, 30),
        lowlevel = True,
        unit = 'mm',
    ),
    sst = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-30, 50),
        lowlevel = True,
        unit = 'mm',
    ),
    ss = device('nicos.devices.generic.Slit',
        description = 'sample slit',
        left = 'ssl',
        right = 'ssr',
        bottom = 'ssb',
        top = 'sst',
        opmode = 'offcentered',
    ),
    vdet = device('nicos.devices.tas.virtual.VirtualTasDetector',
        description = 'simulated TAS intensity',
        tas = 'tas',
        background = 1,
        realtime = True,
    ),
    ec = device('nicos.devices.tas.EulerianCradle',
        description = 'Eulerian cradle',
        cell = 'Sample',
        tas = 'tas',
        chi = 'echi',
        omega = 'ephi'
    ),
    echi = device('nicos.devices.generic.VirtualMotor',
        description = 'big Euler circle',
        abslimits = (-180, 180),
        unit = 'deg',
    ),
    ephi = device('nicos.devices.generic.VirtualMotor',
        description = 'small Euler circle',
        abslimits = (-180, 180),
        unit = 'deg',
    ),
    sgx = device('nicos.devices.generic.VirtualMotor',
        description = 'X axis sample gonio',
        abslimits = (-10, 10),
        unit = 'deg',
    ),
    sgy = device('nicos.devices.generic.VirtualMotor',
        description = 'Y axis sample gonio',
        abslimits = (-10, 10),
        unit = 'deg',
    ),
    vg1 = device('nicos.devices.tas.VirtualGonio',
        description = 'Gonio along orient1 reflex',
        cell = 'Sample',
        gx = 'sgx',
        gy = 'sgy',
        axis = 1,
        unit = 'deg',
    ),
    vg2 = device('nicos.devices.tas.VirtualGonio',
        description = 'Gonio along orient2 reflex',
        cell = 'Sample',
        gx = 'sgx',
        gy = 'sgy',
        axis = 2,
        unit = 'deg',
    ),
    TBeFilter = device('nicos.devices.generic.VirtualTemperature',
        description = 'Beryllium filter temperature',
        abslimits = (0, 100),
        warnlimits = (0, 70),
        unit = 'K'
    ),
    Shutter = device('nicos.devices.generic.ManualSwitch',
        description = 'Instrument shutter',
        states = ['open', 'closed']
    ),
    Lms = device('nicos.devices.generic.ManualMove',
        description = 'Distance monochromator to sample',
        abslimits = (600, 1500),
        default = 1000,
        unit = 'mm',
    ),
    Lsa = device('nicos.devices.generic.ManualMove',
        description = 'Distance sample to analyzer',
        abslimits = (500, 1000),
        default = 580,
        unit = 'mm',
    ),
    Lad = device('nicos.devices.generic.ManualMove',
        description = 'Distance analyzer to detector',
        abslimits = (400, 600),
        default = 400,
        unit = 'mm',
    ),
)

alias_config = {
    'sth': {'psi': 0},
}

startupcode = '''
if mth() == 0:
    mth.speed = mtt.speed = ath.speed = att.speed = psi.speed = phi.speed = 0
    reset(tas)
    mono(1.55)
    kf(1.55)
    Sample.lattice = [3.5, 3.5, 3.5]
    tas(1,0,0,0)
    mth.speed = mtt.speed = 0.5
    psi.speed = 2
    phi.speed = 1
    ath.speed = att.speed = 0.5
SetDetectors(vdet)

printinfo("===================================================================")
printinfo("Welcome to the NICOS BATAN Triple-Axis Spectrometer SN1 demo setup.")
printinfo("This demo is configured as a virtual triple-axis instrument.")
printinfo("Try doing an elastic scan over a Bragg peak, e.g.")
printinfo("  > qcscan((1, 0, 0, 0), (0.002, 0, 0, 0), 10, t=1, kf=1.4)")
printinfo("or an energy scan, e.g.")
printinfo("  > qscan((1, 0.2, 0, 4), (0, 0, 0, 0.2), 21, t=1, kf=1.55)")
printinfo("===================================================================")
'''
