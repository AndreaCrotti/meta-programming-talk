import unittest

from . import models, timers, good_practice


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


def to_time2():
    for _ in range(100000):
        pass

    return 42


class TestTime(unittest.TestCase):
    def test_timer_change_signature(self):
        val, time = timers.timeit_change_signature(to_time)()
        self.assertEqual(val, 42)
        self.assertTrue(time.microseconds > 0)

    def test_implementation_1_faster(self):
        val1, time1 = timers.timeit_change_signature(to_time)()
        val2, time2 = timers.timeit_change_signature(to_time2)()
        self.assertEqual(val1, 42)
        self.assertEqual(val2, 42)
        self.assertLess(time1, time2)

    def test_timer_print(self):
        val = timers.timeit_print(to_time)()
        self.assertEqual(val, 42)


class TestForceCallingSuper(unittest.TestCase):
    def test_super_call(self):
        good_practice.SubClassWithSuper()

        with self.assertRaises(AssertionError):
            good_practice.SubClassForgotSuper()
