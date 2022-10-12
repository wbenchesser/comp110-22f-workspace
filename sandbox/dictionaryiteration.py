"""Testing interating in a dictionary."""

i: int = 0
ai: int = 0

dictionary: dict[int, int] = {1: 1, 2: 1, 3: 3}

for key in dictionary:
    if dictionary[i] == dictionary[key]:
        print("error")
        i += 1
        

    