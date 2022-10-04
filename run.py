import time
from time import sleep
import random
from colors import Color as Col


MAX_TURNS = 10
game_running = True
word_bank = ["constitutional", "river", "president", "avenue", "game",
             "developer", "engineer", "mathematics", "gun", "robbery",
             "supplementary", "scene", "tree", "conscious", "school",
             "sports", "football", "wrestling", "dangerous", "motorsport"
             "jesus", "plastic", "therapy", "love", "professor", "ball",
             "negligence", "discrimination", "representative", "glide"]

""" 
Choose a random word
"""

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
    print(Col.BLUE + "Pick an option to continue...")
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


def show_hangman(wrong):
    """
    Display hangman when wrong guesses are made
    """
    if (wrong == 0):
        print("\n")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif(wrong == 1):
        print("\n")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print(" ")
    elif(wrong == 2):
        print("\n")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("   ___")
    elif(wrong == 3):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("   ___")
    elif(wrong == 4):
        print("\n+---+")
        print("|   |")
        print("    |")
        print("    |")
        print("    |")
        print("   ___")
    elif(wrong == 5):
        print("\n+---+")
        print(" |  |")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ___")
    elif(wrong == 6):
        print("\n+---+")
        print(" |  |")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ___")
    elif(wrong == 7):
        print("\n+---+")
        print(" |  |")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ___")
    elif(wrong == 8):
        print("\n+---+")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ___")
    elif(wrong == 9):
        print("\n+---+")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ___")
    elif(wrong == 10):
        print("\n+---+")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ___")


def show_word(pickedLetters):
    """
    Display the already picked letters and how many
    guesses left
    """
    counter = 0
    correct_letters = 0
    for char in random_word:
        if (char in pickedLetters):
            print(random_word[counter].upper(), end=" ")
            correct_letters += 1
        else: 
            print(" ", end=" ")
        counter += 1
    return pickedLetters


def lines():
    """
    Shows the correct word
    """
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")


def check_guessed_word(guess, word):
    """
    Check for correctly guessed word
    """
    if guess in word:
        return True
    return False


def verify_input(text, valid_values_list):
    input_is_correct = False
    while input_is_correct is False:
        input_value = input(text)
        if input_value.lower() in valid_values_list:
            input_is_correct = True
        else:
            print(f"Please enter a correct option: {str(valid_values_list)}")
    return input_value


