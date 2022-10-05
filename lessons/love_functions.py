"""Some tender, loving functions."""

from curses import KEY_RESIZE


def love (subject: str) -> str:
    """Given a subject as a parameter, returns aa loving string."""
    return f"I love you {subject}!"

print(love("queen"))


def spread_love (to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i = i + 1
    return love_note
