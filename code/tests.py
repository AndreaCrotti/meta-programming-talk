import unittest

from . import models, good_practice, decorators


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

    def test_type_checking_on_arguments(self):
        with self.assertRaises(TypeError):
            Simple(y=1)


class TestFields(unittest.TestCase):
    def test_value_overrides_default(self):
        mod = models.Integer(value=0, default=1)
        self.assertEqual(mod, 0)

    def test_setting_wrong_type_field_init_time_fails(self):
        with self.assertRaises(TypeError):
            models.String(value=100)

    def test_changing_field_at_runtime_wrong_type_fields(self):
        sampl = models.String(value="hello")
        with self.assertRaises(TypeError):
            sampl.value = 100


def to_time():
    return 42


def to_time2():
    for _ in range(100000):
        pass

    return 42


class TestTime(unittest.TestCase):
    def test_timer_change_signature(self):
        val, time = decorators.timeit_change_signature(to_time)()
        self.assertEqual(val, 42)
        self.assertTrue(time.microseconds > 0)

    def test_implementation_1_faster(self):
        val1, time1 = decorators.timeit_change_signature(to_time)()
        val2, time2 = decorators.timeit_change_signature(to_time2)()
        self.assertEqual(val1, 42)
        self.assertEqual(val2, 42)
        self.assertLess(time1, time2)

    def test_timer_print(self):
        val = decorators.timeit_print(to_time)()
        self.assertEqual(val, 42)


class TestForceCallingSuper(unittest.TestCase):
    def test_super_call(self):
        good_practice.SubClassWithSuper()

        with self.assertRaises(AssertionError):
            good_practice.SubClassForgotSuper()


class TestForceCallingSuperNoMeta(unittest.TestCase):
    def test_super_call(self):
        class Sub(good_practice.EnforceInitSimple):
            def __init__(self):
                self.var = 42

        with self.assertRaises(Exception):
            Sub().meth()


class TestAddMethod(unittest.TestCase):
    def test_add_method_to_class(self):

        @decorators.add_response
        class Cls:
            pass

        self.assertEqual(Cls().response(), 42)
