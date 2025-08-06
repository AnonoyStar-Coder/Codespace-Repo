import random
import curses
from collections import Counter

# List of fruits
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')

# ASCII art for the hangman stages
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# ASCII art for the title and game over screen
title_art = r"""
 ____  ____                                                             
|_   ||   _|                                                            
  | |__| |    ,--.    _ .--.     .--./)  _ .--..--.    ,--.    _ .--.   
  |  __  |   `'_\ :  [ `.-. |   / /'`\; [ `.-. .-. |  `'_\ :  [ `.-. |  
 _| |  | |_  // | |,  | | | |   \ \._//  | | | | | |  // | |,  | | | |  
|____||____| \'-;__/ [___||__]  .',__`  [___||__||__] \'-;__/ [___||__] 
                               ( ( __))                                
"""

def display_game_status(stdscr, chances_left, guessed_letters, word):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Display hangman stage centered
    hangman_stage = hangman_stages[len(hangman_stages) - chances_left - 1]
    for idx, line in enumerate(hangman_stage.splitlines()):
        stdscr.addstr(idx, w // 2 - len(line) // 2, line)

    # Display chances left and the word to be guessed
    stdscr.addstr(len(hangman_stage.splitlines()) + 1, w // 2 - len(f"Chances left: {chances_left}") // 2, f"Chances left: {chances_left}")
    
    word_display = "Word: " + " ".join([char if char in guessed_letters else "_" for char in word])
    stdscr.addstr(len(hangman_stage.splitlines()) + 3, w // 2 - len(word_display) // 2, word_display, curses.A_BOLD)

    # Display guessed letters
    guessed_display = "Guessed letters: " + " ".join(guessed_letters)
    stdscr.addstr(len(hangman_stage.splitlines()) + 5, w // 2 - len(guessed_display) // 2, guessed_display)
    stdscr.refresh()

def center_text(stdscr, text, start_y):
    h, w = stdscr.getmaxyx()
    for idx, line in enumerate(text.splitlines()):
        x = w // 2 - len(line) // 2
        y = start_y + idx
        stdscr.addstr(y, x, line)

def end_screen(stdscr, message):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Display title art at the top, centered
    center_text(stdscr, title_art, 0)

    # Display message centered below the title art
    stdscr.addstr(len(title_art.splitlines()) + 1, w // 2 - len(message) // 2, message, curses.A_BOLD)

    # Display instruction to exit centered
    exit_msg = "Press any key to exit..."
    stdscr.addstr(len(title_art.splitlines()) + 3, w // 2 - len(exit_msg) // 2, exit_msg, curses.A_DIM)
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    word = random.choice(someWords)
    guessed_letters = []
    chances_left = 6
    flag = False

    # Title Screen
    h, w = stdscr.getmaxyx()

    stdscr.clear()
    # Display title art at the top, centered
    center_text(stdscr, title_art, 0)

    # Display the title and instructions centered
    title = "Welcome to Hangman!"
    subtitle = "Guess the word! HINT: The word is a name of a fruit."
    stdscr.addstr(len(title_art.splitlines()) + 1, w // 2 - len(title) // 2, title, curses.A_BOLD)
    stdscr.addstr(len(title_art.splitlines()) + 3, w // 2 - len(subtitle) // 2, subtitle)
    start_msg = "Press any key to start..."
    stdscr.addstr(len(title_art.splitlines()) + 5, w // 2 - len(start_msg) // 2, start_msg, curses.A_DIM)
    stdscr.refresh()

    stdscr.getch()  # Wait for user input to start the game

    while chances_left > 0 and not flag:
        display_game_status(stdscr, chances_left, guessed_letters, word)
        guess = stdscr.getkey().lower()

        if not guess.isalpha() or len(guess) != 1:
            stdscr.addstr("Please enter a single letter.\n", curses.A_BLINK)
            continue

        if guess in guessed_letters:
            stdscr.addstr("You've already guessed that letter.\n", curses.A_BLINK)
            continue

        guessed_letters.append(guess)

        if guess in word:
            stdscr.addstr(f"Good guess! '{guess}' is in the word.\n", curses.A_BOLD)
            if all(char in guessed_letters for char in word):
                flag = True
                display_game_status(stdscr, chances_left, guessed_letters, word)
                end_screen(stdscr, "Congratulations! You've guessed the word!")
        else:
            stdscr.addstr(f"Sorry, '{guess}' is not in the word.\n", curses.A_BLINK)
            chances_left -= 1

    if not flag:
        end_screen(stdscr, f"Game Over! The word was: {word}")

    stdscr.clear()
    stdscr.refresh()

curses.wrapper(main)

