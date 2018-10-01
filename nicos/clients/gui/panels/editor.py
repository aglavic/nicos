#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2018 by the NICOS contributors (see AUTHORS)
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

"""NICOS GUI user editor window."""

import io
import sys
import time
from logging import WARNING
from os import path
from uuid import uuid1

from nicos.clients.gui.dialogs.editordialogs import OverwriteQuestion, \
    SearchDialog
from nicos.clients.gui.dialogs.traceback import TracebackDialog
from nicos.clients.gui.panels import Panel
from nicos.clients.gui.tools import createToolMenu
from nicos.clients.gui.utils import loadUi, showToolText
from nicos.clients.gui.widgets.qscintillacompat import QScintillaCompatible
from nicos.guisupport.qt import QAction, QActionGroup, QByteArray, QColor, \
    QDialog, QFileDialog, QFileSystemModel, QFileSystemWatcher, QFont, \
    QFontMetrics, QHBoxLayout, QHeaderView, QInputDialog, QMenu, QMessageBox, \
    QPen, QPrintDialog, QPrinter, QsciLexerPython, QsciPrinter, \
    QsciScintilla, Qt, QTabWidget, QToolBar, QTreeWidgetItem, pyqtSlot
from nicos.guisupport.utils import setBackgroundColor
from nicos.pycompat import iteritems
from nicos.utils import formatDuration, formatEndtime

has_scintilla = QsciScintilla is not None

COMMENT_STR = '## '


if has_scintilla:
    class Printer(QsciPrinter):
        """
        Class extending the default QsciPrinter with a header.
        """
        def formatPage(self, painter, drawing, area, pagenr):
            QsciPrinter.formatPage(self, painter, drawing, area, pagenr)

            fn = self.docName()
            header = 'File: %s    page %s    %s' % \
                     (fn, pagenr, time.strftime('%Y-%m-%d %H:%M'))
            painter.save()
            pen = QPen(QColor(30, 30, 30))
            pen.setWidth(1)
            painter.setPen(pen)
            newTop = area.top() + painter.fontMetrics().height() + 15
            area.setLeft(area.left() + 30)
            if drawing:
                painter.drawText(area.left(),
                                 area.top() + painter.fontMetrics().ascent(),
                                 header)
                painter.drawLine(area.left() - 2, newTop - 12,
                                 area.right() + 2, newTop - 12)
            area.setTop(newTop)
            painter.restore()

    class QsciScintillaCustom(QsciScintilla):
        def moveToEnd(self):
            self.SendScintilla(self.SCI_DOCUMENTEND)


