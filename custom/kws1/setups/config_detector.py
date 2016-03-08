description = 'presets for the detector position'
group = 'configdata'

DETECTOR_PRESETS = {
    '5A': {
        '1.5m':    dict(z=1.5, x=-5.0,  y=9.7),
        '2m':      dict(z=2,   x=-4.5,  y=9.1),
        '4m':      dict(z=4,   x=-3.2,  y=8.0),
        '8m':      dict(z=8,   x=-3.0,  y=7.0),
        '14m':     dict(z=14,  x=-3.0,  y=5.2),
        '20m':     dict(z=20,  x=-4.5,  y=1.0),
        '6m Hum':  dict(z=6,   x=-3.5,  y=8.0),
        '1.5m Tr': dict(z=1.5, x=-25,   y=-40),
        '2m Tr':   dict(z=2,   x=-25,   y=-40),
        '8m Tr':   dict(z=8,   x=-25,   y=-40),
        '20m Tr':  dict(z=20,  x=-25,   y=-40),
    },
    '6A': {
        '1.5m':    dict(z=1.5, x=-5.0,  y=9.7),
        '2m':      dict(z=2,   x=-5.0,  y=9.3),
        '4m':      dict(z=4,   x=-3.5,  y=7.8),
        '8m':      dict(z=8,   x=-3.0,  y=6.7),
        '20m':     dict(z=20,  x=-4.0,  y=-3.0),
        '8m Tr':   dict(z=8,   x=-25,   y=-40),
    },
    '7A': {
        '1.5m':    dict(z=1.5, x=-3.5,  y=9.0),
        '2m':      dict(z=2,   x=-3.5,  y=9.0),
        '4m':      dict(z=4,   x=-2.0,  y=7.3),
        '8m':      dict(z=8,   x=-1.5,  y=6.5),
        '14m':     dict(z=14,  x=-3.3,  y=2.0),
        '20m':     dict(z=20,  x=-2.9,  y=-4.5),
        '8m Tr':   dict(z=8,   x=-25,   y=-40),
        '18.3m C20 Lens': dict(z=18.3, x=-3, y=-7),
    },
    '8A': {
        '8m Tr':   dict(z=8,   x=-25,   y=-40),
    },
    '10A': {
        '1.5m':    dict(z=1.5, x=-4.1,  y=8.1),
        '2m':      dict(z=2,   x=-4.1,  y=8.1),
        '4m':      dict(z=4,   x=-2.7,  y=6.7),
        '8m':      dict(z=8,   x=-1.9,  y=4.5),
        '14m':     dict(z=14,  x=-3.0,  y=-4.0),
        '20m':     dict(z=20,  x=-1.8,  y=-21.5),
        '8m Tr':   dict(z=8,   x=-25,   y=-40),
        '6.4m C20 Lens':  dict(z=6.4,  x=-2.5, y=1.0),
        '10.4m C14 Lens': dict(z=10.4, x=-2.2, y=2.0),
    },
    '12A': {
        '1.5m':    dict(z=1.5, x=-4.0,  y=8.0),
        '2m':      dict(z=2,   x=-4.0,  y=8.0),
        '4m':      dict(z=4,   x=-1.5,  y=6.5),
        '8m':      dict(z=8,   x=-2.7,  y=1.3),
        '20m':     dict(z=20,  x=-3.2,  y=-29.7),
    },
}
