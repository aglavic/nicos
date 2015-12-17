#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2015 by the NICOS contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Stefanie Keuler <s.keuler@fz-juelich.de>
#   Lydia Fleischhauer-Fuss <l.fleischhauer-fuss@fz-juelich.de>
#
# *****************************************************************************

"""DNS file format saver

.d_dat: document the file format here.
"""

from time import strftime, localtime

import numpy as np

from nicos import session
from nicos.core import Override, ImageSink
from nicos.core.utils import DeviceValueDict


class DNSFileFormat(ImageSink):
    """Saves DNS image data"""
    parameter_overrides = {
        'filenametemplate': Override(mandatory=False, settable=False,
                                     userparam=False,
                                     default=['%(proposal)s_%(counter)s.d_dat',
                                              '%(proposal)s'
                                              '%(imagecounter)010d'
                                              '%(session.experiment.sample.'
                                              'samplename)s.d_dat'],
                                     ),
    }

    fileFormat = 'DNS'     # should be unique amongst filesavers!

    def acceptImageType(self, imagetype):
        return True

    def prepareImage(self, imageinfo, subdir=''):
        ImageSink.prepareImage(self, imageinfo, subdir)
        imageinfo.data = DeviceValueDict(
            fileName=imageinfo.filename,
            fileDate=strftime('%m/%d/%Y'),
            fileTime=strftime('%r'),
            FromDate=strftime('%m/%d/%Y'),
            FromTime=strftime('%r'),
            Environment='_'.join(session.explicit_setups),
        )

    def updateImage(self, imageinfo, image):
        """just write the data upon update"""
        imageinfo.file.seek(0)
        numarr = np.array(image)
        imageinfo.file.write("# 64 %4d\n" % 1)
        for ch in range(64):
            imageinfo.file.write("%2d %8d\n" % (ch, numarr[ch]))
        imageinfo.file.flush()

    def finalizeImage(self, imageinfo):
        """finalizes the on-disk image, normally just a close"""
        ImageSink.finalizeImage(self, imageinfo)

    def saveImage(self, imageinfo, image):
        """Save in DNS format"""
        w = imageinfo.file.write
        separator = "#" + "-"*74 + "\n"

        def readdev(name):
            return session.getDevice(name).read()

        imageinfo.file.seek(0)
        exp = session.experiment
        w("# DNS Data userid=%s,exp=%s,file=%s,sample=%s\n" %
          (exp.users, exp.lastscan, exp.lastimage, exp.sample.samplename))
        w(separator)

        # TODO: use right value, remove dummylines
        # w("# %d\n" % len(datacomment))
        # for i in range(len(datacomment)):
        #     w("# " + datacomment[i] + "\n")

        w("# 2\n")  # TODO: add other comment maybe
        w("# User: %s\n" % exp.users)
        w("# Sample: %s\n" % exp.sample.samplename)
        w(separator)

        w("# DNS   Mono  d-spacing[nm]  Theta[deg]   "
          "Lambda[nm]   Energy[meV]   Speed[m/sec]\n")
        lam = readdev('mon_lambda')
        energy = 81.804165 / lam**2
        speed = 3956.0 / lam
        w("#      %s   %6.4f         %6.2f         %6.3f"
          "%6.3f      %7.2f\n" %
          ("PG-002", 0.3350, readdev('mon_rot'), lam, energy, speed))

        w("# Distances [cm] Sample_Chopper    "
          "Sample_Detector    Sample_Monochromator\n")
        # TODO: not hard coded?
        w("#                  36.00            80.00            220.00\n")
        w(separator)

        w("# Motors                      Position\n")
        w("# Monochromator              %6.2f deg\n" % readdev('mon_rot'))
        w("# DeteRota                   %6.2f deg\n" % readdev('det_rot'))
        w("#\n")
        w("# Huber                      %6.2f deg\n" % readdev('sample_rot'))
        w("# Cradle_lower               %6.2f deg\n" % readdev('cradle_lo'))
        w("# Cradle_upper               %6.2f deg\n" % readdev('cradle_up'))
        w("#\n")
        w("# Slit_i_vertical upper      %6.1f mm\n" %
          readdev('ap_sam_y_upper'))
        w("#                 lower      %6.1f mm\n" %
          readdev('ap_sam_y_lower'))
        w("# Slit_i_horizontal left     %6.1f mm\n" %
          readdev('ap_sam_x_left'))
        w("#                   right    %6.1f mm\n" %
          readdev('ap_sam_x_right'))
        w("#\n")
        # dummy line
        w("# Slit_f_upper                %4d mm\n" % 0)
        # dummy line
        w("# Slit_f_lower                %4d mm\n" % 0)
        # dummy line
        w("# Detector_Position_vertical  %4d mm\n" % 0)
        w("#\n")
        w("# Polariser\n")
        w("#    Translation              %4d mm\n" % readdev('pol_trans'))
        w("#    Rotation              %6.2f deg\n" % readdev('pol_rot'))
        w("#\n")
        w("# Analysers                 undefined\n")
        w(separator)
        # write currents
        w("# B-fields                   current[A]  field[G]\n")
        w("#   Flipper_precession        %6.3f A     %6.2f G\n" %
          (readdev('Co'), 0.0))
        w("#   Flipper_z_compensation    %6.3f A     %6.2f G\n" %
          (readdev('Fi'), 0.0))
        w("#   C_a                       %6.3f A     %6.2f G\n" %
          (readdev('A'), 0.0))
        w("#   C_b                       %6.3f A     %6.2f G\n" %
          (readdev('B'), 0.0))
        w("#   C_c                       %6.3f A     %6.2f G\n" %
          (readdev('C'), 0.0))
        w("#   C_z                       %6.3f A     %6.2f G\n" %
          (readdev('ZT'), 0.0))
        w(separator)

        tsample, ttube, tset = float('NaN'), float('NaN'), float('NaN')
        if 'Ts' in session.devices:
            tsample = readdev('Ts')
        if 'T_jlc3_tube' in session.devices:
            ttube = readdev('T_jlc3_tube')
            tset = float(session.getDevice('T_jlc3_tube').setpoint)

        w("# Temperatures/Lakeshore      T\n")
        w("#  T1                         %6.3f K\n" % ttube)
        w("#  T2                         %6.3f K\n" % tsample)
        w("#  sample_setpoint            %6.3f K\n" % tset)
        w(separator)

        det_dev = session.getDevice('det')
        w("# TOF parameters\n")
        w("#  TOF channels                %4d\n" % det_dev.nrtimechan)
        tdiv = 0.05 * (det_dev.divisor + 1)
        w("#  Time per channel            %6.1f microsecs\n" % tdiv)
        tdel = 0.05 * det_dev.offsetdelay
        w("#  Delay time                  %6.1f microsecs\n" % tdel)

        w("#  Chopper slits\n")  # %4d\n" % config.datachopperslits) # TODO
        w("#  Elastic time channel\n")  # %4d\n" % config.dataelastictime) # TODO
        w("#  Chopper frequency\n")  # %4d Hz\n" % monitor.getfreq()) # TODO
        w(separator)

        w("# Active_Stop_Unit           TIMER\n")
        w("#  Timer                    %6.1f sec\n" % readdev('timer')[0])
        w("#  Monitor           %16d\n" % readdev('mon0')[0])
        w("#\n")
        begin_t = strftime('%Y-%m-%d %H:%M:%S', localtime(imageinfo.begintime))
        end_t = strftime('%Y-%m-%d %H:%M:%S', localtime(imageinfo.endtime))
        w("#    start   at      %s\n" % begin_t)
        w("#    stopped at      %s\n" % end_t)
        w(separator)

        # write array
        w("# DATA (number of detectors, number of TOF channels)\n")
        numarr = np.array(image)
        w("# 64 %4d\n" % det_dev.nrtimechan)
        for ch in range(64):
            w("%2d " % ch)
            for q in range(det_dev.nrtimechan):
                w(" %8d" % (numarr[q, ch]))
            w("\n")
        imageinfo.file.flush()
