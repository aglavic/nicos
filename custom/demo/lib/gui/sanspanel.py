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
#   Georg Brandl <georg.brandl@frm2.tum.de>
#
# *****************************************************************************

"""NICOS livewidget 2D data plot window/panel."""

from __future__ import with_statement

__version__ = "$Revision$"

import os
import time
from os import path

from PyQt4.QtCore import Qt, QVariant, SIGNAL, SLOT
from PyQt4.QtCore import pyqtSignature as qtsig, QSize
from PyQt4.QtGui import QPrinter, QPrintDialog, QDialog, QMainWindow, \
     QMenu, QToolBar, QStatusBar, QSizePolicy, QListWidgetItem, QLabel, QFont, \
     QBrush, QPen, QComboBox, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, \
     QStyle, QDialogButtonBox
from PyQt4.Qwt5 import QwtPlot, QwtPlotPicker, QwtPlotZoomer, QwtPlotCurve, \
     QwtPlotMarker, QwtSymbol

from nicos.clients.gui.utils import loadUi, dialogFromUi
from nicos.clients.gui.panels import Panel
from nicos.clients.gui.livewidget import LWWidget, LWData, Logscale, \
     MinimumMaximum, BrightnessContrast, Integrate, Histogram, CreateProfile

DATATYPES = frozenset(('<I4', '<i4', '>I4', '>i4', '<I2', '<i2', '>I2', '>i2',
                       'I1', 'i1', 'f8', 'f4'))


my_uipath = path.dirname(__file__)


