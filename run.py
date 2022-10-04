import time
from time import sleep
import random
from colors import Color as Col


def game_logo():
    """
    Displays Game Title
    """
    print(Col.BLUE + "Hello, Welcome To:")
    print(" ")
    print(Col.LOGO_R + " _    _")
    print(Col.LOGO_R + "| |  | |")
    print(Col.LOGO_R + "| |  | |")
    print(Col.LOGO_R + "| |  | |      _       ___      _   ____")
    print(Col.LOGO_R + "| |__| |     / \     |   \    | | / ___\ ")
    print(Col.LOGO_R + "|  __  |    / _ \    | |\ \   | |/ /")
    print(Col.LOGO_R + "| |  | |   / /_\ \   | | \ \  | || |  ___")
    print(Col.LOGO_R + "| |  | |  /  ___  \  | |  \ \ | || | |__ |")
    print(Col.LOGO_R + "| |  | | /  /   \  \ | |   \ \| |\  \__/ /")
    print(Col.LOGO_R + "|_|  |_|/__/     \__\|_|    \___| \_____/")
    print(Col.LOGO_R + " ___      ___       _       ___      _")
    print(Col.LOGO_R + "|   \    /   |     / \     |   \    | |")
    print(Col.LOGO_R + "| |\ \  / /| |    / _ \    | |\ \   | |")
    print(Col.LOGO_R + "| | \ \/ / | |   / /_\ \   | | \ \  | |")
    print(Col.LOGO_R + "| |  \__/  | |  /  ___  \  | |  \ \ | |")
    print(Col.LOGO_R + "| |        | | /  /   \  \ | |   \ \| |")
    print(Col.LOGO_R + "|_|        |_|/__/     \__\|_|    \___|")
    print(" ")
    print(" ")
    print(" ")
    time.sleep(1)


def seperate_lines():
    """
    Print '-' lines to seperate messages
    """
    print(" ")
    print("- "*30)
    print(" ")


def main_screen() -> str:
    """
    The game will load two possible options for the
    user to select from, view game rules or start
    game
    """
    time.sleep(1)
    print(COL.BLUE + "Pick an option to continue...")
    continue_options = "1). View rules of game\n2). Play Game\n"
    continue_options_selected = input(continue_options)
    seperate_lines()

    # Confirm if answer is either 1 or 2
    while continue_options_selected not in ("1", "2"):
        print(Col.YELLOW + "Please choose option one or 2 to move on:")
        continue_options_selected = input(continue_options)
        seperate_lines()

    if continue_options_selected == "1":
       game_logo()
       rules()

    elif  continue_options_selected == "2":
        start_hangman()

    return continue_options_selected


def rules():
    """
    Display rules of the game which
    user can exit by pressing any key
    """
    print(Col.RED + "Game Rules:")
    print("The rules of the game are simple, a random word will be " +
        "generated simply type in any letter to guess the word")
    time.sleep(1)
    print(" ")
    seperate_lines()
    input("Press any key to exit...\n")
    main_screen()


def start_hangman() -> str:
    """
    The game will check if user has played before
    """
    time.sleep(1)
    print(Col.GREEN + "Have you played this game before?")
    answer = "1). Yes \n2). No\n"
    answered = input(answer)
    seperate_lines()

    # Confirm if answer is either Yes or No
    while answered not in ("1", "y", "2", "n"):
        print(Col.CYAN + "Please select one of the options shown:")
        answered = input(answer)

        seperate_lines()

    if answered == "1" or answered == "y":
        game_logo()
    
    elif answered == "2" or answered == "n":
        game_logo()

    return answered


