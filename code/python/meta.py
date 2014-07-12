class SimpleMeta(type):
    pass


def setq2(v1, v2, e):
    val = eval(e)
    globals().update({v1: val, v2: val})