class SANSPanel(Panel):
    panelName = 'SANS acquisition'

    def __init__(self, parent, client):
        Panel.__init__(self, parent, client)
        loadUi(self, 'sanspanel.ui', my_uipath)

        self._format = '<I4'
        self._runtime = 0
        self._no_direct_display = False
        self._range_active = False
        self._filename = ''
        self._nx = self._ny = 128
        self._nz = 1
        self.current_status = None

        self.statusBar = QStatusBar(self)
        policy = self.statusBar.sizePolicy()
        policy.setVerticalPolicy(QSizePolicy.Fixed)
        self.statusBar.setSizePolicy(policy)
        self.statusBar.setSizeGripEnabled(False)
        self.layout().addWidget(self.statusBar)

        self.widgetLayout.addWidget(QLabel('test'))

        self.widget = LWWidget(self)
        self.widget.setAxisLabels('pixels x', 'pixels y')
        self.widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.widget.setKeepAspect(False)
        self.widget.setControls(Logscale | MinimumMaximum | BrightnessContrast |
                                Integrate | Histogram | CreateProfile)
        self.widgetLayout.addWidget(self.widget)

        self.liveitem = QListWidgetItem('<Live>', self.fileList)
        self.liveitem.setData(32, '')
        self.liveitem.setData(33, '')

        self.splitter.restoreState(self.splitterstate)

        self.connect(client, SIGNAL('livedata'), self.on_client_livedata)
        self.connect(client, SIGNAL('liveparams'), self.on_client_liveparams)
        if client.connected:
            self.on_client_connected()
        self.connect(client, SIGNAL('connected'), self.on_client_connected)

        self.connect(self.actionLogScale, SIGNAL("toggled(bool)"),
                     self.widget, SLOT("setLog10(bool)"))
        self.connect(self.widget,
                     SIGNAL('customContextMenuRequested(const QPoint&)'),
                     self.on_widget_customContextMenuRequested)
        self.connect(self.widget,
                     SIGNAL('profileUpdate(int, int, void*, void*)'),
                     self.on_widget_profileUpdate)

    def setSettings(self, settings):
        self._instrument = settings.get('instrument', '')
        self.widget.setInstrumentOption(self._instrument)

    def loadSettings(self, settings):
        self.splitterstate = settings.value('splitter').toByteArray()

    def saveSettings(self, settings):
        settings.setValue('splitter', self.splitter.saveState())
        settings.setValue('geometry', QVariant(self.saveGeometry()))

    def getMenus(self):
        self.menu = menu = QMenu('&Live data', self)
        menu.addAction(self.actionPrint)
        menu.addSeparator()
        menu.addAction(self.actionSetAsROI)
        menu.addAction(self.actionUnzoom)
        menu.addAction(self.actionLogScale)
        menu.addAction(self.actionNormalized)
        menu.addAction(self.actionLegend)
        return [menu]

    def getToolbars(self):
        bar = QToolBar('Live data')
        bar.addAction(self.actionPrint)
        bar.addSeparator()
        bar.addAction(self.actionLogScale)
        bar.addSeparator()
        bar.addAction(self.actionUnzoom)
        #bar.addAction(self.actionSetAsROI)
        return [bar]

    def updateStatus(self, status, exception=False):
        self.current_status = status

    def on_widget_customContextMenuRequested(self, point):
        self.menu.popup(self.mapToGlobal(point))

    def on_widget_profileUpdate(self, type, nbins, x, y):
        pass

    def on_fileList_itemClicked(self, item):
        if item is None:
            return
        fname = item.data(32).toString()
        if fname == '':
            if self._no_direct_display:
                self._no_direct_display = False
                self.widget.setData(LWData(self._nx, self._ny, self._nz,
                                           self._format, self._last_data))
        else:
            self._no_direct_display = True
            fcontent = open(fname, 'rb').read()
            self.widget.setData(LWData(self._nx, self._ny, self._nz,
                                       self._format, fcontent))

    def on_fileList_currentItemChanged(self, item, previous):
        self.on_fileList_itemClicked(item)

    def on_client_connected(self):
        pass
        datapath = self.client.eval('session.experiment.datapath', [])
        caspath = path.join(datapath[0], '2ddata')
        if path.isdir(caspath):
            for fn in sorted(os.listdir(caspath)):
                if fn.endswith('.dat'):
                    self.add_to_flist(path.join(caspath, fn), '', False)

    def on_client_liveparams(self, params):
        _tag, fname, dtype, nx, ny, nz, runtime = params
        self._runtime = runtime
        self._filename = fname
        if dtype not in DATATYPES:
            self._format = None
            print 'Unsupported live data format:', params
            return
        self._format = dtype
        self._nx = nx
        self._ny = ny
        self._nz = nz

    def on_client_livedata(self, data):
        self._last_data = data
        if not self._no_direct_display:
            self.widget.setData(
                LWData(self._nx, self._ny, self._nz, self._format, data))
        if self._filename:# and path.isfile(self._filename):
            self.add_to_flist(self._filename, self._format)

    def add_to_flist(self, filename, fformat, scroll=True):
        shortname = path.basename(filename)
        item = QListWidgetItem(shortname)
        item.setData(32, filename)
        item.setData(33, fformat)
        self.fileList.insertItem(self.fileList.count()-1, item)
        if scroll:
            self.fileList.scrollToBottom()

    @qtsig('')
    def on_start_clicked(self):
        detpos = self.detpos.value()
        ctime = self.ctime.value()
        coll = self.coll10.isChecked() and '10m' or \
            (self.coll15.isChecked() and '15m' or '20m')
        code = 'move(coll, %r)\nmove(det_pos, %r)\nwait(coll, det_pos)\ncount(%s)\n' % \
            (coll, detpos, ctime)
        self.execScript(code)

    @qtsig('')
    def on_actionUnzoom_triggered(self):
        self.widget.plot().getZoomer().zoom(0)

    @qtsig('')
    def on_actionPrint_triggered(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setColorMode(QPrinter.Color)
        printer.setOrientation(QPrinter.Landscape)
        printer.setOutputFileName('')
        if QPrintDialog(printer, self).exec_() == QDialog.Accepted:
            self.widget.plot().print_(printer)

    def execScript(self, script):
        action = 'queue'
        if self.current_status != 'idle':
            qwindow = dialogFromUi(self, 'question.ui', 'panels')
            qwindow.questionText.setText('A script is currently running.  What '
                                         'do you want to do?')
            icon = qwindow.style().standardIcon
            qwindow.iconLabel.setPixmap(
                icon(QStyle.SP_MessageBoxQuestion).pixmap(32, 32))
            b0 = QPushButton(icon(QStyle.SP_DialogCancelButton), 'Cancel')
            b1 = QPushButton(icon(QStyle.SP_DialogOkButton), 'Queue script')
            b2 = QPushButton(icon(QStyle.SP_MessageBoxWarning), 'Execute now!')
            qwindow.buttonBox.addButton(b0, QDialogButtonBox.ApplyRole)
            qwindow.buttonBox.addButton(b1, QDialogButtonBox.ApplyRole)
            qwindow.buttonBox.addButton(b2, QDialogButtonBox.ApplyRole)
            qwindow.buttonBox.setFocus()
            result = [0]
            def pushed(btn):
                if btn is b1:
                    result[0] = 1
                elif btn is b2:
                    result[0] = 2
                qwindow.accept()
            self.connect(qwindow.buttonBox, SIGNAL('clicked(QAbstractButton*)'),
                         pushed)
            qwindow.exec_()
            if result[0] == 0:
                return
            elif result[0] == 2:
                action = 'execute'
        if action == 'queue':
            self.client.tell('queue', '', script)
            self.mainwindow.action_start_time = time.time()
        else:
            self.client.tell('exec', script)
