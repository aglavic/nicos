
"""NICOS GUI LoKI configuration."""

main_window = docked(
    tabbed(
        (
            'Experiment',
            vsplit(panel('nicos_ess.gui.panels.exp_panel.ExpPanel',
                         hide_sample=True),
                   ),  # vsplit
        ),
        (
            'Setup',
            vsplit(
                (panel('nicos.clients.flowui.panels.setup_panel.SetupsPanel'))
            ),  # vsplit
        ),
        (
            'Samples',
            vsplit(panel('nicos_ess.loki.gui.legacy.sampleconf.LokiSamplePanel',
            holder_info = [
                ('Al 2-level',   (9,  2, 'sam_trans_x', 26.6,   'sam_trans_y', 105.05)),
                ('Al 3-level',   (9,  3, 'sam_trans_x', 27,     'sam_trans_y', 75)),
            ])),  # vsplit
        ),
        (
            'Experiment Configuration',
            vsplit(
                (panel('nicos_ess.loki.gui.experiment_conf.LokiExperimentPanel'))
            ),  # vsplit
        ),
        ('  ', panel('nicos.clients.flowui.panels.empty.EmptyPanel')),
        (
            'Instrument interaction',
            hsplit(
                vbox(
                    tabbed(
                        (
                            'Output',
                            panel(
                                'nicos.clients.flowui.panels.console.ConsolePanel',
                                hasinput=False,
                            ),
                        ),
                        ('Scan Plot', panel('nicos.clients.flowui.panels.scans.ScansPanel')),
                        (
                            'Detector Image',
                            panel('nicos.clients.flowui.panels.live.LiveDataPanel'),
                        ),
                        (
                            'Script Status',
                            panel(
                                'nicos.clients.flowui.panels.status.ScriptStatusPanel',
                                eta=True,
                            ),
                        ),
                    ),
                    panel(
                        'nicos.clients.flowui.panels.cmdbuilder.CommandPanel',
                        modules=['nicos.clients.gui.cmdlets'],
                    ),
                ),  # vsplit
                panel(
                    'nicos.clients.flowui.panels.devices.DevicesPanel',
                    dockpos='right',
                    param_display={'tas': 'scanmode', 'Exp': ['lastpoint', 'lastscan']},
                    filters=[('Detector', 'det'), ('Temperatures', '^T'),],
                ),
            ),  # hsplit
        ),
        (
            'Script Editor',
            vsplit(
                panel(
                    'nicos_ess.loki.gui.scriptbuilder.CommandsPanel',
                    modules=['nicos_ess.loki.gui.cmdlets'],
                ),
                panel('nicos.clients.flowui.panels.editor.EditorPanel', tools=None),
            ),
        ),
        ('Prototype', panel('nicos_ess.loki.gui.loki_scriptbuilder.LokiScriptBuilderPanel')),
        ('Detector Image', panel('nicos.clients.flowui.panels.live.LiveDataPanel')),
        ('History', panel('nicos.clients.flowui.panels.history.HistoryPanel'),),
        (
            'Logs',
            tabbed(
                ('Errors', panel('nicos.clients.gui.panels.errors.ErrorPanel')),
                (
                    'Log files',
                    panel('nicos.clients.gui.panels.logviewer.LogViewerPanel'),
                ),
            ),
        ),
        ('  ', panel('nicos.clients.flowui.panels.empty.EmptyPanel')),
        ('Finish Experiment', panel('nicos.clients.flowui.panels.setup_panel.FinishPanel')),
        position='left',
    ),  # tabbed
)  # docked

windows = []

tools = [
    tool(
        'Report NICOS bug or request enhancement',
        'nicos.clients.gui.tools.bugreport.BugreportTool',
    ),
]

options = {
    'ess_gui': True,
}
