"""EX05 - List Utitlity Functions Continued."""

__author__ = "730564467"


def only_evens(l1: list[int]) -> list[int]:
    """Given a list of ints, only_evens will return a list of only the even values."""
    i: int = 0
    newlist: list[int] = []
    while i < len(l1):
        if l1[i] % 2 == 0:
            newlist.append(l1[i])
            i += 1
        else:
            i += 1
    return newlist


def concat(l1: list[int], l2: list[int]) -> list[int]:
    """Given two lists of ints, concat will return a list of all values of list 1 followed by all values of list 2."""
    i: int = 0
    newlist: list[int] = []
    while i < len(l1):
        newlist.append(l1[i])
        i += 1

    i: int = 0
    while i < len(l2):
        newlist.append(l2[i])
        i += 1
    
    return newlist


def sub(l1: list[int], start: int, stop: int) -> list[int]:
    """Given a list of ints and two ints, sub will make a new list using the two ints as index start and stop values."""
    newlist: list[int] = []
    if (len(l1) == 0) or (start > len(l1)) or (stop <= 0):
        return []

    if start < 0:
        start = 0
    
    if stop > len(l1):
        stop = len(l1)
    
    while start < stop:
        newlist.append(l1[start])
        start += 1
    
    return newlist

    