#  -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2022 by the NICOS contributors (see AUTHORS)
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
#   Georg Brandl <g.brandl@fz-juelich.de>
#
# *****************************************************************************

"""NICOS GUI default configuration."""

main_window = docked(
    tabbed(
        ('Setup',
         tabbed(
             ('Experiment',
              panel('nicos_sinq.gui.panels.setup_panel.ExpPanel')),
             ('Instrument',
              panel('nicos.clients.flowui.panels.setup_panel.SetupsPanel')),
         ),
         ),
        ('  ', panel('nicos.clients.flowui.panels.empty.EmptyPanel')),
        ('Instrument interaction',
         hsplit(
             vbox(
                 panel('nicos.clients.flowui.panels.cmdbuilder.CommandPanel',
                       modules=['nicos.clients.gui.cmdlets'],),
                 tabbed(
                     ('Output',
                      panel('nicos.clients.flowui.panels.console.ConsolePanel',
                            hasinput=False)),
                     ('Scan Plot',
                      panel('nicos.clients.flowui.panels.scans.ScansPanel')),
                     ('Detector Image',
                      panel('nicos_sinq.sans.gui.panels.live.SansLiveDataPanel')
                      ),
                     ('Script Status',
                      panel(
                          'nicos.clients.flowui.panels.status.ScriptStatusPanel',
                          eta=True)),
                 ),
             ),  # vsplit
             panel(
                 'nicos.clients.flowui.panels.devices.DevicesPanel',
                 dockpos='right',
                 param_display={'tas': 'scanmode',
                                'Exp': ['lastpoint', 'lastscan']},
                 filters=[('Detector', 'det'),
                          ('Temperatures', '^T'),
                          ],
             ),
         ),  # hsplit
         ),
        ('Batch file generation',
         vsplit(
             panel('nicos.clients.gui.panels.scriptbuilder.CommandsPanel'),
             panel('nicos.clients.flowui.panels.editor.EditorPanel',
                   tools=None),),
         ),
        ('Detector Image',
         panel('nicos_sinq.sans.gui.panels.live.SansLiveDataPanel')),
        ('History',
         panel('nicos.clients.flowui.panels.history.HistoryPanel'),),
        ('Logs',
         tabbed(
             ('Errors',
              panel('nicos.clients.gui.panels.errors.ErrorPanel')),
             ('Log files',
              panel('nicos.clients.gui.panels.logviewer.LogViewerPanel')),
         ),
         ),


        ('  ', panel('nicos.clients.flowui.panels.empty.EmptyPanel')),

        ('Finish Experiment',
         panel('nicos.clients.flowui.panels.setup_panel.FinishPanel')),

        position='left',
    ),  # tabbed

)  # docked

windows = []

tools = [
    tool('Report NICOS bug or request enhancement',
         'nicos.clients.gui.tools.bugreport.BugreportTool'),
]

options = {
    'facility': 'sinq',
    'mainwindow_class': 'nicos_sinq.gui.mainwindow.MainWindow',
}
