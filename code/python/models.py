"""
Implement a very simple Django-like Model with meta classes
"""


class MetaModel(type):
    def __new__(mcl, name, bases, nmspc):
        # TODO: replace the __init__ of the class that we are changing
        # with an init that takes arguments in a more flexible way
        return type(name, bases, nmspc)


class Integer:
    def __init__(self, default=0):
        self.default = default


class String:
    pass


class Model(object, metaclass=MetaModel):
    pass
