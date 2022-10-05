"""An example of for_in syntax."""

names: list[str] = ["Ben", "Raven", "Gwen", "Korra"]

# Example of iterating through names using while loops
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for..in loop is the same as the while loop
for name in names:
    print(name)