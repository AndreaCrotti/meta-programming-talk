class SimpleMeta(type):
    pass


def setq2(v1, v2, e):
    """Call it using

    setq2('a', 'b', '(1 + 2)')
    """
    val = eval(e)
    globals().update({v1: val, v2: val})
