from math import isclose

def reverse(lst : list) -> list:
    """ This function takes a list as an argument and returns the list in the reverse order."""
    rev = []
    i = len(lst)
    for x in lst:
        rev += [lst[i - 1]]
        i -= 1
    return rev

def reverse2(lst : list) -> list:
    """ This function takes a list as an argument and returns the list in the reverse order."""
    range(lst, 1)
    rev = []
    i = len(lst) - 1
    for x in lst:
        rev += [lst[i]]
        i -= 1
    return rev



def reverse3(lst : list) -> list:
    """ This function takes a list as an argument and returns the list in the reverse order."""
    rev = []
    for i in range(len(lst), 0, -1):
        rev += [lst[i - 1]]
    return rev

if __name__ == "__main__":        
    assert reverse([]) == []
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def only_positive(nums : list[int]) -> list:
    """This function takes a list of whole numbers as an arugment and returns a list of positive numbers, i.e. > 0."""
    positives = []
    for x in nums:
        if x > 0:
            positives += [x]
    return positives


if __name__ == "__main__":
    assert only_positive([]) == []
    assert only_positive([1, 2, 3]) == [1, 2, 3]
    assert only_positive([-8, 1, -5, -9, 2, -7, 3, -6, 0]) == [1, 2, 3]


def average(commas : list[float]) -> float:
    """This function takes a list of floats as an argument and returns the average of the numbers."""
    avg = 0
    div = len(commas)
    if div == 0:
        return 0.0
    for x in commas:
        avg += x
    return avg / div
    

if __name__ == "__main__":
    eps = 1e-4
    assert isclose(average([]), 0.0, abs_tol=eps, rel_tol=eps)
    assert isclose(average([1.0]), 1.0, rel_tol=eps)
    assert isclose(average([5.0, 10.0, 15.0, 20.0]), 12.5, rel_tol=eps)