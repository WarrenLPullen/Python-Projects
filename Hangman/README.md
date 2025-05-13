# Hangman Game

## Description

A classic Hangman game implemented in Python. Guess the hidden word letter by letter. Incorrect guesses display parts of the hangman figure.

## How to Play

1.  Guess a letter.
2.  Correct guess: Letter revealed.
3.  Incorrect guess: Hangman figure updated, life lost.
4.  Game ends on word guess or life loss.

## Files

* `main.py`: Main game logic.
* `hangman_words.py`: Word list.
* `hangman_art.py`: ASCII art for Hangman.


## Game Flow

1.  **Setup:** Imports, word selection, placeholders.
2.  **Gameplay Loop:**
    * Print logo, word state, lives.
    * Get letter guess, validate input.
    * Update word display.
    * Handle correct/incorrect guesses.
    * Check win/loss conditions.
    * Print Hangman stage.
3.  **End Game:** Display win/loss message.

## Code Details

* `hangman_art.py`: Contains Hangman ASCII art.
* `hangman_words.py`: Contains the word list.
* `main.py`:
    * Imports modules.
    * Implements game logic using a `while` loop.
    * Tracks lives and game state.

## Improvements

* Input validation.
* Play again option.
* Scoring.
* More words.
* GUI.
* Difficulty levels.
* Display guessed letters.
