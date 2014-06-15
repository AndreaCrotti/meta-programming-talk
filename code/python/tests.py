import unittest

from . import models


class Simple(models.Model):
    x = models.Integer(0)
    y = models.String()



class TestModels(unittest.TestCase):
    def test_model_attribute_create_fields(self):
        s = Simple(y="Hello world")
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, "Hello world")
