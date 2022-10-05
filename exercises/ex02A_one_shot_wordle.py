"""EX02 - One Shot Wordle"""

__author__ = "730564467"

from platform import python_branch


secret: str = "python"
guess: str = input(f"What is your { len(secret) }-letter guess? ")

while len(secret) != len(guess):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

if secret == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
