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