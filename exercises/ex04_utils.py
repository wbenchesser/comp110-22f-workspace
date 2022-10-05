"""List Utility Functions."""


__author__ = 730564467


def all(numlist: list[int], num: int) -> bool:
    """Given a list of ints and a single int, function will return True if all parts of list ar equal to single given int."""
    if len(numlist) == 0:
        return False
    i: int = 0
    while i < len(numlist):
        if numlist[i] != num:
            return False
        else:
            i += 1
    return True


def max(intlist: list[int]) -> int:
    """Given a list of ints, max will return largest int."""
    if len(intlist) == 0:
        raise ValueError("max() arg is an empty list")
    max: int = intlist[0]
    i: int = 0
    while i < len(intlist):
        if intlist[i] > max:
            max = intlist[i]
        i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists, if all values of both lists are equal, return True. If not, return False."""
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True