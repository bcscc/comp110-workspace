"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730470219"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an empty Linked List should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(Node(10, Node(20, Node(30, None))), 3)


def test_value_at_non_empty() -> None:
    """Value_at of a non-empty list should return its data value at the given index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_max_empty() -> None:
    """Max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Max of a non-empty list should return its maximum data value."""
    linked_list = Node(30, Node(20, Node(10, None)))
    assert max(linked_list) == 30


def test_linkify_single() -> None:
    """Linkify of a single int list should return a one-tier Node object."""
    items: list[int] = [1]
    assert str(linkify(items)) == "1 -> None"

    
def test_linkify_mutiply() -> None:
    """Linkify of a muti int list should return a multi-tier Node object."""
    items: list[int] = [1, 2, 3]
    assert str(linkify(items)) == "1 -> 2 -> 3 -> None"


def test_scale_empty() -> None:
    """Scale of an empty Linked List should return None."""
    assert scale(None) is None


def test_scale_non_empty() -> None:
    """Scale of a non-empty list should return a new linked list of with data values scaled by the given factor."""
    assert str(scale(linkify([1, 2, 3]), 2)) == "2 -> 4 -> 6 -> None"