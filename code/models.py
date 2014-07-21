"""
Implement a very simple Django-like Model with meta classes
"""


class MetaModel(type):
    def __new__(mcl, name, bases, classdict):
        keywords = {}
        for attr, val in classdict.items():
            if isinstance(val, Field):
                keywords[attr] = val

        def init(self, **kwargs):
            unknown = set(kwargs) - set(keywords)
            if len(unknown) > 0:
                raise Exception("Unknown arguments %s" % str(unknown))

            for key, val in kwargs.items():
                new_val = keywords[key].__class__(value=val)
                setattr(self, key, new_val)

        classdict['__init__'] = init
        return super().__new__(mcl, name, bases, classdict)


class Field:
    BASE_TYPE = None

    def __init__(self, value=None, default=None):
        self.value = value if value is not None else default

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self._check_type()

    def _check_type(self):
        if self.value and not isinstance(self.value, self.BASE_TYPE):
            raise TypeError

    def __eq__(self, other):
        return self.value == other


class Integer(Field):
    BASE_TYPE = int


class String(Field):
    BASE_TYPE = str


class Model(object, metaclass=MetaModel):
    pass


class ModelNoMeta(object):
    def __init__(self, x=1, y=""):
        self.x = x
        # TODO: add a type check that you are passing the right thing!
        self.y = y
