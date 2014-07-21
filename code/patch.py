"""
Suppose we never want to have listdir to do something specific
"""

# TODO: this can be put together with the other example

from mock import patch
from unittest import TestCase


class TestMeta(type):
    def __new__(mcls, name, bases, dct):
        to_patch = []

        for attrname, attr in dct.items():
            if attrname.startswith('test') and callable(attr):
                to_patch.append(attrname)

        cls = type.__new__(mcls, name, bases, dct)
        for methname in to_patch:
            meth = getattr(cls, methname)
            meth = cls.patch_method(meth)
            setattr(cls, methname, meth)

        return cls


class PatchedTestCase(TestCase=TestMeta):
    @classmethod
    def patch_method(cls, meth):
        pass
