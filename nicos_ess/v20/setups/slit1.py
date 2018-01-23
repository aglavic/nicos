description = 'Slit 1'
servername = 'EXV20'
nameservice = '192.168.1.254'

loadblock = '''start=never,async
stop=never,async
read=always,async
motion_TBG=0.1
motion_TBK=0.01
motion_usefloat=true
motion_autodelete=false
motion_display=36
motion_displayformat=%0.3f
motion_retries=1
loadoffset=yes
'''

devices = dict(
    slit1hl = device('nicos.devices.vendor.caress.Motor',
        description = 'Slit 1 Horizontal Left',
        fmtstr = '%.2f',
        unit = 'mm',
        coderoffset = 0,
        abslimits = (-30, 30),
        nameserver = '%s' % (nameservice,),
        objname = '%s' % (servername),
        config = 'MB1HL 500 nist222dh1787.hmi.de:/st222.caress_object '
                 'CopleyStepnet 2 -4000 BeckhoffKL5001 BK5120/63/32/8/0 '
                 '-4096 232159',
        lowlevel = True,
        loadblock = loadblock
    ),
    slit1hr = device('nicos.devices.vendor.caress.Motor',
        description = 'Slit 1 Horizontal Right',
        fmtstr = '%.2f',
        unit = 'mm',
        coderoffset = 0,
        abslimits = (-30, 30),
        nameserver = '%s' % (nameservice,),
        objname = '%s' % (servername),
        config = 'MB1HR 500 nist222dh1787.hmi.de:/st222.caress_object '
                 'CopleyStepnet 3 -4000 BeckhoffKL5001 BK5120/63/32/12/0 '
                 '-4096 227117',
        lowlevel = True,
        loadblock = loadblock
    ),
    slit1vb = device('nicos.devices.vendor.caress.Motor',
        description = 'Slit 1 Vertical Bottom',
        fmtstr = '%.2f',
        unit = 'mm',
        coderoffset = 0,
        abslimits = (-60, 60),
        nameserver = '%s' % (nameservice,),
        objname = '%s' % (servername),
        config = 'MB1VB 500 nist222dh1787.hmi.de:/st222.caress_object '
                 'CopleyStepnet 4 4000 BeckhoffKL5001 BK5120/63/32/16/0 '
                 '4096 368403',
        lowlevel = True,
        loadblock = loadblock
    ),
    slit1vt = device('nicos.devices.vendor.caress.Motor',
        description = 'Slit 1 Vertical Top',
        fmtstr = '%.2f',
        unit = 'mm',
        coderoffset = 0,
        abslimits = (-60, 60),
        nameserver = '%s' % (nameservice,),
        objname = '%s' % (servername),
        config = 'MB1VT 500 nist222dh1787.hmi.de:/st222.caress_object '
                 'CopleyStepnet 5 4000 BeckhoffKL5001 BK5120/63/32/20/0 '
                 '4096 371652',
        lowlevel = True,
        loadblock = loadblock
    ),
    slit1 = device('nicos.devices.generic.Slit',
        description = 'Slit 1',
        left = 'slit1hl',
        right = 'slit1hr',
        top = 'slit1vt',
        bottom = 'slit1vb',
        opmode = 'offcentered',
        coordinates = 'equal',
    ),
)
