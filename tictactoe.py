"""
Tic-Tac-Toe Game
A simple console-based Tic-Tac-Toe game built in Python for two players.
Players take turns placing 'X' or 'O' on a 3x3 board until someone wins or the game ends in a tie.
"""

# Set up the 3x3 board as a list of lists
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

current_player = "X"
game_over = False


def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(row)


def check_winner(board, player):
    """Check if the given player has three marks in a row, column, or diagonal."""
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def check_tie(board):
    """Check if the board is full with no winner (tie)."""
    for row in board:
        if " " in row:
            return False
    return True


print("=" * 40)
print("Welcome to Tic-Tac-Toe!")
print("Players take turns. Enter row and column (0-2).")
print("=" * 40)
print_board(board)

while not game_over:
    print("\nCurrent player:", current_player)

    row = int(input("Enter row (0, 1, or 2): "))
    col = int(input("Enter column (0, 1, or 2): "))

    # Prevent overwriting a filled cell
    if board[row][col] != " ":
        print("That cell is already taken. Try again.")
        continue

    board[row][col] = current_player
    print_board(board)

    if check_winner(board, current_player):
        print("\nPlayer", current_player, "wins!")
        game_over = True
    elif check_tie(board):
        print("\nIt's a tie!")
        game_over = True
    else:
        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"