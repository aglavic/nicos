#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the FRM-II
# Copyright (c) 2009-2012 by the NICOS contributors (see AUTHORS)
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
#   Klaudia Hradil <klaudia.hradil@frm2.tum.de>
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
# *****************************************************************************

"""NICOS triple-axis instrument devices."""

__version__ = "$Revision$"

from nicos.core import Moveable, Param, Override, AutoDevice, Value, \
     ConfigurationError, ComputationError, tupleof, multiStatus
from nicos.tas.cell import Cell
from nicos.tas.mono import Monochromator
from nicos.instrument import Instrument


SCANMODES = ['CKI', 'CKF', 'CPHI', 'CPSI', 'DIFF']

ENERGYTRANSFERUNITS = ['meV', 'THz']
THZ2MEV = 4.136


class TAS(Instrument, Moveable):
    """An instrument class that can move in (q,w) space.

    When setting up a triple-axis configuration, use this as your instrument
    device (or derive an individual subclass).
    """

    attached_devices = {
        'cell': (Cell, 'Unit cell object to calculate angles'),
        'mono': (Monochromator, 'Monochromator device'),
        'ana':  (Monochromator, 'Analysator device'),
        'phi':  (Moveable, 'Sample scattering angle'),
        'psi':  (Moveable, 'Sample rocking angle'),
    }

    parameters = {
        'scanmode':     Param('Operation mode: one of ' + ', '.join(SCANMODES),
                              type=str, default='CKI', settable=True,
                              category='instrument'),
        'scanconstant': Param('Constant of the operation mode', type=float,
                              default=0, settable=True, category='instrument'),
        'axiscoupling': Param('Whether the sample th/tt axes are coupled',
                              type=bool, default=True, settable=True),
        'psi360':       Param('Whether the range of psi is 0-360 deg '
                              '(otherwise -180-180 deg is assumed).',
                              type=bool, default=True, settable=True),
        'scatteringsense': Param('Scattering sense', default=(1, -1, 1),
                                 type=tupleof(int, int, int), settable=True,
                                 category='instrument'),
        'energytransferunit': Param('Energy transfer unit', type=str,
                                    default='THz', settable=True),
        'collimation':  Param('Collimation settings', type=str,
                              settable=True, category='instrument'),
    }

    parameter_overrides = {
        'fmtstr': Override(default='[%6.4f, %6.4f, %6.4f, %6.4f]'),
        'unit':   Override(default='rlu rlu rlu THz', mandatory=False,
                           settable=True)
    }

    hardware_access = False

    def doInit(self):
        self.__dict__['h'] = TASIndex('h', unit='rlu', fmtstr='%.3f',
                                      index=0, lowlevel=True, tas=self)
        self.__dict__['k'] = TASIndex('k', unit='rlu', fmtstr='%.3f',
                                      index=1, lowlevel=True, tas=self)
        self.__dict__['l'] = TASIndex('l', unit='rlu', fmtstr='%.3f',
                                      index=2, lowlevel=True, tas=self)
        self.__dict__['E'] = TASIndex('E', unit=self.energytransferunit,
                                      fmtstr='%.3f', index=3, lowlevel=True,
                                      tas=self)
        self._last_calpos = None

    def _thz(self, ny):
        if self.energytransferunit == 'meV':
            return ny / THZ2MEV
        return ny

    def doIsAllowed(self, pos):
        qh, qk, ql, ny = pos
        ny = self._thz(ny)
        try:
            angles = self._adevs['cell'].cal_angles(
                [qh, qk, ql], ny, self.scanmode, self.scanconstant,
                self.scatteringsense[1], self.axiscoupling, self.psi360)
        except ComputationError, err:
            return False, str(err)
        # check limits for the individual axes
        for devname, value in zip(['mono', 'ana', 'phi', 'psi'], angles[:4]):
            dev = self._adevs[devname]
            if isinstance(dev, Monochromator):
                ok, why = dev._allowedInvAng(value)
            else:
                ok, why = dev.isAllowed(value)
            if not ok:
                return ok, 'target position %s %s outside limits for %s: %s' % \
                       (dev.format(value), dev.unit, dev, why)
        return True, ''

    def doStart(self, pos):
        qh, qk, ql, ny = pos
        ny = self._thz(ny)
        angles = self._adevs['cell'].cal_angles(
            [qh, qk, ql], ny, self.scanmode, self.scanconstant,
            self.scatteringsense[1], self.axiscoupling, self.psi360)
        mono, ana, phi, psi = self._adevs['mono'], self._adevs['ana'], \
                              self._adevs['phi'], self._adevs['psi']
        self.log.debug('moving phi/stt to %s' % angles[2])
        phi.start(angles[2])
        self.log.debug('moving psi/sth to %s' % angles[3])
        psi.start(angles[3])
        self.log.debug('moving mono to %s' % angles[0])
        mono._startInvAng(angles[0])
        if self.scanmode != 'DIFF':
            self.log.debug('moving ana to %s' % angles[1])
            ana._startInvAng(angles[1])
        mono.wait()
        if self.scanmode != 'DIFF':
            ana.wait()
        phi.wait()
        psi.wait()
        #h, k, l, ny = self.read(0)
        # make sure index members read the latest value
        for index in (self.h, self.k, self.l, self.E):
            if index._cache:
                index._cache.invalidate(index, 'value')
        #self.log.info('position hkl: (%7.4f %7.4f %7.4f) E: %7.4f %s' %
        #               (h, k, l, ny, self.energytransferunit))

    def doStatus(self):
        return multiStatus((name, self._adevs[name]) for name in
                           ['mono', 'ana', 'phi', 'psi'])

    def doWriteScatteringsense(self, val):
        for v in val:
            if v not in [-1, 1]:
                raise ConfigurationError('invalid scattering sense %s' % v)

    def doUpdateScatteringsense(self, val):
        self._adevs['mono']._scatsense = val[0]
        self._adevs['ana']._scatsense = val[2]

    def doUpdateScanmode(self, val):
        if val not in SCANMODES:
            raise ConfigurationError('invalid scanmode: %r' % val)

    def doWriteEnergytransferunit(self, val):
        if val not in ENERGYTRANSFERUNITS:
            raise ConfigurationError('invalid energy transfer unit: %r' % val)
        if self._cache:
            self._cache.invalidate(self, 'value')
        self.unit = 'rlu rlu rlu %s' % val
        self.E.unit = val

    def valueInfo(self):
        return Value('h', unit='rlu', fmtstr='%.4f'), \
            Value('k', unit='rlu', fmtstr='%.4f'), \
            Value('l', unit='rlu', fmtstr='%.4f'), \
            Value('E', unit=self.energytransferunit, fmtstr='%.4f')

    def doRead(self):
        # XXX read() or read(0)
        mono, ana, phi, psi = self._adevs['mono'], self._adevs['ana'], \
                              self._adevs['phi'], self._adevs['psi']
        # read out position
        if self.scanmode == 'DIFF':
            hkl = self._adevs['cell'].angle2hkl(
                [mono._readInvAng(), mono._readInvAng(), phi.read(), psi.read()],
                self.axiscoupling)
            ny = 0
        else:
            hkl = self._adevs['cell'].angle2hkl(
                [mono._readInvAng(), ana._readInvAng(), phi.read(), psi.read()],
                self.axiscoupling)
            ny = self._adevs['cell'].cal_ny(mono._readInvAng(), ana._readInvAng())
            if self.energytransferunit == 'meV':
                ny *= THZ2MEV
        return [hkl[0], hkl[1], hkl[2], ny]

    def _calpos(self, pos, printout=True):
        qh, qk, ql, ny, sc = pos
        ny = self._thz(ny)
        try:
            angles = self._adevs['cell'].cal_angles(
                [qh, qk, ql], ny, self.scanmode, sc,
                self.scatteringsense[1], self.axiscoupling, self.psi360)
        except ComputationError, err:
            self.log.warning('cannot calculate position: %s' % err)
            return
        if not printout:
            return angles
        for devname, value in zip(['mono', 'ana', 'phi', 'psi'], angles[:4]):
            dev = self._adevs[devname]
            if isinstance(dev, Monochromator):
                ok, why = dev._allowedInvAng(value)
            else:
                ok, why = dev.isAllowed(value)
            if not ok:
                why = 'target position %s %s outside limits for %s: %s' % \
                    (dev.format(value), dev.unit, dev, why)
                break
        self._last_calpos = pos
        self.log.info('ki:            %8.3f A-1' % angles[0])
        self.log.info('kf:            %8.3f A-1' % angles[1])
        self.log.info('2theta sample: %8.3f deg' % angles[2])
        self.log.info('theta sample:  %8.3f deg' % angles[3])
        if ok:
            self.log.info('position allowed')
        else:
            self.log.warning('position not allowed: ' + why)

    def _calhkl(self, angles):
        return self._adevs['cell'].angle2hkl(angles, self.axiscoupling)


