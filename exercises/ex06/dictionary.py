"""Dictionary Utility Functions."""

__author__ = "730470219"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and values in a dictionary."""
    result: dict[str, str] = dict()
    for key in dictionary:
        if dictionary[key] in result:
            raise KeyError()
        result[dictionary[key]] = key
    return result


def favorite_color(dictionary: dict[str, str]) -> str:
    """Function that returns the color that appears most frequently in a given dictionary."""
    count: dict[str, int] = dict()
    result: str = ""
    for key in dictionary:
        if result == "":
            result = dictionary[key]
        if not dictionary[key] in count:
            count[dictionary[key]] = 1
        else:
            count[dictionary[key]] += 1
    for key in count:
        if count[key] > count[result]:
            result = key
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Function that counts the number of times that each item in a given list appears."""
    result: dict[str, int] = dict()
    for item in input_list:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result