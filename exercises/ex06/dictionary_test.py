"""Tests for the dictionary utility functions."""

__author__ = "730470219"

import pytest
from dictionary import count, favorite_color, invert


def test_invert_empty() -> None:
    """Edge case test for 'invert' function."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_invert_one() -> None:
    """Use case test for 'invert' function."""
    dictionary: dict[str, str] = {'apple': 'cat'}
    assert invert(dictionary) == {'cat': 'apple'}


def test_invert_mutiple() -> None:
    """Use case test for 'invert' function."""
    dictionary: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_error() -> None:
    """Keyerror test for 'invert' function."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color_same() -> None:
    """Edge case test for 'favorite_color' function."""
    dictionary: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "green"}
    assert favorite_color(dictionary) == "yellow"


def test_favorite_color() -> None:
    """Use case test for 'favorite_color' function."""
    dictionary: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(dictionary) == "blue"


def test_favorite_color_again() -> None:
    """Use case test for 'favorite_color' function."""
    dictionary: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "yellow", "Bob": "greem", "Matt": "yellow", "Dan": "blue"}
    assert favorite_color(dictionary) == "yellow"


def test_count_empty() -> None:
    """Edge case test for 'count' function."""
    input_list: list[str] = []
    assert count(input_list) == {}


def test_count_single() -> None:
    """Use case test for 'count' function."""
    input_list: list[str] = ["a", "a", "a"]
    assert count(input_list) == {"a": 3}


def test_count_mutiple() -> None:
    """Use case test for 'count' function."""
    input_list: list[str] = ["a", "a", "a", "b", "b", "c"]
    assert count(input_list) == {"a": 3, "b": 2, "c": 1}