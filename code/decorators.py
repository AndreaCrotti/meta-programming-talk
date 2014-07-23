from datetime import datetime
from functools import wraps


def add_response(cls):
    """Add a method called response to the class
    """
    cls.response = lambda self: 42
    return cls


def timeit_change_signature(func):
    """Change the signature of the decorated function
    returning the time of execution as first element in the
    return tuple
    """
    @wraps(func)
    def _timeit_change_signature(*args, **kwargs):
        before = datetime.utcnow()
        ret = func(*args, **kwargs)
        after = datetime.utcnow()
        return ret, after - before

    return _timeit_change_signature


def timeit_print(func):
    """Print out the execution time of the decorated function
    """
    @wraps(func)
    def _timeit_print(*args, **kwargs):
        before = datetime.utcnow()
        ret = func(*args, **kwargs)
        after = datetime.utcnow()
        print("{} took {} seconds to run".format(func, after - before))
        return ret

    return _timeit_print
