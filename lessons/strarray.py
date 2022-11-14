"""An example of vectorized operations via operator overloading."""

from __future__ import annotations
from typing import Union

class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:  # repr should be returning valid python code.
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for item in self.items:
                item += rhs
                result.items.append(item)
        else:
            assert len(self.items) == len(rhs.items)
            i: int = 0
            while i < len(self.items):
                result.items.append(self.items[i] + rhs.items[i])
                i += 1
        return result

a: StrArray = StrArray(["A", "B", "C"])
b: StrArray = StrArray(["1", "2", "3"])
print(a)
print(a + "!")
print(a + b)
