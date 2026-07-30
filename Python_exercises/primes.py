from math import sqrt


def is_prime(x: int, ps: list) -> bool:
    "Checks whether x is a prime number."
    if x <= 1:
        return False
    for prime in ps:
        if x % prime == 0:
            return False
    return True


def primes(n = int) -> list:
    """Primes takes a whole number as an argument and returns 
    a list of all the prime numbers up to and including n."""
    if n < 2:
        return []
    ps = [2]
    for i in range(3, n + 1):
        if is_prime(i, ps):
            ps += [i]
    return ps

assert primes(1) == []
assert primes(2) == [2]
assert primes(3) == [2, 3]
assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    