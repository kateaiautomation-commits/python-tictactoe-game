# ⭕ Tic-Tac-Toe Game (Python)

A simple console-based Tic-Tac-Toe game built in Python. Two players take turns placing 'X' or 'O' on a 3x3 board until someone wins or the game ends in a tie.

## Features

- 3x3 game board represented as a list of lists
- Players alternate turns automatically (X and O)
- Detects wins across rows, columns, and diagonals
- Detects a tie when the board is full with no winner
- Prevents players from overwriting an already-filled cell

## How to Play

1. Run the script:
```bash
   python tictactoe.py
```
2. When prompted, enter a row number (0, 1, or 2) and a column number (0, 1, or 2).
3. Players alternate turns until one player wins or the board fills up (tie).

## Concepts Used

- 2D lists (list of lists) for the game board
- Nested loops and indexing
- Functions for win detection and tie detection
- `if` / `elif` / `else` conditionals
- `while` loop for the main game loop
- User input handling

## Example Gameplay
