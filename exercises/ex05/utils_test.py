"""Tests for the utility functions."""

__author__ = "730470219"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_none() -> None:
    """Edge case test for 'only_evens' function."""
    intergers: list[int] = [1, 5, 3]
    assert only_evens(intergers) == []


def test_only_evens_one() -> None:
    """Use case test for 'only_evens' function."""
    intergers: list[int] = [1, 2, 3]
    assert only_evens(intergers) == [2]


def test_only_evens_all() -> None:
    """Use case test for 'only_evens' function."""
    intergers: list[int] = [4, 4, 4]
    assert only_evens(intergers) == [4, 4, 4]


def test_sub_invalid() -> None:
    """Edge case test for 'sub' function."""
    intergers: list[int] = [10, 20, 30, 40]
    assert sub([], 3, 4) == []
    assert sub(intergers, 5, 2) == []
    assert sub(intergers, 2, -1) == []


def test_sub_valid() -> None:
    """Use case test for 'sub' function."""
    intergers: list[int] = [10, 20, 30, 40]
    assert sub(intergers, 1, 3) == [20, 30]


def test_sub_beyond_len() -> None:
    """Use case test for 'sub' function."""
    intergers: list[int] = [10, 20, 30, 40]
    assert sub(intergers, -1, 4) == [10, 20, 30, 40]


def test_concat_empty() -> None:
    """Edge case test for 'concat' function."""
    list1: list[int] = []
    list2: list[int] = [1, 2, 3]
    assert concat(list1, list2) == [1, 2, 3]
    assert concat(list2, list1) == [1, 2, 3]


def test_concat() -> None:
    """Use case test for 'concat' function."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_concat_again() -> None:
    """Use case test for 'concat' function."""
    list1: list[int] = [5, 21, 3]
    list2: list[int] = [49, 1000, 1]
    assert concat(list2, list1) == [49, 1000, 1, 5, 21, 3]