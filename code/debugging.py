"""
Use a debug class
"""


class DebugMeta(type):
    def __new__(mcs, name, bases, dict):
        return type.__new__(mcs, name, bases, dict)

