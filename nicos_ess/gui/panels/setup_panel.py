#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2021 by the NICOS contributors (see AUTHORS)
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
#   Michele Brambilla <michele.brambilla@psi.ch>
#   Ebad Kamil <Ebad.Kamil@ess.eu>
#   Matt Clarke <matt.clarke@ess.eu>
#   Kenan Muric <kenan.muric@ess.eu>
#   AÜC Hardal <umit.hardal@ess.eu>
#
# *****************************************************************************

"""NICOS GUI experiment setup window."""
from copy import deepcopy

from PyQt5.QtWidgets import QHeaderView

from nicos.clients.gui.panels import Panel, PanelDialog
from nicos.clients.gui.panels.setup_panel import \
    SetupsPanel as DefaultSetupsPanel, combineUsers, splitUsers
from nicos.clients.gui.utils import loadUi
from nicos.core import ConfigurationError
from nicos.guisupport.qt import QDialogButtonBox, QMessageBox, Qt, \
    pyqtSignal, pyqtSlot, QAbstractTableModel
from nicos.utils import decodeAny, findResource

from nicos_ess.gui import uipath


class SamplesModel(QAbstractTableModel):
    data_updated = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.sample_properties = ["name", "formula", "number of", "mass/volume",
                                  "density"]
        self._samples = []
        self._table_data = self.empty_table(len(self.sample_properties),
                                            len(self._samples))

    @property
    def samples(self):
        return self._samples

    @samples.setter
    def samples(self, samples):
        self._samples = samples

        new_table = self.empty_table(len(self.sample_properties),
                                     len(self._samples))
        for i, sample in enumerate(self._samples):
            for j, key in enumerate(sample.keys()):
                new_table[j][i] = sample[key]

        self._table_data = new_table
        self.layoutChanged.emit()

    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self._table_data[index.row()][index.column()]

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._table_data[index.row()][index.column()] = value
            self._samples[index.column()][self.sample_properties[index.row()]] = value
            self.data_updated.emit()
            return True

    def rowCount(self, index):
        return len(self._table_data)

    def columnCount(self, index):
        return len(self._samples)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return section + 1
        if role == Qt.DisplayRole and orientation == Qt.Vertical:
            return self.sample_properties[section]

    def setHeaderData(self, section, orientation, value, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            self._header_data[section] = value
            self.headerDataChanged.emit(orientation, section, section)
        return True

    def empty_table(self, rows, columns):
        return [[""] * columns for _ in range(rows)]

    @property
    def num_rows(self):
        return len(self._table_data)


class ProposalSettings:
    def __init__(self, proposal_id='', title='', users='', local_contacts='',
                 notifications='', abort_on_error='', samples=None):
        self.proposal_id = proposal_id
        self.title = title
        self.users = users
        self.local_contacts = local_contacts
        self.samples = samples if samples else []
        self.notifications = notifications
        self.abort_on_error = abort_on_error

    def __eq__(self, other):
        if self.proposal_id != other.proposal_id \
                or self.title != other.title \
                or self.users != other.users \
                or self.local_contacts != other.local_contacts \
                or self.notifications != other.notifications \
                or self.abort_on_error != other.abort_on_error\
                or self.samples != other.samples:
            return False
        return True


class ExpPanel(Panel):
    """Provides a panel with several input fields for the experiment settings.

    Options:

    * ``new_exp_panel`` -- class name of the panel which should be opened after
      a new experiment has been started.
    """

    panelName = 'Experiment setup'
    exp_proposal_activated = pyqtSignal()

    def __init__(self, parent, client, options):
        Panel.__init__(self, parent, client, options)
        loadUi(self, findResource('nicos_ess/gui/panels/ui_files/setup_exp.ui'))

        self.old_proposal_settings = ProposalSettings()
        self.new_proposal_settings = deepcopy(self.old_proposal_settings)

        self.model = SamplesModel()
        self.model.data_updated.connect(self.on_samples_changed)
        self.sampleTable.setModel(self.model)
        self.sampleTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.applyWarningLabel.setStyleSheet('color: red')
        self.applyWarningLabel.setVisible(False)
        self.discardButton.setVisible(False)

        self._text_controls = (self.expTitle, self.users, self.localContacts,
                               self.proposalNum, self.proposalQuery)

        if options.get('hide_sample', False):
            self._hide_sample_info()

        self.initialise_connection_status_listeners()

    def _hide_sample_info(self):
        self.sampleTable.hide()
        self.sampleLabel.hide()
        self.sampleLine.hide()

    def initialise_connection_status_listeners(self):
        if self.client.isconnected:
            self.on_client_connected()
        else:
            self.on_client_disconnected()
        self.client.connected.connect(self.on_client_connected)
        self.client.disconnected.connect(self.on_client_disconnected)

    def _update_proposal_info(self):
        values = self.client.eval('session.experiment.proposal, '
                                  'session.experiment.title, '
                                  'session.experiment.users, '
                                  'session.experiment.localcontact, '
                                  'session.experiment.errorbehavior', None)
        notif_emails = self.client.eval(
            'session.experiment.propinfo["notif_emails"]', [])
        samples_dict = self.client.eval('Exp.sample.samples', {})

        if values:
            self.old_proposal_settings = ProposalSettings(decodeAny(values[0]),
                                                          decodeAny(values[1]),
                                                          decodeAny(values[2]),
                                                          decodeAny(values[3]),
                                                          notif_emails,
                                                          values[4] == 'abort',
                                                          )
            self.old_proposal_settings.samples = self._extract_samples(samples_dict)
            self.new_proposal_settings = deepcopy(self.old_proposal_settings)
            # Update GUI
            self.proposalNum.setText(self.old_proposal_settings.proposal_id)
            self.expTitle.setText(self.old_proposal_settings.title)
            self.users.setText(self.old_proposal_settings.users)
            self.localContacts.setText(
                self.old_proposal_settings.local_contacts)
            self.errorAbortBox.setChecked(
                self.old_proposal_settings.abort_on_error)
            self.notifEmails.setPlainText(
                '\n'.join(self.old_proposal_settings.notifications))
            self.model.samples = self.old_proposal_settings.samples

    def _extract_samples(self, samples_dict):
        samples = []
        for sample in samples_dict.values():
            samples.append({
                'name': sample.get('sample_name', ''),
                'formula': sample.get('formula', ''),
                'number of': sample.get('number_of', 1),
                'mass/volume': sample.get('mass_volume', ''),
                'density': sample.get('density', ''),
            })
        return samples

    def on_client_connected(self):
        self._update_proposal_info()
        self._is_proposal_system_available()
        self.setViewOnly(self.client.viewonly)

    def _is_proposal_system_available(self):
        if self.client.eval('session.experiment._canQueryProposals()', None):
            self.findProposalBox.setVisible(True)
            self.proposalNum.setReadOnly(True)
        else:
            self.findProposalBox.setVisible(False)
            self.proposalNum.setReadOnly(False)

    def on_client_disconnected(self):
        for control in self._text_controls:
            control.setText("")
        self.notifEmails.setPlainText('')
        self.setViewOnly(True)

    def setViewOnly(self, is_view_only):
        for control in self._text_controls:
            control.setEnabled(not is_view_only)
        self.notifEmails.setEnabled(not is_view_only)
        self.errorAbortBox.setEnabled(not is_view_only)
        self.queryDBButton.setEnabled(not is_view_only)
        if is_view_only:
            self.applyButton.setEnabled(False)
            self.applyWarningLabel.setVisible(False)
            self.discardButton.setVisible(False)
        else:
            self._check_for_changes()

    def _format_users(self, users):
        if users:
            try:
                return splitUsers(users)
            except ValueError:
                QMessageBox.warning(self, 'Error', 'Invalid email address in '
                                    'users list')
                raise ConfigurationError from None
        return []

    def _format_local_contacts(self, local_contacts):
        if local_contacts:
            try:
                return splitUsers(local_contacts)
            except ValueError:
                QMessageBox.warning(self, 'Error', 'Invalid email address in '
                                    'local contacts list')
                raise ConfigurationError from None
        return []

    def _experiment_in_progress(self, proposal_id):
        if self.client.eval('session.experiment.serviceexp', True) and \
           self.client.eval('session.experiment.proptype', 'user') == 'user' and \
           self.client.eval('session.experiment.proposal', '') != proposal_id:
            return True
        return False

    @pyqtSlot()
    def on_applyButton_clicked(self):
        changes = []

        proposal_id = self.new_proposal_settings.proposal_id
        users = self._format_users(self.new_proposal_settings.users)
        local_contacts = self._format_local_contacts(
            self.new_proposal_settings.local_contacts)

        if self._experiment_in_progress(proposal_id):
            self.showError('Can not directly switch experiments, please use '
                           'FinishExperiment first!')
            return

        # do some work
        if proposal_id != self.old_proposal_settings.proposal_id:
            args = {'proposal': proposal_id,
                    'title': self.new_proposal_settings.title,
                    'localcontact': local_contacts, 'user': users}
            code = 'NewExperiment(%s)' % ', '.join('%s=%r' % i
                                                   for i in args.items())
            if self.client.run(code, noqueue=False) is None:
                self.showError('Could not start new experiment, a script is '
                               'still running.')
                return
            changes.append('New experiment started.')
            if self._new_exp_panel:
                dlg = PanelDialog(self, self.client, self._new_exp_panel,
                                  'New experiment')
                dlg.exec_()
        else:
            self._update_title(changes)
            self._update_users(users, changes)
            self._update_local_contacts(local_contacts, changes)
        self._update_samples(changes)
        self._update_notification_receivers(changes)
        self._update_abort_on_error(changes)

        # tell user about everything we did
        if changes:
            self.showInfo('\n'.join(changes))
        self._update_proposal_info()
        self.exp_proposal_activated.emit()

    def _update_samples(self, changes):
        if self.new_proposal_settings.samples != self.old_proposal_settings.samples:
            for index, sample in enumerate(self.model.samples):
                set_sample_cmd = f'SetSample({index}, {index}, ' \
                                 f'sample_name=\'{sample["name"]}\', ' \
                                 f'formula=\'{sample["formula"]}\', ' \
                                 f'number_of={sample["number of"]}, ' \
                                 f'mass_volume=\'{sample["mass/volume"]}\', ' \
                                 f'density=\'{sample["density"]}\')'
                self.client.run(set_sample_cmd)
            changes.append('Samples updated.')

    def _update_title(self, changes):
        if self.new_proposal_settings.title != self.old_proposal_settings.title:
            self.client.run('Exp.update(title=%r)' %
                            self.new_proposal_settings.title)
            changes.append('New experiment title set.')

    def _update_users(self, users, changes):
        if self.new_proposal_settings.users != self.old_proposal_settings.users:
            self.client.run('Exp.update(users=%r)' % users)
            changes.append('New users set.')

    def _update_local_contacts(self, local_contacts, changes):
        if self.new_proposal_settings.local_contacts != \
                    self.old_proposal_settings.local_contacts:
            self.client.run('Exp.update(localcontacts=%r)' % local_contacts)
            changes.append('New local contact(s) set.')

    def _update_abort_on_error(self, changes):
        abort_on_error = self.new_proposal_settings.abort_on_error
        if abort_on_error != self.old_proposal_settings.abort_on_error:
            self.client.run('SetErrorAbort(%s)' % abort_on_error)
            changes.append('New error behavior set.')

    def _update_notification_receivers(self, changes):
        notifications = self.new_proposal_settings.notifications
        if notifications != self.old_proposal_settings.notifications:
            self.client.run('SetMailReceivers(%s)' %
                            ', '.join(map(repr, notifications)))
            changes.append('New mail receivers set.')

    @pyqtSlot()
    def on_queryDBButton_clicked(self):
        # read values from proposal system
        try:
            proposal = self.proposalQuery.text()
            result = self.client.eval(
                'session.experiment._queryProposals(%r, {})' % proposal)

            if result:
                if len(result) != 1:
                    result = self.chooseProposal(result)
                    if not result:
                        return
                else:
                    result = result[0]
                    # check for errors/warnings:
                    if result.get('errors'):
                        self.showError('Proposal cannot be performed:\n\n' +
                                       '\n'.join(result['errors']))
                        return
                if result.get('warnings'):
                    self.showError('Proposal might have problems:\n\n' +
                                   '\n'.join(result['warnings']))
                # now transfer it into gui
                self.proposalNum.setText(result.get('proposal', proposal))
                self.expTitle.setText(result.get('title', ''))
                self.users.setText(
                    combineUsers(result.get('users', [])))
                self.localContacts.setText(
                    combineUsers(result.get('localcontacts', [])))
                self.model.samples = result['samples']
            else:
                self.showError('Querying proposal management system failed')
        except Exception as e:
            self.log.warning('error in proposal query', exc=1)
            self.showError('Querying proposal management system failed: '
                           + str(e))

    @pyqtSlot(str)
    def on_proposalNum_textChanged(self, value):
        self.new_proposal_settings.proposal_id = value.strip()
        self._check_for_changes()

    @pyqtSlot(str)
    def on_expTitle_textChanged(self, value):
        self.new_proposal_settings.title = value.strip()
        self._check_for_changes()

    @pyqtSlot(str)
    def on_users_textChanged(self, value):
        self.new_proposal_settings.users = value.strip()
        self._check_for_changes()

    def on_samples_changed(self):
        self._check_for_changes()

    @pyqtSlot(str)
    def on_localContacts_textChanged(self, value):
        self.new_proposal_settings.local_contacts = value.strip()
        self._check_for_changes()

    @pyqtSlot()
    def on_errorAbortBox_clicked(self):
        self.new_proposal_settings.abort_on_error = \
            self.errorAbortBox.isChecked()
        self._check_for_changes()

    @pyqtSlot()
    def on_notifEmails_textChanged(self):
        self.new_proposal_settings.notifications = \
            self.notifEmails.toPlainText().strip().splitlines()
        self._check_for_changes()

    def _check_for_changes(self):
        has_changed = self.new_proposal_settings != self.old_proposal_settings
        self.applyWarningLabel.setVisible(has_changed)
        self.applyButton.setEnabled(has_changed)
        self.discardButton.setVisible(has_changed)

    @pyqtSlot()
    def on_discardButton_clicked(self):
        self._update_proposal_info()
        self._check_for_changes()


class SetupsPanel(DefaultSetupsPanel):
    def finishUi(self):
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply)
        self.buttonBox.addButton(self._reload_btn, QDialogButtonBox.ResetRole)

    def setViewOnly(self, value):
        for button in self.buttonBox.buttons():
            button.setEnabled(not value)


