"""EX02 - One Shot Wordle."""

__author__ = "730564467"

index: int = 0   # An index is created to keep track of what letter is being checked for correctness later in the program.
emojis: str = ""   # A string variable is created that will contain the different emojis representing the correctness of the guess. 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"   # Any word can be inserted, not just "python"
guess: str = input(f"What is your { len(secret) } letter guess? ")   # Establishes the players guess which will be compared to the stored secret word. 

elsewhere: bool = False   # Boolean value telling the program whether or not a letter in the guess appears in the wrong position in the secret word.
alti: int = 0   # Alternative index used for checking if letters are in a word in the wrong place.

while len(guess) != len(secret):   # Prompts the player for a guess again if the number of characters in the guess did not match the number of characters in the secret word. 
    guess = input(f"That was not { len(secret) } letters! Try again: ")

while index < len(secret):
    alti = 0   # Every iteration starts with reseting the value of the alternate index (alti) so that each letter guessed can be checked to see if other letters in the secret word match.
    if secret[index] == guess[index]:   # If the letter guessed matches the letter in the same position within the secret word, a green box is concatenated in the emoji string.
        emojis = emojis + GREEN_BOX
        index = index + 1   # Index is increased by one telling the program to move on to checking the next letter.
    else:
        while elsewhere is False and alti < len(secret):   # If the letters do not match, the program loops checking each letter of the secret word to see if contains any of the same letters.
            if secret[alti] == guess[index]:   # If the secret word does share a letter in the wrong position with the guessed word, elsewhere is set to true and a yellow box emoji is concatenated with the string. 
                elsewhere = True
            else:
                alti = alti + 1   # The alternate index is increased by one and restarts the while loops, checking all letters of the secret word for matches in the wrong place.
        if elsewhere is True:   # If a letter in the guessed word matches a letter in the secret word in the wrong position elsewhere is set to true and a yellow box is concatenated onto the emoji string variable.
            emojis = emojis + YELLOW_BOX
            elsewhere = False   # Resets the value of elsewhere to False after adding the yellow box so that the program can check the other letters guessed in the while loop.
            alti = alti + 1
        else:
            emojis = emojis + WHITE_BOX   # If no matching letters are found between the secret and guess words, a white box is concatenated onto the emoji string. 
        index = index + 1 

print(str(emojis))   # After the emoji string has been formed it is printed showing the player how close their guess word was to the secret.

if secret == guess:   # After emojis are printed, message will be sent telling the player if they got the word or not. 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")