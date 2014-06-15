"""
Implement a very simple Django-like Model with meta classes
"""


class MetaModel(type):
    def __new__(mcl, name, bases, classdict):
        # TODO: replace the __init__ of the class that we are changing
        # with an init that takes arguments in a more flexible way
        keywords = {}
        for attr, val in classdict.items():
            if isinstance(val, Field):
                keywords[attr] = val

        def new_init(self, **kwargs):
            assert set(kwargs).issubset(set(keywords)), "Wrong arguments %s" % str(kwargs)
            for key, val in kwargs.items():
                new_val = keywords[key].__class__(value=val)
                setattr(self, key, new_val)

        classdict['__init__'] = new_init
        return type.__new__(mcl, name, bases, classdict)


class Field:
    def __init__(self, value=None, default=None):
        self.value = value if value is not None else default

    def __eq__(self, other):
        return self.value == other


class Integer(Field):
    pass


class String(Field):
    pass


class Model(object, metaclass=MetaModel):
    pass
