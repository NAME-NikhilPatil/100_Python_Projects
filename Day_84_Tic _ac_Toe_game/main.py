def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


# I think is very funny game hehe

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions


def check_draw(board):
    # Check if all cells are filled, and there is no winner
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get the row and column input from the user
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("Please enter a valid number (0, 1, or 2).")
            continue

        # Check if the move is valid
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid position. Choose between 0, 1, or 2.")
            continue
        if board[row][col] != " ":
            print("Position already taken. Choose another spot.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner or a draw
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
