# Python Games Collection

This repository contains various Python scripts demonstrating different game implementations using both console and graphical user interfaces. The games included are:

1. Random Number Guessing Game with Tkinter
2. Tic-Tac-Toe Game with Tkinter
3. Tic-Tac-Toe Game with Hangman Images
4. Quiz Application with Tkinter
5. Number Guessing Game (Console)
6. Tic-Tac-Toe CLI Game (Console)
7. Hangman Game CLI (Console)
8. Hangman Game with Images (Tkinter)

## 1. Random Number Guessing Game with Tkinter

A simple number guessing game where the user tries to guess a randomly generated number between 0 and 10. Feedback is provided via Tkinter message boxes.

### Installation

1. Ensure you have Python installed.
2. Tkinter is usually included with Python. No additional installation is required.

### Usage

1. Run the script:
   ```bash
   python random_number_game.py
   ```

2. Follow the prompts to guess the number.

## 2. Tic-Tac-Toe Game with Tkinter

A graphical Tic-Tac-Toe game where two players can take turns playing on a 3x3 grid. The game detects win conditions and handles player turns.

### Installation

1. Ensure you have Python installed.
2. Tkinter is usually included with Python.

### Usage

1. Run the script:
   ```bash
   python tictactoe.py
   ```

2. Play the game by clicking on the grid.

## 3. Tic-Tac-Toe Game with Hangman Images

An enhanced Tic-Tac-Toe game that displays hangman images to represent incorrect guesses. The game uses Tkinter for the GUI and Pillow for image handling.

### Installation

1. Ensure you have Python installed.
2. Install Pillow:
   ```bash
   pip install pillow
   ```

3. Place hangman images in an `images` folder with filenames `hangman01.png` to `hangman07.png`.

### Usage

1. Run the script:
   ```bash
   python tictactoe_with_images.py
   ```

2. Play the game by clicking on the grid. Images will update with incorrect guesses.

## 4. Quiz Application with Tkinter

A quiz application that uses Tkinter dialogs to ask questions and collect answers from the user. It provides feedback on each answer and displays the final score.

### Installation

1. Ensure you have Python installed.
2. Tkinter is usually included with Python.

### Usage

1. Run the script:
   ```bash
   python quiz.py
   ```

2. Answer the questions in the dialogs and view your final score.

## 5. Number Guessing Game (Console)

A console-based game where the user attempts to guess a randomly generated number between 0 and 10. Feedback is given via console output.

### Installation

1. Ensure you have Python installed.

### Usage

1. Run the script:
   ```bash
   python number_guessing.py
   ```

2. Enter your guesses in the console.

## 6. Tic-Tac-Toe CLI Game (Console)

A simple console-based Tic-Tac-Toe game for two players. Players enter their moves via console input, and the game detects win conditions and draws.

### Installation

1. Ensure you have Python installed.

### Usage

1. Run the script:
   ```bash
   python tictactoe_cli.py
   ```

2. Enter your moves in the console and follow the prompts.

## 7. Hangman Game CLI (Console)

A console-based Hangman game where players guess letters to reveal a hidden word within a limited number of incorrect guesses.

### Installation

1. Ensure you have Python installed.

### Usage

1. Run the script:
   ```bash
   python hangman_cli.py
   ```

2. Guess letters in the console and try to uncover the hidden word.

## 8. Hangman Game with Images (Tkinter)

A graphical Hangman game using Tkinter and images to represent incorrect guesses. The game updates the display with each incorrect guess.

### Installation

1. Ensure you have Python installed.
2. Install Pillow:
   ```bash
   pip install pillow
   ```

3. Place hangman images in an `images` folder with filenames `hangman01.png` to `hangman07.png`.

### Usage

1. Run the script:
   ```bash
   python hangman_with_images.py
   ```

2. Guess letters via Tkinter dialogs and view the hangman images.

## Contributing

Feel free to open an issue or submit a pull request if you have suggestions or improvements for any of the games.

## Contact

For any questions or feedback, please contact asc14088@gmail.com
