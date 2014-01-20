#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2014 by the NICOS contributors (see AUTHORS)
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
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
# *****************************************************************************

"""Core data handling classes."""

from nicos import session
from nicos.core import Device, Param, listof, INFO_CATEGORIES
from nicos.utils import lazy_property
from nicos.core import SIMULATION


class Dataset(object):
    # unique id
    uid = ''
    # scan type
    scantype = None
    # start time
    started = 0
    # data sinks active for this data set
    sinks = []
    # devices to move
    devices = []
    # list of scan positions (can be empty if not known)
    positions = []
    # multi-steps for each scan point
    multistep = []
    # list of detectors for this dataset
    detlist = []
    # list of environment devices for this dataset
    envlist = []
    # preset dictionary of scan
    preset = {}
    # scan info
    scaninfo = ''
    # additional info from data sinks
    sinkinfo = {}
    # resulting x values (should coincide with positions)
    xresults = []
    # resulting y values at the positions
    yresults = []
    # index of the x value to use for plotting
    xindex = 0
    # current point number
    curpoint = 0
    # number of xvalues belonging to environment devices
    envvalues = 0

    # stuff for image support
    imageinfos = []
    # storage for header info
    headerinfo = {}

    # cached info for all sinks to use
    xvalueinfo = []
    xrange = None
    yvalueinfo = []
    yrange = None

    # info derived from valueinfo
    @lazy_property
    def xnames(self):
        return [v.name for v in self.xvalueinfo]
    @lazy_property
    def xunits(self):
        return [v.unit for v in self.xvalueinfo]
    @lazy_property
    def ynames(self):
        if self.multistep:
            ret = []
            mscount = len(self.multistep[0][1])
            nyvalues = len(self.yvalueinfo) // mscount
            for i in range(mscount):
                addname = '_' + '_'.join('%s_%s' % (mse[0], mse[1][i])
                                         for mse in self.multistep)
                ret.extend(val.name + addname
                           for val in self.yvalueinfo[:nyvalues])
            return ret
        return [v.name for v in self.yvalueinfo]
    @lazy_property
    def yunits(self):
        return [v.unit for v in self.yvalueinfo]

    def __init__(self):
        # correctly init mutable types to avoid collecting dust
        self.headerinfo = {}
        self.imageinfos = []
        self.sinks = []
        self.devices = []
        self.positions = []
        self.multistep = []
        self.detlist = []
        self.envlist = []
        self.preset = {}
        self.sinkinfo = {}
        self.xresults = []
        self.yresults = []

    def updateHeaderInfo(self, updatedict=None):
        bycategory = {}
        headerinfo = self.headerinfo = {}
        # XXX: if updatedict is given, only update those devices positions
        # instead of reading all
        for _, device in sorted(session.devices.iteritems()):
            if device.lowlevel:
                continue
            for category, key, value in device.info():
                bycategory.setdefault(category, []).append((device, key, value))
        for catname, catinfo in INFO_CATEGORIES:
            if catname not in bycategory:
                continue
            headerinfo[catinfo] = bycategory[catname]


class DataSink(Device):
    """Base class for all data sinks.

    A DataSink is a configurable object that receives scan data.  All data
    handling is done by sinks; e.g. displaying it on the console or saving to a
    data file.
    """

    parameters = {
        'scantypes': Param('Scan types for which the sink is active',
                           type=listof(str), default=[]),
    }

    # Set to false in subclasses that e.g. write to the filesystem.
    activeInSimulation = True

    def isActive(self, scantype):
        if session.mode == SIMULATION and not self.activeInSimulation:
            return False
        if scantype is not None and scantype not in self.scantypes:
            return False
        return True

    def prepareDataset(self, dataset):
        """Prepare for a new dataset.

        Returns a list of info about the new dataset as ``(key, value)`` pairs.
        A list of all these pairs is then passed to all sinks' `beginDataset()`
        as the *sinkinfo* parameter.  This is meant for sinks that write files
        to communicate the file name to sinks that write the info to the console
        or display them otherwise.
        """

    def beginDataset(self, dataset):
        """Begin a new dataset.

        The dataset will contain x-values for all its *devices* (a list of
        `Device` objects), measured at *positions* (a list of lists, or None if
        the positions are not yet known).

        The dataset will contain y-values measured by the *detlist* using the
        given *preset* (a dictionary).

        *userinfo* is an arbitrary string.  *sinkinfo* is a list of ``(key,
        value)`` pairs as explained in `prepareDataset()`.
        """

    def addInfo(self, dataset, category, valuelist):
        """Add additional information to the dataset.

        This is meant to record e.g. device values at scan startup.  *valuelist*
        is a sequence of tuples ``(device, key, value)``.
        """

    def addPoint(self, dataset, xvalues, yvalues):
        """Add a point to the dataset.

        *xvalues* is a list of values with the same length as the initial
        *devices* list given to `beginDataset()`, and *yvalues* is a list of
        values with the same length as the all of detlist's value lists.
        """

    def addBreak(self, dataset):
        """Add a "break" to the dataset.

        A break indicates a division in the data, e.g. between successive rows
        of a 2-dimensional scan.
        """

    def endDataset(self, dataset):
        """End the current dataset."""

    def addFitCurve(self, dataset, title, xvalues, yvalues):
        """Add a fit curve to the dataset after it is finished."""
