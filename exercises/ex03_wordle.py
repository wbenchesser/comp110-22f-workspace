"""EX03_Wordle - A Full Wordle Game."""

__author__ = "730564467"


def contains_char(secret: str, letter: str) -> bool:
    """Tells if a letter is contained within a word."""
    assert len(letter) == 1
    alti: int = 0
    while alti < len(secret):   # If the letters do not match, the program loops checking each letter of the secret word to see if contains the given letter.
        if secret[alti] == letter:   # If the secret word does contain the given letter, the function returns True. 
            return True
        else:
            alti = alti + 1   # The alternate index is increased by one and restarts the while loops, checking all letters of the secret word for matches with the given letter.
    return False   # The function returns False if it does not find the given letter anywhere within the secret word. 


def emojified(guess: str, secret: str) -> str:
    """Given a guess and a secret word, commnad will return emojis representing matching letters."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojis: str = ""   # A string that will have different emojis concatinated within it to form the final emoji string that will be returned, later to be used by main()
    i: int = 0   # Keeps track of which letter of the word is being compared. 
    while i < len(secret):
        if guess[i] == secret[i]:
            emojis += GREEN_BOX
            i += 1
        else:
            if contains_char(secret, guess[i]) is True:   # Uses func defined earlier to see if any letter is contained within the word in the wrong position.
                emojis += YELLOW_BOX
                i += 1
            else:
                emojis += WHITE_BOX
                i += 1
    return emojis   # String of green, yellow, and white emojis is returned, later to be used in main().


def input_guess(exp_len: int) -> str:   # Allows for main() to have proper length inputs and reprompt user if inputs are incorrect length.
    """Given an integer 'expected length of a guess,' will prompt the user for a guess and continue prompting until correct length is given."""
    guess: str = input(f"Enter a {str(exp_len)} character word: ")
    if len(guess) == exp_len:   # If the length of the guess is as expected it is returned as-is.
        return guess
    else:
        while len(guess) != exp_len:
            guess = input(f"That wasn't {str(exp_len)} chars! Try again: ")  # If the length of the guess is not as expected the user is repropted until they insert a correct length response. 
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "chesser"   # Word can be changed and the game will still run properly.
    playing: bool = True   # Allows for the while loop to be manually stopped if player gets correct answer.
    turn: int = 1
    while playing is True and turn < 7:   # While loop can be ended either if player answers correctly or if they run out of turns. 
        print(f"=== Turn {turn}/6 ===")
        emojis: str = emojified(input_guess(len(secret)), secret)   # Takes output of input_guess and puts it into emojified and saves it as variable that can be displayed and compared to.
        if emojis == "\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9":   # If the player guessed correctly they are told they won and the game is stopped.
            print(emojis)
            print(f"You won in {turn}/6 turns!")
            playing is False
            return None
        else:
            print(emojis)
            turn += 1   # At the end of every round the turn is increased by one and the while loop restarts

    print("X/6 - Sorry, try again tomorrow!")   # The player is informed they did not win if it takes them more than 6 tries to find the correct solution.
    return None


if __name__ == "__main__":
    main()
