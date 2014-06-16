import unittest

from . import models


class Simple(models.Model):
    x = models.Integer(0)
    y = models.String()


class TestModels(unittest.TestCase):
    def test_model_attribute_create_fields(self):
        s = Simple(y="Hello world")
        self.assertEqual(s.y, "Hello world")
        self.assertEqual(s.x, 0)

    def test_unknown_arguments_fail(self):
        with self.assertRaises(Exception):
            Simple(unknown='hello')


class TestFields(unittest.TestCase):
    def test_value_overrides_default(self):
        mod = models.Integer(value=0, default=1)
        self.assertEqual(mod, 0)
