# ---------- Board Handling Functions ----------

def create_board():
    #3x3 empty game board.
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    #Prints the game board to the console.
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_cell_empty(board, row, col):
    #Checks if a specific cell is empty.
    return board[row][col] == " "

def is_full(board):
    #Checks if the board is full (draw).
    return all(cell != " " for row in board for cell in row)

# ---------- Game Logic Functions ----------

def check_winner(board, player):
    #Checks if the given player has won the game.
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def switch_player(current_player):
    #Switches player from X to O or O to X.
    return "O" if current_player == "X" else "X"

# ---------- Input Handling Function ----------

def get_player_move(player):
    #Prompts the current player to enter a valid move.
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Out of range. Please choose values between 0 and 2.")
            continue

        return row, col

# ---------- Main Game Loop ----------

def play_game():
    #Runs the main Tic Tac Toe game loop.
    board = create_board()
    current_player = "X"
    print("🎮 Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Get and validate move
        row, col = get_player_move(current_player)
        if not is_cell_empty(board, row, col):
            print("Cell already taken. Try again.")
            continue

        # Make move
        board[row][col] = current_player
        print_board(board)

        # Check for win or draw
        if check_winner(board, current_player):
            print(f"🏆 Player {current_player} wins!")
            break

        if is_full(board):
            print("🤝 It's a draw!")
            break

        # Switch turns
        current_player = switch_player(current_player)

# ---------- Entry Point ----------

if __name__ == "__main__":
    play_game()
