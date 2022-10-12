"""EX07 - Dictionary functions."""

__author__ = "730564467"


def invert(d1: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values."""
    result: dict[str, str] = {}
    for key in d1:
        result[d1[key]] = key
    if len(result) < len(d1):
        raise KeyError("Dictionary not inversible, two keys cannot be the same!")
    return result


def favorite_color(d1: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    color: str = ""
    top_color_count: int = 0
    for key in d1:
        color_counter: int = 0
        for i in d1:
            if d1[key] == d1[i]:
                color_counter += 1
        if color_counter > top_color_count:
            top_color_count = color_counter
            color = d1[key] 
    return color


def count(l1: list[str]) -> dict[str, int]:
    """Given a list, returns a dictionary where each list items is associated with its # of appearances in the list."""
    result: dict[str, int] = {}
    for key in l1:
        if key in result:
            temp: int = result[key]
            result[key] = temp + 1
        else:
            result[key] = 1
    return result