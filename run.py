import random
from colors import Color as Col


MAX_TURNS = 10
game_running = True
word_bank = ["constitutional", "river", "president", "avenue", "game",
             "developer", "engineer", "mathematics", "gun", "robbery",
             "supplementary", "scene", "tree", "conscious", "school",
             "sports", "football", "wrestling", "dangerous", "motorsport",
             "jesus", "plastic", "therapy", "love", "professor", "ball",
             "negligence", "discrimination", "representative", "glide"]

"""
Choose a random word
"""


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
    elif (wrong == 1):
        print("\n")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(" ")
    elif (wrong == 2):
        print("\n")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "   ___")
        print(" ")
    elif (wrong == 3):
        print(Col.GREEN + "\n+---+")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "   ___")
        print(" ")
    elif (wrong == 4):
        print(Col.GREEN + "\n+---+")
        print(Col.GREEN + "|   |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "   ___")
        print(" ")
    elif (wrong == 5):
        print(Col.GREEN + "\n+---+")
        print(Col.GREEN + " |  |")
        print(Col.GREEN + " O  |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "   ___")
        print(" ")
    elif (wrong == 6):
        print(Col.GREEN + "\n+---+")
        print(Col.GREEN + " |  |")
        print(Col.GREEN + " O  |")
        print(Col.GREEN + " |  |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "   ___")
        print(" ")
    elif (wrong == 7):
        print(Col.GREEN + "\n+---+")
        print(Col.GREEN + " |  |")
        print(Col.GREEN + " O  |")
        print(Col.GREEN + "/|  |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "   ___")
        print(" ")
    elif (wrong == 8):
        print(Col.GREEN + "\n+---+")
        print(Col.GREEN + " |  |")
        print(Col.GREEN + " O  |")
        print(Col.GREEN + r"/|\ |")
        print(Col.GREEN + "    |")
        print(Col.GREEN + "   ___")
        print(" ")
    elif (wrong == 9):
        print(Col.GREEN + "\n+---+")
        print(Col.GREEN + " |  |")
        print(Col.GREEN + " O  |")
        print(Col.GREEN + r"/|\ |")
        print(Col.GREEN + "/   |")
        print(Col.GREEN + "   ___")
        print(" ")
    elif (wrong == 10):
        print(Col.GREEN + "\n+---+")
        print(Col.GREEN + " |  |")
        print(Col.GREEN + " O  |")
        print(Col.GREEN + r"/|\ |")
        print(Col.GREEN + r"/ \ |")
        print(Col.GREEN + "   ___")
        print(" ")


def show_word(pickedletters):
    """
    Display the already picked letters and how many
    guesses left
    """
    counter = 0
    correct_letters = 0
    for char in random_word:
        if (char in pickedletters):
            print(random_word[counter].upper(), end=" ")
            correct_letters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return correct_letters


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


def main_screen() -> str:
    """
    The game will load two possible options for the
    user to select from, view game rules or start
    game
    """
    print(Col.BLUE + "Pick an option to continue...")
    continue_options = "1). View rules of game\n2). Play Game\n"
    continue_options_selected = input(continue_options)
    # Confirm if answer is either 1 or 2
    while continue_options_selected not in ("1", "2"):
        print(Col.YELLOW + "Please choose option one or two to move on:")
        continue_options_selected = input(continue_options)

    if continue_options_selected == "1":
        rules()

    elif continue_options_selected == "2":
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
    print("Keep guessing a letter until you have " +
          "guessed the word or ran out of guesses")
    print(" ")
    input(Col.RED + "Press any key to exit...\n")
    main_screen()


def start_hangman():
    """
    The game will check if user has played before
    """
    print(Col.GREEN + "Have you played this game before?")
    answer = "1). Yes \n2). No\n"
    answered = input(answer)
    # Confirm if answer is either Yes or No
    while answered not in ("1", "y", "2", "n"):
        print(Col.CYAN + "Please select one of the options shown:")
        answered = input(answer)

    if answered == "1" or answered == "y":
        __name__
    elif answered == "2" or answered == "n":
        rules()

    return answered


"""
Running the game
"""
if __name__ == "__main__":
    while (game_running):
        random_word = random.choice(word_bank)
        print(Col.BLUE + "Hello, Welcome To:")
        print(" ")
        print(Col.LOGO_R + r" _    _")
        print(Col.LOGO_R + r"| |  | |")
        print(Col.LOGO_R + r"| |  | |")
        print(Col.LOGO_R + r"| |  | |      _       ___      _   ____")
        print(Col.LOGO_R + r"| |__| |     / \     |   \    | | / ___\ ")
        print(Col.LOGO_R + r"|  __  |    / _ \    | |\ \   | |/ /")
        print(Col.LOGO_R + r"| |  | |   / /_\ \   | | \ \  | || |  ___")
        print(Col.LOGO_R + r"| |  | |  /  ___  \  | |  \ \ | || | |__ |")
        print(Col.LOGO_R + r"| |  | | /  /   \  \ | |   \ \| |\  \__/ /")
        print(Col.LOGO_R + r"|_|  |_|/__/     \__\|_|    \___| \_____/")
        print(Col.LOGO_R + r" ___      ___       _       ___      _")
        print(Col.LOGO_R + r"|   \    /   |     / \     |   \    | |")
        print(Col.LOGO_R + r"| |\ \  / /| |    / _ \    | |\ \   | |")
        print(Col.LOGO_R + r"| | \ \/ / | |   / /_\ \   | | \ \  | |")
        print(Col.LOGO_R + r"| |  \__/  | |  /  ___  \  | |  \ \ | |")
        print(Col.LOGO_R + r"| |        | | /  /   \  \ | |   \ \| |")
        print(Col.LOGO_R + r"|_|        |_|/__/     \__\|_|    \___|")
        print(" ")
        print(" ")
        print(" ")
        show_hangman(0)
        for x in random_word:
            print("_ ", end="")
        word_length = len(random_word)
        times_wrong = 0
        guess_index = 0
        letters_guessed = []
        letters_right = 0
        main_screen()
        while (times_wrong != MAX_TURNS and letters_right != word_length):
            """
            Show users possible letter inputs
            """
            show_letters_guessed = verify_input("\nPlease guess a letter: ",
                                                ["a", "b", "c", "d", "e", "f",
                                                 "g", "h", "i", "j", "k", "l",
                                                 "m", "n", "o", "p", "q", "r",
                                                 "s", "t", "u", "v", "w", "x",
                                                 "y", "z"])
            """
            Display the users guesses if correct or false,
            upon failure, display the correct word to user.
            """
            letters_guessed.append(show_letters_guessed)
            if check_guessed_word(show_letters_guessed, random_word) is False:
                times_wrong += 1
            letters_right = show_word(letters_guessed)
            lines()
            show_hangman(times_wrong)
            print("Guesses left = {}".format(MAX_TURNS -
                                             times_wrong))
            print("Correct guess = {}".format(letters_right))
            if letters_right >= len(random_word):
                print("\n\n Congratulations, You've Won!! \n\n")
                break
            elif times_wrong >= MAX_TURNS:
                print("\n\n You have lost! The word was '" + random_word +
                      "', better luck next time!\n")
            """
            Allow user to restart game or start with a new word
            """
            play_again = verify_input("\n Do you want to play again? (Y/N): ",
                                      ['y', 'yes', 'yeah', 'n', 'no'])
            if play_again in ['y', 'yes', 'yeah']:
                game_running = True
            else:
                exit()
                """
                Game ending message
                """
                print("You selected no, Your game has ended!")
