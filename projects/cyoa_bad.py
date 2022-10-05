"""EX06 - Choose Your Own Adventure Game."""

__author__ = "730564467"

main_times: int = 0 
# Establishes a variable to keep track of how many times main is run
# so that if main is run more than once the player is not reprompted
# for their name.


def main() -> None:
    """Entrypoint of the CYOA game."""
    global main_times
    main_times += 1
    global points
    points = 0
    global player
    if main_times == 1:
        player = ""
    greet()
    choice_1: str = ""
    choice_1 = input(f"{player}, what would you like to do? \n a - Yell for Help. \n b - Walk down the stairs \n c - Try to break out the front door \n:")
    points += 1
    i: int = 0

    if choice_1 == "a":
        choice_1 = input(f"You call out, but you hear no response. \nWhat would you like to do, {player}? \n a - Yell for Help. \n b - Walk down the stairs \n c - Try to break out the front door \n:")

    while choice_1 == "a" and i < 9: # Continue prompting the player for an answer until they pick b or c or continue to choose a 8 more times. 
        choice_1 = input(f"You call out again, but you still hear no response. \nWhat would you like to do, {player}? \n a - Yell for Help. \n b - Walk down the stairs \n c - Try to break out the front door \n:")
        i += 1

    if i == 10: # Secret ending: if the player keeps calling for help, they will eventually reach this secret ending getting them 10 adventure points and asking if they would like to play again.
        points += 10
        print(f"Out of nowhere, Kevin Guskiewicz comes out from around the corner! \n\"{player}, is that you?\" He says. \n\"Here, let me help you get out of this place!\" \n\nCongratulations! You got a secret ending!")
        print(f"You have {points} *spooky* adventure points!")
        playagain: str = ""
        playagain = input("Would you like to play again? y/n: ")
        if playagain == "y":
            main()
        else:
            print(f"Thanks for playing, {player}!")
            return None



def greet() -> None: # Saves player's name as a global variable and gives th player background info for their cyoa game!
    """Greets the player."""
    global player
    if player == "":
        player = input("Please enter your name: ")
    print(f"Welcome, {player}, to Kris Jordan's escape room spooktacular! \nYou mysteriously wake up just inside what appears to be Sitterson Hall!")
    print("It is dark and storming outside. You look around but no one is to be seen.")




if __name__ == "__main__":
    main()

