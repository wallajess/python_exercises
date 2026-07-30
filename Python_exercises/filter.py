# Aufabe 11.2

# a)
def my_filter(xs: set, ys: set) -> set:
    """Takes two sets as arguments and returns a new set that contains elements that were only in  the first set"""
    return xs - ys


# b)
def my_diff(xs: set, ys: set) -> set:
    """Returns the elements that are in both sets once only."""
    return (xs - ys) | (ys - xs)