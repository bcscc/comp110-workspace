"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730470219"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Copys the rows of a csv into a dict 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(row_table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in row_table:
        result.append(row[column])
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], n_items: int) -> dict[str, list[str]]:
    """Creates a new table with the first n number of rows."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        if n_items > len(column_table):
            n_items = len(column_table)
        row_items: list[str] = []
        for i in range(0, n_items):
            row_items.append(column_table[column][i])
            i += 1
        result[column] = row_items
    return result


def select(column_table: dict[str, list[str]], selected_columns: list[str]) -> dict[str, list[str]]:
    """Creates a new table that contains only certain selected columns."""
    result: dict[str, list[str]] = {}
    for column in selected_columns:
        result[column] = column_table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables into one."""
    result: dict[str, list[str]] = {}
    for i in table1:
        result[i] = table1[i]
    for j in table2:
        if j in result:
            for k in table2[j]:
                result[j].append(k)
        else:
            result[j] = table2[j]
    return result


def sort(dictionary: dict[str, int]) -> dict[str, int]:
    """Sorts a dictionary's keys by numerical order."""
    result: dict[str, int] = {}
    sorted_keys: list[str] = sorted(dictionary)
    for i in sorted_keys:
        result[i] = dictionary[i]
    return result


def count(strs: list[str]) -> dict[str, int]:
    """Counts the number of each unique str in a list."""
    count: dict[str, int] = {}
    for i in strs:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return sort(count)