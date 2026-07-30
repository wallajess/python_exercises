import math

def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        x = math.floor(math.sqrt(n)) + 1
        i = 3
        while i < x:
            if n % i == 0:
                return False
            i += 2
            return True

print(is_prime(25))