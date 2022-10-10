# HANGMAN GAME <img src="https://cdn-icons-png.flaticon.com/512/514/514163.png" style="width: 35px; height:35px;">

**Developer: Zack Owen**

[Live website](https://hangman-ci-game.herokuapp.com/)

![Mockup Image](docs/hangman-home.png)

## About

This is a command-line version of the classic Hangman game we all know.

The classic game is played by guessing a randomly generated word by picking an individual letters on each go. Each player will get to keep guessing a letter until they either get the correct word or the hanging man shows. The hanging man will show after 10 incorrect guesses.

The objective of the game is to correctly guess the randomly generated word before the hanging man shows.

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Play a fun easy game.
- Read the rules before playing.
- Be able to see whether you win or lose

### Site Owner Goals

- Create a game that is user to play for users
- Ensure that users can understand the rules of the game
- Give users feedback whilst playing

## User Experience

### Target Audience

There is no specific target audience as this game can be played by everyone. However I would recommend anyone above the age of 8 to play this game.

### User Requirements and Expectations

- A simple, error-free game
- Easy navigation
- Feedback on game results

### User Manual

<details><summary>Click here to view game instructions</summary>

#### Main Menu
On the main menu, users are presented with a custom made Hangman title. Below the title graphic there are 2 options for the user to choose from.
Operation: Input a numeric value or y/n and press enter.
1. View game rules
2. Play game

If at any point the user has inputted an incorrect value, the user will be prompted to try again.

#### Game Rules
With the game rules option, the users are presented with a short message about the game rules, once read the users can return back to the main menu.
Operation: Press any key and hit enter.

#### Play
With the play game option, users are asked if they have played the game before. 
Operation: Input a numeric value.
The extra inputs for available are 'y' for yes or 'n' for no.
1. Yes
2. No

#### Play Again
At the end of the game if the user wins or loses they can select if they want to play again.
Operation: Input a letter value.
1. Y
2. N

#### Go Back To Main Menu
At the end of game the user can return to the main menu if they win or lose.
Operation: Input a letter value.
1. Yes
2. No

Note if the user wins, the game will automatically return to the main menu.

</details>

[Back to Table of Contents](#table-of-contents)

## User Stories
