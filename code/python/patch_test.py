# TODO: this can be put together with the other example

from unittest import TestCase


class TestMeta(type(TestCase)):
    def __new__(mcls, name, bases, dct):
        to_patch = []

        for methname, meth in dct.items():
            if methname.startswith('test') and callable(meth):
                to_patch.append(methname)

        cls = type.__new__(mcls, name, bases, dct)
        for methname in to_patch:
            meth = getattr(cls, methname)
            meth = cls.patch_method(meth)
            setattr(cls, methname, meth)

        return cls


class PatchedTestCase(TestCase):
    __metaclass__ = TestMeta

    @classmethod
    def patch_method(cls, meth):
        pass