class TASIndex(Moveable, AutoDevice):
    """
    "Partial" devices for the H, K, L, E indices of the TAS instrument.
    """

    parameters = {
        'index': Param('The index into the TAS value', type=int),
    }

    attached_devices = {
        'tas': (TAS, 'The spectrometer to control'),
    }

    hardware_access = False

    def doRead(self):
        # XXX read() or read(0)
        return self._adevs['tas'].read()[self.index]

    def doStart(self, pos):
        # XXX read() or read(0)
        current = list(self._adevs['tas'].read())
        current[self.index] = pos
        self._adevs['tas'].start(current)

    def doWait(self):
        self._adevs['tas'].wait()


class Wavevector(Moveable):
    """
    Device for adjusting initial/final wavevectors of the TAS and also setting
    the scanmode.
    """

    parameters = {
        'scanmode': Param('Scanmode to set', type=str, mandatory=True),
    }

    parameter_overrides = {
        'maxage':   Override(default=0),
    }

    attached_devices = {
        'base': (Moveable, 'Device to move (mono or ana)'),
        'tas':  (TAS, 'The spectrometer for setting scanmode'),
    }

    hardware_access = False

    def doInit(self):
        self._value = None

    def doRead(self):
        if self._value is None:
            # XXX read() or read(0)
            self._value = self._adevs['base']._readInvAng()
        return self._value

    def doStart(self, pos):
        # first drive there, to determine if it is within limits
        self._adevs['base']._startInvAng(pos)
        self._adevs['tas'].scanmode = self.scanmode
        self._adevs['tas'].scanconstant = pos
        self._value = pos

    def info(self):
        # Do not add "ki" or "kf" pseudo-devices to scan files
        return []
