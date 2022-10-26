"""Dictionary related utility functions."""

__author__ = "730564467"

from csv import DictReader

# Define your functions below


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Reads the csv by rows."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(path, "r", encoding="utf8")

    # Prepare to read the data file as a csv line-by-line
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resource
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], col: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[col]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(d1: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if n > len(d1):
        n = len(d1)
    for key in d1:
        temp: list[str] = []
        i: int = 0
        while i < n:
            temp.append(d1[key][i])
            i += 1
        result[key] = temp

    return result


def select(d1: dict[str, list[str]], l1: list[str]) -> dict[str, list[str]]:
    """Produce a nre column based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in l1:
        result[item] = d1[item]
    return result


def concat(d1: dict[str, list[str]], d2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for col in d1:
        result[col] = d1[col]
        for col2 in d2:
            if col2 in d1:
                result[col2] = d1[col2] + d2[col2]
            else:
                result[col2] = d2[col2]
    return result


def count(vals: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in vals:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
