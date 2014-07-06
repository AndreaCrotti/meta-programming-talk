"""
Implement a very simple Django-like Model with meta classes
"""


class MetaModel(type):
    def __new__(mcl, name, bases, classdict):
        keywords = {}
        for attr, val in classdict.items():
            if isinstance(val, Field):
                keywords[attr] = val

        def new_init(self, **kwargs):
            unknown = set(kwargs) - set(keywords)
            if len(unknown) > 0:
                raise Exception("Unknown arguments %s" % str(unknown))

            for key, val in kwargs.items():
                new_val = keywords[key].__class__(value=val)
                setattr(self, key, new_val)

        classdict['__init__'] = new_init
        return super().__new__(mcl, name, bases, classdict)


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


class ModelNoMeta(object):
    def __init__(self, x=1, y=""):
        self.x = x
        # TODO: add a type check that you are passing the right thing!
        self.y = y