class EditorPanel(Panel):
    """Provides a text editor specialized for entering scripts.

    Together with actions such as `Run` or `Simulate` it gives the user the
    opportunity to create and check measurement scripts.  The editor widget
    uses `QScintilla` if it is installed, and a standard text edit box
    otherwise.

    Options:

    * ``tools`` (default None) -- a list of `tools` which may configure some
      special commands or scripts.  The tools can generate code to insert
      into the editor window.  The access to these tools will be given via a
      special menu ``Editor tools``.
    """

    panelName = 'User editor'

    def __init__(self, parent, client, options):
        Panel.__init__(self, parent, client, options)
        loadUi(self, 'editor.ui', 'panels')

        self.window = parent
        self.custom_font = None
        self.custom_back = None

        self.mainwindow.codeGenerated.connect(self.on_codeGenerated)

        if not has_scintilla:
            self.actionComment.setEnabled(False)

        self.menus = None
        self.bar = None
        self.current_status = None
        self.simuuid = ''
        self.recentf_actions = []
        self.searchdlg = None
        self.menuRecent = QMenu('Recent files')

        self.menuToolsActions = []

        for fn in self.recentf:
            action = QAction(fn.replace('&', '&&'), self)
            action.setData(fn)
            action.triggered.connect(self.openRecentFile)
            self.recentf_actions.append(action)
            self.menuRecent.addAction(action)

        self.tabber = QTabWidget(self, tabsClosable=True, documentMode=True)
        self.tabber.currentChanged.connect(self.on_tabber_currentChanged)
        self.tabber.tabCloseRequested.connect(self.on_tabber_tabCloseRequested)

        self.toolconfig = options.get('tools')

        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.addWidget(self.tabber)
        self.mainFrame.setLayout(hlayout)

        self.editors = []    # tab index -> editor
        self.filenames = {}  # editor -> filename
        self.watchers = {}   # editor -> QFileSystemWatcher
        self.currentEditor = None

        self.saving = False  # True while saving
        self.warnWidget.hide()

        self.simOutStack.setCurrentIndex(0)
        hdr = self.simRanges.header()
        if hasattr(hdr, 'setResizeMode'):  # Qt4
            hdr.setResizeMode(QHeaderView.ResizeToContents)
        else:
            hdr.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.simPane.hide()

        self.splitter.restoreState(self.splitterstate)
        self.treeModel = QFileSystemModel()
        idx = self.treeModel.setRootPath('/')
        self.treeModel.setNameFilters(['*.py', '*.txt'])
        self.treeModel.setNameFilterDisables(False)  # hide them
        self.fileTree.setModel(self.treeModel)
        self.fileTree.header().hideSection(1)
        self.fileTree.header().hideSection(2)
        self.fileTree.header().hideSection(3)
        self.fileTree.header().hide()
        self.fileTree.setRootIndex(idx)
        self.actionShowScripts = self.scriptsPane.toggleViewAction()
        self.actionShowScripts.setText('Show Script Browser')

        self.activeGroup = QActionGroup(self)
        self.activeGroup.addAction(self.actionRun)
        self.activeGroup.addAction(self.actionSimulate)
        self.activeGroup.addAction(self.actionUpdate)

        client.simmessage.connect(self.on_client_simmessage)
        client.simresult.connect(self.on_client_simresult)
        if client.isconnected:
            self.on_client_connected()
        client.connected.connect(self.on_client_connected)
        client.setup.connect(self.on_client_connected)
        client.cache.connect(self.on_client_cache)
        client.experiment.connect(self.on_client_experiment)

        if self.openfiles:
            for fn in self.openfiles:
                self.openFile(fn, quiet=True)
        else:
            self.newFile()

    def __del__(self):
        # On some systems the  QFilesystemWatchers deadlock on application exit
        # so destroy them explicitly
        self.watchers.clear()

    def setViewOnly(self, viewonly):
        self.activeGroup.setEnabled(not viewonly)

    def getMenus(self):
        menuFile = QMenu('&File', self)
        menuFile.addAction(self.actionNew)
        menuFile.addAction(self.actionOpen)
        menuFile.addAction(self.menuRecent.menuAction())
        menuFile.addAction(self.actionSave)
        menuFile.addAction(self.actionSaveAs)
        menuFile.addAction(self.actionReload)
        menuFile.addSeparator()
        menuFile.addAction(self.actionPrint)

        menuView = QMenu('&View', self)
        menuView.addAction(self.actionShowScripts)

        menuEdit = QMenu('&Edit', self)
        menuEdit.addAction(self.actionUndo)
        menuEdit.addAction(self.actionRedo)
        menuEdit.addSeparator()
        menuEdit.addAction(self.actionCut)
        menuEdit.addAction(self.actionCopy)
        menuEdit.addAction(self.actionPaste)
        menuEdit.addSeparator()
        menuEdit.addAction(self.actionComment)
        menuEdit.addSeparator()
        menuEdit.addAction(self.actionFind)

        menuScript = QMenu('&Script', self)
        menuScript.addSeparator()
        menuScript.addAction(self.actionRun)
        menuScript.addAction(self.actionSimulate)
        menuScript.addAction(self.actionUpdate)
        menuScript.addSeparator()
        menuScript.addAction(self.actionGet)

        if self.toolconfig:
            menuTools = QMenu('Editor t&ools', self)
            createToolMenu(self, self.toolconfig, menuTools)
            menus = [menuFile, menuView, menuEdit, menuScript, menuTools]
        else:
            menus = [menuFile, menuView, menuEdit, menuScript]

        self.menus = menus
        return self.menus

    def getToolbars(self):
        if not self.bar:
            bar = QToolBar('Editor')
            bar.addAction(self.actionNew)
            bar.addAction(self.actionOpen)
            bar.addAction(self.actionSave)
            bar.addSeparator()
            bar.addAction(self.actionPrint)
            bar.addSeparator()
            bar.addAction(self.actionUndo)
            bar.addAction(self.actionRedo)
            bar.addSeparator()
            bar.addAction(self.actionCut)
            bar.addAction(self.actionCopy)
            bar.addAction(self.actionPaste)
            bar.addSeparator()
            bar.addAction(self.actionRun)
            bar.addAction(self.actionSimulate)
            bar.addAction(self.actionGet)
            bar.addAction(self.actionUpdate)
            showToolText(bar, self.actionRun)
            showToolText(bar, self.actionSimulate)
            showToolText(bar, self.actionGet)
            showToolText(bar, self.actionUpdate)
            self.bar = bar

        return [self.bar]

    def updateStatus(self, status, exception=False):
        self.current_status = status

    def setCustomStyle(self, font, back):
        self.custom_font = font
        self.custom_back = back
        self.simOutView.setFont(font)
        self.simOutViewErrors.setFont(font)
        for editor in self.editors:
            self._updateStyle(editor)

    def _updateStyle(self, editor):
        if self.custom_font is None:
            return
        bold = QFont(self.custom_font)
        bold.setBold(True)
        if has_scintilla:
            lexer = editor.lexer()
            lexer.setDefaultFont(self.custom_font)
            for i in range(16):
                lexer.setFont(self.custom_font, i)
            # make keywords bold
            lexer.setFont(bold, 5)
        else:
            editor.setFont(self.custom_font)
        if has_scintilla:
            lexer.setPaper(self.custom_back)
        else:
            setBackgroundColor(editor, self.custom_back)

    def enableFileActions(self, on):
        for action in [
            self.actionSave, self.actionSaveAs, self.actionReload,
            self.actionPrint, self.actionUndo, self.actionRedo, self.actionCut,
            self.actionCopy, self.actionPaste, self.actionFind, self.actionRun,
            self.actionSimulate, self.actionUpdate
        ]:
            action.setEnabled(on)
        for action in [self.actionComment]:
            action.setEnabled(on and has_scintilla)

    def on_codeGenerated(self, code):
        if self.currentEditor:
            self.currentEditor.beginUndoAction()
            if self.currentEditor.text():
                res = OverwriteQuestion().exec_()
                if res == QMessageBox.Apply:
                    self.currentEditor.clear()
                elif res == QMessageBox.Cancel:
                    return
            # append() and setText() would clear undo history in QScintilla,
            # therefore we use these calls
            self.currentEditor.moveToEnd()
            self.currentEditor.insert(code)
            self.currentEditor.endUndoAction()
        else:
            self.showError('No script is opened at the moment.')

    def on_tabber_currentChanged(self, index):
        self.enableFileActions(index >= 0)
        if index == -1:
            self.currentEditor = None
            self.window.setWindowTitle('%s editor' % self.mainwindow.instrument)
            return
        editor = self.editors[index]
        fn = self.filenames[editor]
        if fn:
            self.window.setWindowTitle('%s[*] - %s editor' %
                                       (fn, self.mainwindow.instrument))
        else:
            self.window.setWindowTitle('New[*] - %s editor' %
                                       self.mainwindow.instrument)
        self.window.setWindowModified(editor.isModified())
        self.actionSave.setEnabled(editor.isModified())
        self.actionUndo.setEnabled(editor.isModified())
        self.currentEditor = editor
        if self.searchdlg:
            self.searchdlg.setEditor(editor)

    def on_tabber_tabCloseRequested(self, index):
        editor = self.editors[index]
        self._close(editor)

    def _close(self, editor):
        if not self.checkDirty(editor):
            return
        index = self.editors.index(editor)
        del self.editors[index]
        del self.filenames[editor]
        del self.watchers[editor]
        self.tabber.removeTab(index)

    def setDirty(self, dirty):
        if self.sender() is self.currentEditor:
            self.actionSave.setEnabled(dirty)
            self.actionUndo.setEnabled(dirty)
            self.window.setWindowModified(dirty)
            index = self.tabber.currentIndex()
            tt = self.tabber.tabText(index).rstrip('*')
            self.tabber.setTabText(index, tt + (dirty and '*' or ''))

    def loadSettings(self, settings):
        self.recentf = settings.value('recentf') or []
        self.splitterstate = settings.value('splitter', '', QByteArray)
        self.openfiles = settings.value('openfiles') or []

    def saveSettings(self, settings):
        settings.setValue('splitter', self.splitter.saveState())
        settings.setValue('openfiles',
                          [self.filenames[e] for e in self.editors
                           if self.filenames[e]])

    def requestClose(self):
        for editor in self.editors:
            if not self.checkDirty(editor):
                return False
        return True

    def createEditor(self):
        if has_scintilla:
            editor = QsciScintillaCustom(self)
            lexer = QsciLexerPython(editor)
            editor.setUtf8(True)
            editor.setLexer(lexer)
            editor.setAutoIndent(True)
            editor.setEolMode(QsciScintilla.EolUnix)
            editor.setIndentationsUseTabs(False)
            editor.setIndentationGuides(True)
            editor.setTabIndents(True)
            editor.setBackspaceUnindents(True)
            editor.setTabWidth(4)
            editor.setIndentationWidth(0)
            editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
            editor.setFolding(QsciScintilla.PlainFoldStyle)
            editor.setIndentationGuidesForegroundColor(QColor("#CCC"))
            editor.setWrapMode(QsciScintilla.WrapCharacter)
            editor.setMarginLineNumbers(1, True)
            editor.setMarginWidth(
                1, 5 + 4 * QFontMetrics(editor.font()).averageCharWidth())
        else:
            editor = QScintillaCompatible(self)
        # editor.setFrameStyle(0)
        editor.modificationChanged.connect(self.setDirty)
        self._updateStyle(editor)
        return editor

    def on_client_connected(self):
        self._set_scriptdir()

    def _set_scriptdir(self):
        initialdir = self.client.eval('session.experiment.scriptpath', '')
        if initialdir:
            idx = self.treeModel.setRootPath(initialdir)
            self.fileTree.setRootIndex(idx)

    def on_client_cache(self, data):
        (_time, key, _op, _value) = data
        if key.endswith('/scriptpath'):
            self.on_client_connected()

    def on_client_simmessage(self, simmessage):
        if simmessage[5] != self.simuuid:
            return
        self.simOutView.addMessage(simmessage)
        if simmessage[2] >= WARNING:
            self.simOutViewErrors.addMessage(simmessage)

    def on_client_simresult(self, data):
        self.actionSimulate.setEnabled(True)
        (timing, devinfo, uuid) = data
        if uuid != self.simuuid:
            return

        # show timing
        if timing < 0:
            self.simTotalTime.setText('Error occurred')
            self.simFinished.setText('See messages')
        else:
            self.simTotalTime.setText(formatDuration(timing, precise=False))
            self.simFinished.setText(formatEndtime(timing))

        # device ranges
        for devname, (_dval, dmin, dmax, aliases) in iteritems(devinfo):
            if dmin is not None:
                aliascol = 'aliases: ' + ', '.join(aliases) if aliases else ''
                item = QTreeWidgetItem([devname, dmin, '-', dmax, '', aliascol])
                self.simRanges.addTopLevelItem(item)

        self.simRanges.sortByColumn(0, Qt.AscendingOrder)
        self.simPane.show()

    def on_client_experiment(self, data):
        (_, proptype) = data
        self._set_scriptdir()
        self.simPane.hide()
        if proptype == 'user':
            # close existing tabs when switching TO a user experiment
            for index in range(len(self.editors) - 1, -1, -1):
                self.on_tabber_tabCloseRequested(index)
            # if all tabs have been closed, open a new file
            if not self.tabber.count():
                self.on_actionNew_triggered()

    def on_fileTree_doubleClicked(self, idx):
        fpath = self.treeModel.filePath(idx)
        for i, editor in enumerate(self.editors):
            if self.filenames[editor] == fpath:
                self.tabber.setCurrentIndex(i)
                return
        self.openFile(fpath)

    @pyqtSlot()
    def on_actionPrint_triggered(self):
        if has_scintilla:
            printer = Printer()
            printer.setOutputFileName('')
            printer.setDocName(self.filenames[self.currentEditor])
            # printer.setFullPage(True)
            if QPrintDialog(printer, self).exec_() == QDialog.Accepted:
                lexer = self.currentEditor.lexer()
                bgcolor = lexer.paper(0)
                # printer prints background color too, so set it to white
                lexer.setPaper(Qt.white)
                printer.printRange(self.currentEditor)
                lexer.setPaper(bgcolor)
        else:
            printer = QPrinter()
            printer.setOutputFileName('')
            if QPrintDialog(printer, self).exec_() == QDialog.Accepted:
                getattr(self.currentEditor, 'print')(printer)

    def validateScript(self):
        script = self.currentEditor.text()
        # XXX: this does not apply to .txt (SPM) scripts
        # try:
        #    compile(script, 'script', 'exec')
        # except SyntaxError as err:
        #    self.showError('Syntax error in script: %s' % err)
        #    self.currentEditor.setCursorPosition(err.lineno - 1, err.offset)
        #    return
        return script

    @pyqtSlot()
    def on_actionRun_triggered(self):
        script = self.validateScript()
        if script is None:
            return
        if not self.checkDirty(self.currentEditor, askonly=True):
            return
        if self.current_status != 'idle':
            if not self.askQuestion('A script is currently running, do you '
                                    'want to queue this script?', True):
                return
        self.client.run(script, self.filenames[self.currentEditor])

    @pyqtSlot()
    def on_actionSimulate_triggered(self):
        script = self.validateScript()
        if script is None:
            return
        if not self.checkDirty(self.currentEditor, askonly=True):
            return
        self.actionSimulate.setEnabled(False)
        self.simuuid = str(uuid1())
        self.client.tell('simulate', self.filenames[self.currentEditor], script,
                         self.simuuid)
        self.clearSimPane()
        self.simPane.show()

    @pyqtSlot()
    def on_actionUpdate_triggered(self):
        script = self.validateScript()
        if script is None:
            return
        if not self.checkDirty(self.currentEditor, askonly=True):
            return
        reason, ok = QInputDialog.getText(
            self, 'Update reason', 'For the logbook, you can enter a reason '
            'for the update here:', text='no reason specified')
        if not ok:
            return
        self.client.tell('update', script, reason)

    @pyqtSlot()
    def on_actionGet_triggered(self):
        script = self.client.ask('getscript')
        if script is not None:
            editor = self.newFile()
            editor.setText(script)

    def clearSimPane(self):
        self.simOutView.clear()
        self.simOutViewErrors.clear()
        self.simRanges.clear()
        self.simTotalTime.setText('')
        self.simFinished.setText('')

    def on_simErrorsOnly_toggled(self, on):
        self.simOutStack.setCurrentIndex(on)

    def checkDirty(self, editor, askonly=False):
        if not editor.isModified():
            return True
        if self.filenames[editor]:
            message = 'Save changes in %s before continuing?' % \
                self.filenames[editor]
        else:
            message = 'Save new file before continuing?'
        buttons = QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        if askonly:
            buttons = QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
        rc = QMessageBox.question(self, 'User Editor', message, buttons)
        if rc in (QMessageBox.Save, QMessageBox.Yes):
            return self.saveFile(editor)
        if rc in (QMessageBox.Discard, QMessageBox.No):
            return True
        return False

    def on_fileSystemWatcher_fileChanged(self, filename):
        if self.saving:
            return
        editor = watcher = None
        for editor, watcher in iteritems(self.watchers):
            if watcher is self.sender():
                break
        else:
            return
        if editor.isModified():
            # warn the user
            self.warnText.setText(
                'The file %r has changed on disk, but has also been edited'
                ' here.\nPlease use either File-Reload to load the'
                ' version on disk or File-Save to save this version.'
                % self.filenames[editor])
            self.warnWidget.show()
        else:
            # reload without asking
            try:
                with io.open(self.filenames[editor], 'r', encoding='utf-8') as f:
                    text = f.read()
            except Exception:
                return
            editor.setText(text)
            editor.setModified(False)
        # re-add the filename to the watcher if it was deleted
        # (happens for programs that do delete-write on save)
        if not watcher.files():
            watcher.addPath(self.filenames[editor])

    @pyqtSlot()
    def on_actionNew_triggered(self):
        self.newFile()

    def newFile(self):
        editor = self.createEditor()
        editor.setModified(False)
        self.editors.append(editor)
        self.filenames[editor] = ''
        self.watchers[editor] = QFileSystemWatcher(self)
        self.watchers[editor].fileChanged.connect(
            self.on_fileSystemWatcher_fileChanged)
        self.tabber.addTab(editor, '(New script)')
        self.tabber.setCurrentWidget(editor)
        self.clearSimPane()
        editor.setFocus()
        return editor

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        if self.currentEditor is not None and self.filenames[self.currentEditor]:
            initialdir = path.dirname(self.filenames[self.currentEditor])
        else:
            initialdir = self.client.eval('session.experiment.scriptpath', '')
        fn = QFileDialog.getOpenFileName(self, 'Open script', initialdir,
                                         'Script files (*.py *.txt)')[0]
        if not fn:
            return
        self.openFile(fn)
        self.addToRecentf(fn)

    @pyqtSlot()
    def on_actionReload_triggered(self):
        fn = self.filenames[self.currentEditor]
        if not fn:
            return
        if not self.checkDirty(self.currentEditor):
            return
        try:
            with io.open(fn, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as err:
            return self.showError('Opening file failed: %s' % err)
        self.currentEditor.setText(text)
        self.clearSimPane()

    def openRecentFile(self):
        self.openFile(self.sender().data())

    def openFile(self, fn, quiet=False):
        try:
            with io.open(fn.encode(sys.getfilesystemencoding()), 'r',
                         encoding='utf-8') as f:
                text = f.read()
        except Exception as err:
            if quiet:
                return
            return self.showError('Opening file failed: %s' % err)

        editor = self.createEditor()
        editor.setText(text)
        editor.setModified(False)

        # replace tab if it's a single new file
        if len(self.editors) == 1 and not self.filenames[self.editors[0]] and \
           not self.editors[0].isModified():
            self._close(self.editors[0])

        self.editors.append(editor)
        self.filenames[editor] = fn
        self.watchers[editor] = QFileSystemWatcher(self)
        self.watchers[editor].fileChanged.connect(
            self.on_fileSystemWatcher_fileChanged)
        self.watchers[editor].addPath(fn)
        self.tabber.addTab(editor, path.basename(fn))
        self.tabber.setCurrentWidget(editor)
        self.clearSimPane()
        editor.setFocus()

    def addToRecentf(self, fn):
        new_action = QAction(fn.replace('&', '&&'), self)
        new_action.setData(fn)
        new_action.triggered.connect(self.openRecentFile)
        if self.recentf_actions:
            self.menuRecent.insertAction(self.recentf_actions[0], new_action)
            self.recentf_actions.insert(0, new_action)
            del self.recentf_actions[10:]
        else:
            self.menuRecent.addAction(new_action)
            self.recentf_actions.append(new_action)
        with self.sgroup as settings:
            settings.setValue('recentf',
                              [a.data() for a in self.recentf_actions])

    @pyqtSlot()
    def on_actionSave_triggered(self):
        self.saveFile(self.currentEditor)
        self.window.setWindowTitle(
            '%s[*] - %s editor' %
            (self.filenames[self.currentEditor], self.mainwindow.instrument))

    @pyqtSlot()
    def on_actionSaveAs_triggered(self):
        self.saveFileAs(self.currentEditor)
        self.window.setWindowTitle(
            '%s[*] - %s editor' %
            (self.filenames[self.currentEditor], self.mainwindow.instrument))

    def saveFile(self, editor):
        if not self.filenames[editor]:
            return self.saveFileAs(editor)

        try:
            self.saving = True
            try:
                with io.open(self.filenames[editor], 'w', encoding='utf-8') as f:
                    f.write(editor.text())
            finally:
                self.saving = False
        except Exception as err:
            self.showError('Writing file failed: %s' % err)
            return False

        self.watchers[editor].addPath(self.filenames[editor])
        editor.setModified(False)
        return True

    def saveFileAs(self, editor):
        if self.filenames[editor]:
            initialdir = path.dirname(self.filenames[editor])
        else:
            initialdir = self.client.eval('session.experiment.scriptpath', '')
        if self.client.eval('session.spMode', False):
            defaultext = '.txt'
            flt = 'Script files (*.txt *.py)'
        else:
            defaultext = '.py'
            flt = 'Script files (*.py *.txt)'
        fn = QFileDialog.getSaveFileName(self, 'Save script', initialdir, flt)[0]
        if not fn:
            return False
        if not fn.endswith(('.py', '.txt')):
            fn += defaultext
        self.addToRecentf(fn)
        self.watchers[editor].removePath(self.filenames[editor])
        self.filenames[editor] = fn
        self.tabber.setTabText(self.editors.index(editor), path.basename(fn))
        return self.saveFile(editor)

    @pyqtSlot()
    def on_actionFind_triggered(self):
        if not self.searchdlg:
            self.searchdlg = SearchDialog(self, self.currentEditor,
                                          has_scintilla)
        self.searchdlg.setEditor(self.currentEditor)
        self.searchdlg.show()

    @pyqtSlot()
    def on_actionUndo_triggered(self):
        self.currentEditor.undo()

    @pyqtSlot()
    def on_actionRedo_triggered(self):
        self.currentEditor.redo()

    @pyqtSlot()
    def on_actionCut_triggered(self):
        self.currentEditor.cut()

    @pyqtSlot()
    def on_actionCopy_triggered(self):
        self.currentEditor.copy()

    @pyqtSlot()
    def on_actionPaste_triggered(self):
        self.currentEditor.paste()

    @pyqtSlot()
    def on_actionComment_triggered(self):
        clen = len(COMMENT_STR)
        # act on selection?
        if self.currentEditor.hasSelectedText():
            # get the selection boundaries
            line1, index1, line2, index2 = self.currentEditor.getSelection()
            if index2 == 0:
                endLine = line2 - 1
            else:
                endLine = line2
            assert endLine >= line1

            self.currentEditor.beginUndoAction()
            # iterate over the lines
            action = []
            for line in range(line1, endLine + 1):
                if self.currentEditor.text(line).startswith(COMMENT_STR):
                    self.currentEditor.setSelection(line, 0, line, clen)
                    self.currentEditor.removeSelectedText()
                    action.append(-1)
                else:
                    self.currentEditor.insertAt(COMMENT_STR, line, 0)
                    action.append(1)
            # adapt original selection boundaries
            if index1 > 0:
                if action[0] == 1:
                    index1 += clen
                else:
                    index1 = max(0, index1 - clen)
            if endLine > line1 and index2 > 0:
                if action[-1] == 1:
                    index2 += clen
                else:
                    index2 = max(0, index2 - clen)
            # restore selection accordingly
            self.currentEditor.setSelection(line1, index1, line2, index2)
            self.currentEditor.endUndoAction()
        else:
            # comment line
            line, _ = self.currentEditor.getCursorPosition()
            self.currentEditor.beginUndoAction()
            if self.currentEditor.text(line).startswith(COMMENT_STR):
                self.currentEditor.setSelection(line, 0, line, clen)
                self.currentEditor.removeSelectedText()
            else:
                self.currentEditor.insertAt(COMMENT_STR, line, 0)
            self.currentEditor.endUndoAction()

    def on_simOutView_anchorClicked(self, url):
        if url.scheme() == 'trace':
            TracebackDialog(self, self.simOutView, url.path()).show()

    def on_simOutViewErrors_anchorClicked(self, url):
        self.on_simOutView_anchorClicked(url)
