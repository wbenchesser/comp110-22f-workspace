"""EX06 - Choose Your Own Adventure Game."""

__author__ = "730564467"

from random import randint


GHOST: str = "\U0001F47B"
JACK: str = "\U0001F383"
ZOMBIE: str = "\U0001F9DF"
BAT: str = "\U0001F987"
VAMP: str = "\U0001F9DB"


player: str = ""  # A global variable named player is defined to track the player’s name.
points: int = 0  # Due to static typing requirements, points is first defined as a int outside of main. 
main_times: int = 0  # A variable which keeps track of how many times main is run. 


def main() -> None:
    """Entrypoint of the game that establishes points and player global variables and starts cyoa game."""
    global points 
    global player
    global main_times
    main_times += 1
    if main_times < 2:  # If main() has already been run onced, points should not be reset to zero and should rather carry over. 
        points = 0
    greet()  # Calls greet function to establish a global variable of the players name and introduce them to the background of the game. 
    choice_1: str = input(f"{player}, what would you like to do? \n a - Yell for Help {GHOST} \n b - Walk down the stairs {VAMP} \n c - Try to break out {BAT} \n d - End game {ZOMBIE}\n:")
    points += 1
    if choice_1 == "d":  # Choice 1/4 that ends the experience and prints a goodbye message.
        print("Saddened and defeated, you lay back down on the ground and give up.")
        end()  # A function that tells the player how many points they have and asks if they would like to play again. 
    elif choice_1 == "a":
        print(f"Hearing your call for help, Kevin Guskiewicz comes out from around the corner! \n\"{player}, is that you?\" He says. \"Here, let me help you get out of this place!\"")
        end()
    elif choice_1 == "b":  
        stairs()  # Adventure points are used in this procedure via global variables. 
    elif choice_1 == "c":
        points = break_out(points)  # Rather than using global variables, choice c "passes" the points variable to the break_out function where it is adjusted and "passed" back.
        end()


def greet() -> None:  # Procedure, called at the beginning of main().
    """Saves player's name as a global variable and gives the player background info for their cyoa game!"""
    global player  # Assigns the name input by the user to the global variable named player.
    if player == "":  # Allows for those replaying the game to not be reprompted for their name .
        player = input("Please enter your name: ")
    print(f"     {JACK} Welcome, {player}, to Kris Jordan's escape room spooktacular! {JACK} \n You mysteriously wake up just inside what appears to be Sitterson Hall!")
    print("It is dark and storming outside. You look around but no one is to be seen.")


def break_out(points: int) -> int:  # Custom function that utilizes "passes" the players points through the function, and back to main().
    """The player chooses to try and break out!"""
    print("You see that scattered across the ground near a large window is some halloween candy.")
    print("You decide that you are going to start throwing this candy at the window to try and break it open.")
    candy: int = input("How much candy would you like to throw at the window at a time? ")
    throws: int = candies(candy)
    candy = 100 // throws
    if 100 // throws != 0:
        candy += 1
    points += (int(candy) // 5)
    print(f"You break the window by throwing {candy} candies at the window {throws} times.")
    print("After getting outside, you see Ben from the Comp 110 team!")
    bonus: int = randint(1, 5)  # Ben from the Comp 110 team gives the player a random number of *spooky* adventure points from 1-5.
    print(f"He says \"You've done well\" and gives you {bonus} bonus *spooky* adventure points! {GHOST}{JACK}{ZOMBIE}{BAT}{VAMP}")
    points += bonus
    return points


def end() -> None:
    """Congratulates the player for reaching an ending, tells them how many points they have, and asks if they want to play again."""
    global points
    print("You reached an ending!")
    if points == 0:
        print("You have no *spooky* adventure points.")
    elif points == 1:
        print("You have 1 *spooky* adventure point!")
    elif points > 1:
        print(f"You have {points} *spooky* adventure points!")
    playagain: str = ""
    playagain = input("Would you like to play again? y/n: ")
    if playagain == "y":
        main()  # Functions as a game loop, allowing the player to replay and keep their previous adventure points. 
    else:
        print(f"Thanks for playing, {player}!")
        return None
    

def stairs() -> None:  # A custom procedure that lead to textual interaction(s) that make use of players name and ask the player for additional input.
    """The player decides to go down the stairs."""
    global points
    print("Getting to the bottom of the stairs you look down a hallway. \nYou walk down it and at the end there is a crossroads.")
    print(f"You see a message written on the wall in messy, red ink \nIt says \"Go right, {player}!\"")
    choice_2: str = input("What would you like to do? \na - Go Right \nb - Go Left \n:")
    if choice_2 == "a":
        points += 2
        right()
    if choice_2 == "b":
        points += 1
        left()


def left() -> None:  # A custom procedure that lead to textual interaction(s) that make use of players name and ask the player for additional input.
    """The player chooses to go left."""
    global player
    global points
    print("You decide to go left, against the suggestion of the message.")
    print("At the end of the left hallway is a door with more red writing that says")
    print("Im serious, go back and go to the right! ")
    choice_3: str = ""
    choice_3 = input("What would you like to do? \na - Go back and go down the right hallway \nb - Open the door. \n:")
    if choice_3 == "a":
        points += 1
        right()
    if choice_3 == "b":
        print("You open the door and you see the Comp Sci team looking very disapointed in you.")
        print(f"\"{player}\"! We said go right!")
        points -= 3
        print("They take away 3 of your *spooky* adventure points.")
        end()


def right() -> None:  # A custom procedure that lead to textual interaction(s) that make use of players name and ask the player for additional input.
    """The player chooses to go right."""
    global points
    print("You decide to go right, following the instructions of the red message.")
    print("At the end of the hallway you find a computer!")
    print("Open on it is some code that says \n Comp110 == Spooky.")
    choice_4: str = input("What do you type? \na - True \nb - False \n:")
    if choice_4 == "a":
        print("When you type True, a secret door opens up.")
        print("You look inside and see Kris Jordan and a bunch of Computer Science students at a halloween party!")
        print(f"\"Congrats {player}! You made it!\" Kris says.")
        print(f"Here, take 5 free *spooky* adventure points! {GHOST}{JACK}{ZOMBIE}{BAT}{VAMP}")
        points += 5
        end()
    if choice_4 == "b":
        points += 1
        print("A message pops up on the screen that says:")
        print(f"Oh, this isn't spooky, {player}? \nI'll show you spooky!")
        print("A trap door opens up beneath your feet and you fall!")
        print("Game Over.")
        end()
    
 
def candies(pieces: int) -> int:
    """It takes 100 total halloween candy throws to break the window, how many handfuls of candy does it take to break the window?"""
    global player
    pieces = int(pieces)
    while pieces < 0 or pieces > 15 or pieces == 0:
        if pieces < 0:
            print("You feel like trying to throw a negative amount of candy may disrupt the space-time continuum.")
            pieces = int(input(f"How many would you like to throw instead, {player}? \n:"))
        if pieces > 15: 
            print(f"You try to pick up {pieces} candies at a time, but you just can't fit that many in your hands.")
            pieces = int(input(f"How many would you like to throw instead, {player}? \n:"))
        if pieces == 0: 
            print("You feel that throwing no candies is a very inefficient way of breaking the window.")
            pieces = int(input(f"How many would you like to throw instead, {player} \n:?"))
    throw_count: int = (100 // pieces)
    if 100 % pieces != 0:
        throw_count += 1
    return throw_count


if __name__ == "__main__":  # Python idiom for calling main at the end of the program.
    main()