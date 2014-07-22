"""

This use case comes from the implementation of threading, where
the way the init check is done is by checking in every method or
property for __initialized, which is not very nice to maintain

"""


class CheckInit(type):
    def __new__(mcs, name, bases, classdict):
        original_init = classdict['__init__']

        def init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            assert hasattr(self, self.flag_variable), "super not called"

        classdict['__init__'] = init
        return super().__new__(mcs, name, bases, classdict)


class Base(metaclass=CheckInit):
    flag_variable = 'var'

    def __init__(self):
        self.var = 42


class SubClassWithSuper(Base):
    def __init__(self):
        super().__init__()
        self.subvar = 100


class SubClassForgotSuper(Base):
    def __init__(self):
        self.subvar = 100


class EnforceInitSimple:
    _initialed = False

    def __init__(self):
        self._initialed = True

    def meth(self):
        if not self._initialed:
            raise Exception("Forgot to call __init__")
