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
#   AÜC Hardal <umit.hardal@ess.eu>
#
# *****************************************************************************

"""LoKI Experiment Configuration dialog."""
import itertools

from nicos.guisupport.qt import Qt, QLineEdit

from nicos.clients.gui.utils import loadUi
from nicos.utils import findResource

from nicos_ess.loki.gui.loki_panel import LokiPanelBase
from nicos_ess.utilities.validators import DoubleValidator


class LokiExperimentPanel(LokiPanelBase):
    panelName = 'LoKI Instrument Setup'

    def __init__(self, parent, client, options):
        LokiPanelBase.__init__(self, parent, client, options)
        loadUi(self, findResource('nicos_ess/loki/gui/ui_files/exp_config.ui'))

        self.holder_info = options.get('holder_info', [])
        self.instrument = options.get('instrument', 'loki')
        self.initialise_connection_status_listeners()
        self.initialise_markups()
        self.initialise_validators()

        self.envComboBox.addItems(['Sample Changer A', 'Sample Changer B'])
        # Start with a "no item", ie, empty selection.
        self.envComboBox.setCurrentIndex(-1)

        # Hide read-only properties and hide and disable reference cell
        # positions until a sample environment is chosen by the user.
        self.propertiesGroupBox.setVisible(False)

        # Hide and disable cell position properties which shall be only
        # available for sample environments that holds them.
        self.refPosGroupBox.setVisible(False)

        self.refCellSpinBox.valueChanged.connect(
            self._set_sample_changer_ref_cell
        )

        self.envComboBox.activated.connect(self._activate_environment_settings)

        # Listen to changes in Aperture and Detector Offset values
        self.apXBox.textChanged.connect(self.set_apt_pos_x)
        self.apYBox.textChanged.connect(self.set_apt_pos_y)
        self.apWBox.textChanged.connect(self.set_apt_width)
        self.apHBox.textChanged.connect(self.set_apt_height)
        self.offsetBox.textChanged.connect(self.set_det_offset)

        # Listen to changes in environments
        self.refPosXBox.textChanged.connect(self.set_ref_pos_x)
        self.refPosYBox.textChanged.connect(self.set_ref_pos_y)

        # Disable apply buttons in both settings until an action taken by the
        # user.
        self.sampleSetApply.setEnabled(False)
        self.instSetApply.setEnabled(False)

    def initialise_markups(self):
        for box in self._get_editable_settings():
            box.setAlignment(Qt.AlignRight)
            box.setPlaceholderText('0.0')

    def initialise_validators(self):
        _validator_values = {  # in units of mm
            'bottom': 0.0,
            'top': 1000.0,
            'decimal': 5,
        }
        validator = DoubleValidator(**_validator_values)
        for box in self._get_editable_settings():
            box.setValidator(validator)

    def _get_editable_settings(self):
        _editable_settings = list(
            itertools.chain(
                self.aptGroupBox.findChildren(QLineEdit),
                self.detGroupBox.findChildren(QLineEdit)
            )
        )
        return _editable_settings

    def setViewOnly(self, viewonly):
        self.sampleSetGroupBox.setEnabled(not viewonly)
        self.instSetGroupBox.setEnabled(not viewonly)

    def _activate_environment_settings(self):
        # Enable sample environments
        self.propertiesGroupBox.setVisible(True)

        self._set_cell_indices()
        self.refPosGroupBox.setVisible(True)
        self.refPosGroupBox.setEnabled(True)
        self.refCellSpinBox.setFocus()

    def _set_cell_indices(self):
        # Setting minimum and maximum values for the number of cells not only
        # ensures we have the correct numbers to choose from in the UI but also
        # prevents user errors as any integer that is not in [min, max] is not
        # allowed (or non-integer types).
        self.refCellSpinBox.setMinimum(1)

    def _set_sample_changer_ref_cell(self):
        pass

    def set_det_offset(self, value):
        pass

    def set_apt_pos_x(self, value):
        pass

    def set_apt_pos_y(self, value):
        pass

    def set_apt_width(self, value):
        pass

    def set_apt_height(self, value):
        pass

    def set_ref_pos_x(self, value):
        pass

    def set_ref_pos_y(self, value):
        pass
