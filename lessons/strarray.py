"""An example of vectorized operations via operator overloading."""

from __future__ import annotations
from typing import Union

class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:  # repr should be returning valid python code.
        return f"StrArray({self.items})"

    def __add__(self, rhs: str) -> StrArray:
        result: StrArray = StrArray([])
        for item in self.items:
            item += rhs
            result.items.append(item)
        return result

a: StrArray = StrArray(["A", "B", "C"])
b: StrArray = StrArray(["1", "2", "3"])
print(a)
print(a + "!")
