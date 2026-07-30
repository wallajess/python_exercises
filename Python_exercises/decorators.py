import time
import functools


def cached(f):
    """Decorator that optimizes fib"""
    cache = {}

    def wrapper(*args, **kwargs):
        if args[0] in cache.keys():
            return cache[args[0]]
        result = f(*args, **kwargs)
        cache[args[0]] = result
        return result
    return wrapper


def timeit(f):
    def wrapper(*args, **kwargs):
        print("--> Start timer")
        t0 = time.time()
        res = f()
        delta = time.time() - t0
        print("--> End timer: %s sec." % delta)
        return res
    return wrapper


@cached
def fib_fast(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fast(n - 1) + fib_fast(n - 2)

def fib_slow(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_slow(n-1) + fib_slow(n-2)


if __name__ == "__main__":
    print(fib_fast(32))


def test_cached():
    for i in range(15):
        assert fib_slow(i) == fib_fast(i)


if __name__ == '__main__':
    for fib in (fib_fast, fib_slow):
        fib = timeit(fib)
        for x in (0, 1, 5, 15, 32):
            y, dt = fib(x)
            print(f"{fib.__name__}({x:2}) = {y:>7} in {dt:<7.2} seconds.")
        print("")
