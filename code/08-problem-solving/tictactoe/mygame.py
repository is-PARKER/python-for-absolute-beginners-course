
# Create the Board
# Choose an initial player
# until someone wins, check for winner
#   Show the board
#   Choose location, Mark it
#   toggle the active player

# Game over!, active player won!




def main():
    # Board is a list of rows
    # Rows is a list of cells
    board = [
        [None,None,None],
        [None,None,None],
        [None,None,None],
    ]

    # choose initial Player
    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ['x','o']
    player = players[active_player_index]

    #until someone wins
    while not find_winner(board):
        # Show the Board
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue

        active_player_index = (active_player_index + 1) % len(players)
    print(f"Game Over! {player} wins the round")
    show_board(board)

def choose_location(board, symbol):
    row = int(input("Choose which row:"))
    column = int(input("Choose which column: "))

    row -= 1
    column -= 1
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def show_board(board):
    for row in board:
        print(" | ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()

def announce_turn(player):
    print()
    print(f"it's {player} turn. Here's the board:")
    print()

def find_winner(board):
    sequences = get_win_sequence(board)

    for line in sequences:
        symbol1 = line[0]
        if symbol1 and all(symbol1 == line for line in line):
            return True

    # win by columns


    return False

def get_win_sequence(board):
    sequences = []

    rows = board
    sequences.extend(rows)

    # win by columns
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
        ]
        sequences.append(col)

    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    sequences.extend(diagonals)

    return sequences
if __name__ == '__main__':
    main()


