import unittest

from . import models, timers


class Simple(models.Model):
    x = models.Integer(0)
    y = models.String()


class TestModels(unittest.TestCase):
    def test_model_attribute_create_fields(self):
        s = Simple(y="Hello world")
        # TODO: have a look at setter and getter to make it even smarter
        self.assertEqual(s.y, "Hello world")
        self.assertEqual(s.x, 0)

    def test_unknown_arguments_fail(self):
        with self.assertRaises(Exception):
            Simple(unknown='hello')


class TestFields(unittest.TestCase):
    def test_value_overrides_default(self):
        mod = models.Integer(value=0, default=1)
        self.assertEqual(mod, 0)



def to_time():
    return 42


class TestTime(unittest.TestCase):
    def test_timer_change_signature(self):
        val, time = timers.timeit_change_signature(to_time)()
        self.assertEqual(val, 42)
        self.assertTrue(time.microseconds > 0)

    def test_timer_print(self):
        val = timers.timeit_print(to_time)()
        self.assertEqual(val, 42)
