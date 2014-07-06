class CheckInit(type):
    def __new__(mcs, name, bases, classdict):
        original_init = classdict['__init__']

        def init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            assert hasattr(self, self.flag_variable), "Super init not called"

        classdict['__init__'] = init
        return type.__new__(mcs, name, bases, classdict)


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
