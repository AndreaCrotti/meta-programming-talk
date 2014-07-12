# TODO: run tests in parallel


def add_response(cls):
    cls.response = lambda self: 42
    return cls

