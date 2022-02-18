"""List Utility Function."""

__author__ = "730470219"


def only_evens(intergers: list[int]) -> list[int]:
    """Function that returns only even intergers within a given list."""
    result: list[int] = list()
    for item in intergers:
        if item % 2 == 0:
            result.append(item)
    return result


def sub(intergers: list[int], start_index: int, end_index: int) -> list[int]:
    """Function that returns the items between two indices within a given list."""
    result: list[int] = list()
    if start_index < 0:
        start_index = 0
    if end_index > len(intergers) - 1:
        end_index = len(intergers)
    if intergers == 0 or start_index > len(intergers) or end_index <= 0:
        return result
    while start_index < end_index:
        result.append(intergers[start_index])
        start_index += 1
    return result


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Function that combinds two lists."""
    result: list[int] = list()
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result