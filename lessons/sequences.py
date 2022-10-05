"""Example of the tuple and range sequences."""

# An example of a tuple without type aliasing
goat: tuple[str, str] = ("MJ", 23)

# Typles are sequences so the're 0-indexed
print(goat[0])
print(goat[1])

# Printing a tuple produces its literal syntax
print(goat)

# Sequences have lengths
print(len(goat))

# Sequences are iterable with for...in loops
# Meaning you can loop over them with for...in
for item in goat:
    print(item)

# Tuples are immuntable
# Which means we can't reassign items, or append, nor pop. 
# goat[0] = "LBJ" DNE

# We can invent our own type with a type alias
Player = tuple[str, int]

# Once we alias a type, we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# In a strange wolrd where Jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)



# A range is another common sequence type
zero_to_nine: range = range(0, 10, 1)

print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

# We can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)

names: list[str] = ["a", "b", "c", "d"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")

for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")
    