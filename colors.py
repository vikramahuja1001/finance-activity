CREDIT_COLOR = '#009900'

DEBIT_COLOR = '#ff4040'

CATEGORY_COLORS = [
    (1.0, 1.0, 1.0),
    (1.0, 1.0, 0.6),
    (1.0, 1.0, 0.8),
    (1.0, 0.6, 1.0),
    (1.0, 0.6, 0.6),
    (1.0, 0.6, 0.8),
    (1.0, 0.8, 1.0),
    (1.0, 0.8, 0.6),
    (1.0, 0.8, 0.8),
    (0.6, 1.0, 1.0),
    (0.6, 1.0, 0.6),
    (0.6, 1.0, 0.8),
    (0.6, 0.6, 1.0),
    (0.6, 0.6, 0.6),
    (0.6, 0.6, 0.8),
    (0.6, 0.8, 1.0),
    (0.6, 0.8, 0.6),
    (0.6, 0.8, 0.8),
    (0.8, 1.0, 1.0),
    (0.8, 1.0, 0.6),
    (0.8, 1.0, 0.8),
    (0.8, 0.6, 1.0),
    (0.8, 0.6, 0.6),
    (0.8, 0.6, 0.8),
    (0.8, 0.8, 1.0),
    (0.8, 0.8, 0.6),
    (0.8, 0.8, 0.8),
]


def get_category_color(catname):
    return CATEGORY_COLORS[catname.__hash__() % len(CATEGORY_COLORS)]


def get_category_color_str(catname):
    color = get_category_color(catname)
    return "#%02x%02x%02x" % \
        (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
