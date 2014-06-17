from datetime import datetime


def timeit(func):
    def _timeit(*args, **kwargs):
        before = datetime.utcnow()
        ret = func(*args, **kwargs)
        after = datetime.utcnow()
        return ret, after - before

    return _timeit


def long_function():
    for _ in range(10000):
        pass


if __name__ == '__main__':
    ln, time = timeit(long_function)()
    assert ln is None
    assert time.microseconds > 0
