"""Utility function example."""

# Function name: contains
# We will have 2 parameters: needle (str), and haystack (str)
# Return type bool
def contains(needle: str, haystack: list[str]):
# Gameplan
# 1. Start w/ 1st index
    i: int = 0
# 2. Loop through every index
    while i < len[haystack]:
        #  2.A If item at index is needle return True
        if haystack[i] == needle:
            return True
        i += 1
        # 3. If not return False
    return False

