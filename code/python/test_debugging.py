import unittest
from mock import patch

from .debugging import DebugMeta


class DebugObject(metaclass=DebugMeta):
    pass


class TestDebuggingClass(unittest.TestCase):
    # @patch('__builtins__.object', new=DebugObject)
    def test_object_replaced(self):

        class Debugging:
            pass
