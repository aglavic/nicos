description = "MARIA Argon box monitoring setup"
group = "optional"

tango_base = "tango://phys.maria.frm2:10000/maria/"

devices = dict(
    ArDiff_p1 = device("nicos.devices.entangle.AnalogInput",
        description = "Difference pressure between box and guide hall",
        tangodevice = tango_base + "FZJDP_Analog/ArDiff_p1",
        fmtstr = "%.2f",
        unit = "mbar",
        pollinterval = 5,
        maxage = 6,
    ),
    ArDiff_p2 = device("nicos.devices.entangle.AnalogInput",
        description = "Difference pressure between box and guide hall",
        tangodevice = tango_base + "FZJDP_Analog/ArDiff_p2",
        fmtstr = "%.2f",
        unit = "mbar",
        pollinterval = 5,
        maxage = 6,
    ),
    GuideHall_p = device("nicos.devices.entangle.AnalogInput",
        description = "Pressure in guide hall",
        tangodevice = tango_base + "FZJDP_Analog/GuideHall_p",
        fmtstr = "%.0f",
        unit = "mbar",
        pollinterval = 5,
        maxage = 6,
    ),
    ArO2_fill1 = device("nicos.devices.entangle.AnalogInput",
        description = "O2 level in Ar box",
        tangodevice = tango_base + "FZJDP_Analog/ArO2_fill1",
        fmtstr = "%.2f",
        unit = "%",
        pollinterval = 5,
        maxage = 6,
    ),
    ArO2_fill2 = device("nicos.devices.entangle.AnalogInput",
        description = "O2 level in Ar box",
        tangodevice = tango_base + "FZJDP_Analog/ArO2_fill2",
        fmtstr = "%.2f",
        unit = "%",
        pollinterval = 5,
        maxage = 6,
    ),
    GuideHallO2_fill = device("nicos.devices.entangle.AnalogInput",
        description = "O2 level in guide hall",
        tangodevice = tango_base + "FZJDP_Analog/GuideHallO2_fill",
        fmtstr = "%.2f",
        unit = "%",
        pollinterval = 5,
        maxage = 6,
    ),
    T_ar_air = device("nicos.devices.entangle.AnalogInput",
        description = "Argon box air temperature",
        tangodevice = tango_base + "FZJDP_Analog/TArAir",
        fmtstr = "%.1f",
        unit = "C",
        pollinterval = 5,
        maxage = 6,
    ),
    T_ar_laser = device("nicos.devices.entangle.AnalogInput",
        description = "Argon box laser temperature",
        tangodevice = tango_base + "FZJDP_Analog/TArLaserMagicBox",
        fmtstr = "%.1f",
        unit = "C",
        pollinterval = 5,
        maxage = 6,
    ),
    T_ar_board = device("nicos.devices.entangle.AnalogInput",
        description = "Argon box mu board temperature",
        tangodevice = tango_base + "FZJDP_Analog/TArBoardMagicBox",
        fmtstr = "%.1f",
        unit = "C",
        pollinterval = 5,
        maxage = 6,
    ),
    T_oven = device("nicos.devices.entangle.AnalogInput",
        description = "Oven temperature",
        tangodevice = tango_base + "FZJDP_Analog/TOven",
        fmtstr = "%.1f",
        unit = "C",
        pollinterval = 5,
        maxage = 6,
    ),
)
