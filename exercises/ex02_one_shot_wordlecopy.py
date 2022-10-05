"""EX02 - One Shot Wordle"""

__author__ = "730564467"

index: int = 0
emojis: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9" 
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"
guess: str = input(f"What is your { len(secret) } letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not { len(secret) } letters! Try again: ")

while index < len(secret):
    if secret[index] == guess[index]:
        emojis = emojis + GREEN_BOX
        index = index + 1
    else:
        elsewhere: bool = False
        alti: int = 0
        while elsewhere == False and alti < len(secret):





        emojis = emojis + WHITE_BOX
        index = index + 1

print(str(emojis))

if secret == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")



