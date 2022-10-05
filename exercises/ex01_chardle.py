"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730564467"

number_of_instances: int = 0

five_letter_word: str = input("Enter a 5-character word: ")

if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()

single_letter: str = input("Enter a single character: ")

if len(single_letter) != 1:
    print("Error: Character must be a single character")
    quit()

print("Searching for " + single_letter + " in " + five_letter_word)

if five_letter_word[0] == single_letter:
    print(single_letter + " found at index 0")
    number_of_instances = number_of_instances + int(1)

if five_letter_word[1] == single_letter:
    print(single_letter + " found at index 1")
    number_of_instances = number_of_instances + int(1)

if five_letter_word[2] == single_letter:
    print(single_letter + " found at index 2")
    number_of_instances = number_of_instances + int(1)

if five_letter_word[3] == single_letter:
    print(single_letter + " found at index 3")
    number_of_instances = number_of_instances + int(1)

if five_letter_word[4] == single_letter:
    print(single_letter + " found at index 4")
    number_of_instances = number_of_instances + int(1)

if number_of_instances == 0:
    print("No instances of " + single_letter + " found in " + five_letter_word)

else:
    if number_of_instances == 1:
        print("1 instance of " + single_letter + " found in " + five_letter_word)

    else:
        print(str(number_of_instances) + " instances of " + single_letter + " found in " + five_letter_word)
