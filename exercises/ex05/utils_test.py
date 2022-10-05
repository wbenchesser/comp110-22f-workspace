"""EX05 - Tests for List Utitlity Functions Continued."""


__author__ = "730564467"


from exercises.ex05.utils import only_evens, concat, sub


# only_evens tests

# Edge case: if no list is input, function should return an empty list.
def test_only_evens_listempty() -> None:
    """If no list is input, function should return an empty list."""
    l1: list(int) = []
    assert only_evens(l1) == []


# Use case: given a list containing [1, 2, 3], function should return a list composed of just [2].
def test_only_evens_usecase1() -> None:
    """Given a list containing [1, 2, 3], function should return a list composed of just [2]."""
    l1: list(int) = [1, 2, 3]
    assert only_evens(l1) == [2]


# Use case: given a list containing [2, 2, 2, 3], function should return a list composed of [2, 2, 2].
def test_only_evens_usecase2() -> None:
    """Given a list containing [2, 2, 2, 3], function should return a list composed of [2, 2, 2]."""
    l1: list(int) = [2, 2, 2, 3]
    assert only_evens(l1) == [2, 2, 2]


# concat tests

# Edge case: given that the function is given two empty lists, it should return an empty list. 
def test_concat_emptylists() -> None:
    """Given that the function is given two empty lists, it should return an empty list."""
    l1: list(int) = []
    l2: list(int) = []
    assert concat(l1, l2) == []


# Use case: given a list [1] and a list [3], function should return a new list [1, 3].
def test_concat_use1() -> None:
    """Given a list [1] and a list [3], function should return a new list [1, 3]."""
    l1: list(int) = [1]
    l2: list(int) = [3]
    assert concat(l1, l2) == [1, 3]


# Use case: given a list [1, 2] and a list [3, 4], function should return a new list [1, 2, 3, 4].
def test_concat_use2() -> None:
    """Given a list [1, 2] and a list [3, 4], function should return a new list [1, 2, 3, 4]."""
    l1: list(int) = [1, 2]
    l2: list(int) = [3, 4]
    assert concat(l1, l2) == [1, 2, 3, 4]


# sub tests

# Edge case: given that the function is given a stop int less than the length of l1, the function will return an empty list.
def test_sub_stop_before_len_l1() -> None:
    """Given that the function is given a stop int less than the length of l1, the function will return an empty list."""
    l1: list(int) = [1, 2, 3]
    start: int = 0
    stop: int = -5
    assert sub(l1, start, stop) == []


# Use case: given that the function is given a list [1, 2, 3, 4], a start 1, and a stop 3, the function will return a list [2, 3].
def test_sub_use1() -> None:
    """Given that the function is given a list [1, 2, 3, 4], a start 1, and a stop 3, the function will return a list [2, 3]."""
    l1: list(int) = [1, 2, 3, 4]
    start: int = 1
    stop: int = 3
    assert sub(l1, start, stop) == [2, 3]


# Use case: given that the function is given a list [-1, 10, 4, 200], a start 1, and a stop 4, the function will return a list [10, 4, 200]
def test_sub_use2() -> None:
    """Given that the function is given a list [-1, 10, 4, 200], a start 1, and a stop 4, the function will return a list [10, 4, 200]."""
    l1: list(int) = [-1, 10, 4, 200]
    start: int = 1
    stop: int = 4
    assert sub(l1, start, stop) == [10, 4, 200]