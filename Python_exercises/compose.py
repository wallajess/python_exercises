from typing import Callable
from functools import reduce


# Aufgabe 11.1
def compose(f: Callable[[int], int], g: Callable[[int, int], int]):
    """Takes a function that takes one argument and one that takes two and returns a function composition."""
    return lambda x, y: f(g(x, y))