class FinishPanel(Panel):
    """Provides a panel to finish the experiment.

    Options:

    * ``finish_exp_panel`` -- class name of the panel which should be opened
      before an experiment is finished.
    """

    panelName = 'Finish experiment'
    ui = '%s/panels/ui_files/finish_exp.ui' % uipath

    def __init__(self, parent, client, options):
        Panel.__init__(self, parent, client, options)
        loadUi(self, self.ui)
        self._finish_exp_panel = None

        # Additional dialog panels to pop up after FinishExperiment().
        self._finish_exp_panel = options.get('finish_exp_panel')
        self.finishButton.setEnabled(False)

        client.connected.connect(self.on_client_connected)
        client.disconnected.connect(self.on_client_disconnected)
        client.setup.connect(self.on_client_connected)

    def on_client_connected(self):
        if not self.client.viewonly:
            self.finishButton.setEnabled(True)

    def on_client_disconnected(self):
        self.finishButton.setEnabled(False)

    def setViewOnly(self, value):
        self.finishButton.setEnabled(self.client.isconnected and not value)

    def on_new_experiment_proposal(self):
        if not self.client.viewonly:
            self.finishButton.setEnabled(True)

    @pyqtSlot()
    def on_finishButton_clicked(self):
        if self._finish_exp_panel:
            dlg = PanelDialog(self, self.client, self._finish_exp_panel,
                              'Finish experiment')
            dlg.exec_()
        if self.client.run('FinishExperiment()', noqueue=True) is None:
            self.showError('Could not finish experiment, a script '
                           'is still running.')
        else:
            self.finishButton.setEnabled(False)
            self.show_finish_message()

    def show_finish_message(self):
        msg_box = QMessageBox()
        msg_box.setText('Experiment successfully finished.')
        return msg_box.exec_()
