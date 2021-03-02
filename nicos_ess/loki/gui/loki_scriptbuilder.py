from functools import partial

from nicos.clients.gui.panels import Panel
from nicos.clients.gui.utils import loadUi
from nicos.guisupport.qt import pyqtSlot, QTableWidgetItem, QHeaderView, \
    Qt
from nicos.utils import findResource

TABLE_QSS = "alternate-background-color: aliceblue;"


class LokiScriptBuilderPanel(Panel):
    def __init__(self, parent, client, options):
        Panel.__init__(self, parent, client, options)
        loadUi(self,
               findResource('nicos_ess/loki/gui/ui_files/loki_scriptbuilder.ui'))

        self.window = parent

        trans_options = ['TRANS First', 'SANS First', 'Simultaneous']
        self.comboOrder.addItems(trans_options)

        duration_options = ['Mevents', 'seconds', 'frames']
        self.comboDurationType.addItems(duration_options)

        self.permanent_columns = {
            "position": "Position",
            "sample": "Sample",
            "thickness": "Thickness\n(mm)",
            "trans_duration": "TRANS\nDuration",
            "sans_duration": "SANS\nDuration"
        }

        self.optional_columns = {
            "temperature": ("Temperature", self.chkShowTempColumn),
            "pre-command": ("Pre-command", self.chkShowPreCommand),
            "post-command": ("Post-command", self.chkShowPostCommand)
        }

        self.columns_in_order = [name for name in self.permanent_columns.keys()]
        self.columns_in_order.extend(self.optional_columns.keys())

        self._init_table()

    def _init_table(self, num_rows=25):
        self.tableScript.setColumnCount(len(self.columns_in_order))
        for i, name in enumerate(self.columns_in_order):
            if name in self.permanent_columns:
                title = self.permanent_columns[name]
            else:
                title = self.optional_columns[name][0]
            self.tableScript.setHorizontalHeaderItem(i, QTableWidgetItem(title))

        # Configure optional columns.
        for name, details in self.optional_columns.items():
            _, checkbox = details
            checkbox.stateChanged.connect(
                partial(self._on_optional_column_toggled, name))
            self._hide_column(name)

        # Table formatting
        self.tableScript.horizontalHeader().setStretchLastSection(True)
        self.tableScript.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableScript.resizeColumnsToContents()
        self.tableScript.setAlternatingRowColors(True)
        self.tableScript.setStyleSheet(TABLE_QSS)

        self.tableScript.setRowCount(num_rows)

    @pyqtSlot()
    def on_bulkUpdateButton_clicked(self):
        for index in self.tableScript.selectionModel().selectedIndexes():
            self._update_cell(index.row(), index.column(), self.txtValue.text())

    @pyqtSlot()
    def on_clearTableButton_clicked(self):
        for row in range(self.tableScript.rowCount()):
            for column in range(self.tableScript.columnCount()):
                self._update_cell(row, column, '')

    def _update_cell(self, row, column, new_value):
        item = self.tableScript.item(row, column)
        if not item:
            self.tableScript.setItem(row, column, QTableWidgetItem(new_value))
        else:
            item.setText(new_value)

    def _on_optional_column_toggled(self, column_name, state):
        if state == Qt.Checked:
            self._show_column(column_name)
        else:
            self._hide_column(column_name)

    def _hide_column(self, column_name):
        column_number = self.columns_in_order.index(column_name)
        self.tableScript.setColumnHidden(column_number, True)

    def _show_column(self, column_name):
        column_number = self.columns_in_order.index(column_name)
        self.tableScript.setColumnHidden(column_number, False)
