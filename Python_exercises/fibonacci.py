import time


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def timeit(f):
    print("--> Start timer")
    t0 = time.time()
    res = f()
    delta = time.time() - t0
    print("--> End timer: %s sec." % delta)
    return res


print(timeit(fib(32)))