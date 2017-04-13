description = 'preset values for the sample position'
group = 'configdata'

open_pos_mir_ap2  = (50, 50)
open_pos_sam10_ap = (0, 0, 50, 50)
open_pos_sam01_ap = (0, 0, 30, 30)

dock_pos_sam10_x = 0
dock_pos_sam10_y = 0

dock_pos_sam01_x = 0
dock_pos_sam01_y = 0

SAMPLE_POS_PRESETS = {
    # TODO: add proper presets
    '10m': dict(
        active_ap = 'mir_ap2',
        active_x = 'sam10_x',
        active_y = 'sam10_y',

        sam10_ap = open_pos_sam10_ap,
        sam01_ap = open_pos_sam01_ap,
        sam01_x = dock_pos_sam01_x,
        sam01_y = dock_pos_sam01_y,
    ),
    '9.5m': dict(
        active_ap = 'sam10_ap',
        active_x = 'sam10_x',
        active_y = 'sam10_y',

        mir_ap2 = open_pos_mir_ap2,
        sam01_ap = open_pos_sam01_ap,
        sam01_x = dock_pos_sam01_x,
        sam01_y = dock_pos_sam01_y,
    ),
    '1.3m': dict(
        active_ap = 'sam01_ap',
        active_x = 'sam01_x',
        active_y = 'sam01_y',

        mir_ap2 = open_pos_mir_ap2,
        sam10_ap = open_pos_sam10_ap,
        sam10_x = dock_pos_sam10_x,
        sam10_y = dock_pos_sam10_y,
    ),
    '0.15m': dict(
        active_ap = 'sel_ap2',
        active_x = 'sam01_x',
        active_y = 'sam01_y',

        mir_ap2 = open_pos_mir_ap2,
        sam01_ap = open_pos_sam01_ap,
        sam10_ap = open_pos_sam10_ap,
        sam10_x = dock_pos_sam10_x,
        sam10_y = dock_pos_sam10_y,
    )
}
