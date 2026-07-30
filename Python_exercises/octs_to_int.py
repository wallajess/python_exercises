from functools import reduce


# Aufgabe 11.3
def octs_to_int(octal: list) -> int:
    """Coverts an octal number into an integer."""
    return reduce((lambda x, y: x + (y * 8 ** (len(octal) - (octal.index(y)) - 1))), reversed(octal))