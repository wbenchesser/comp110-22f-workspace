"""Unit tests for EX07 - Dictionary functions."""

__author__ = "730564467"

import pytest
from exercises.ex07.dictionary import invert, favorite_color, count


# Tests for invert


def test_invert_key_error() -> None:
    """Tests if invert raises a KeyError when at least two d1 values are the same."""
    with pytest.raises(KeyError):
        test_dict = {'1': '2', '3': '2'}
        invert(test_dict)


def test_invert_use_1() -> None:
    """Invert function use case test #1."""
    test_list: dict[str, str] = {"1": "2"}
    assert invert(test_list) == {"2": "1"}


def test_invert_use_2() -> None:
    """Invert function use case test #2."""
    test_list: dict[str, str] = {"1": "2", "2": "3", "3": "4"}
    assert invert(test_list) == {"2": "1", "3": "2", "4": "3"}


# Tests for favorite_color


def test_favorite_color_edge() -> None:
    """Favorite_color edge case test -> tie."""
    test_dict: dict[str, str] = {"Ben": "red", "Alex": "blue"}
    assert favorite_color(test_dict) == "red"


def test_favorite_color_use_1() -> None:
    """Favorite_color use case test #1."""
    test_dict: dict[str, str] = {"Ben": "red", "Alex": "red"}
    assert favorite_color(test_dict) == "red"


def test_favorite_color_use_2() -> None:
    """Favorite_color use case test #2."""
    test_dict: dict[str, str] = {"Ben": "yellow", "Alex": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "blue"


# Tests for count


def test_count_edge() -> None:
    """Count edge case test."""
    list1: list[str] = []
    assert count(list1) == {}


def test_count_use_1() -> None:
    """Count use case test #1."""
    list1: list[str] = ["1", "2"]
    assert count(list1) == {"1": 1, "2": 1}


def test_count_use_2() -> None:
    """Count use case test #2."""
    list1: list[str] = ["1", "2", "3", "3"]
    assert count(list1) == {'1': 1, '2': 1, '3': 2}