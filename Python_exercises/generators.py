from typing import Iterator, Callable


# def differentiate(f: Callable[[float], float],
#                  h: float) -> Callable[[float], float]:
#    return lambda x0: (f(x0 + h) - f(x0 - h)) / (2 * h)


# def newton(f: Callable[[float], float], x: int) -> float:
#    """Uses the Newton Method to approximate zeros??"""
#    pass


# Aufgabe 12.1 c)
def arithmetic_mean(iterable: Iterator[int]) -> Iterator[int]:
    """Returns the arithmetic mean of the numbers in the iterable."""
    for x in iterable:
        for y in iterable:
            yield (x + y) // 2


# Aufgabe d)

def map13(iterable: Iterator[int]) -> Iterator[int]:
    """Returns the modulo 13 for each number in the iterable."""
    return map((lambda x: x % 13), iterable)


# Aufgabe e)

def filter57(iterable: Iterator[int]) -> Iterator[int]:
    """Returns the values in the iterable that are divisable by 5 or 7"""
    return filter(lambda x: (x % 5 == 0 or x % 7 == 0), iterable)


if __name__ == "__main__":
    print(list(arithmetic_mean(iter(range(0, 21, 4)))))
    input_iterator = iter(range(0, 26, 5))
    assert list(map13(input_iterator)) == [0, 5, 10, 2, 7, 12]
    input_iterator = iter(range(20))
    assert list(filter57(input_iterator)) == [0, 5, 7, 10, 14, 15]