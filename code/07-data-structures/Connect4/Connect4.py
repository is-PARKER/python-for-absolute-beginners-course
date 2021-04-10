# Assign players a symbol +
# Create board +
# Have players drop in board
# toggle player +
# check for winner
# Display winner

def main():

    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ['x', 'o']
    player = players[active_player_index]


    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol, rise=0):
            print("That isn't an option, try again.")
            continue

        active_player_index = (active_player_index + 1) % len(players)
    print(f"Game OVer! {player} wins the round!")
    show_board(board)


def choose_location(board, symbol, rise):
        #pick a column
    column = int(input(f"Choose a column to place your piece!"))
    column -= 1
    if column < 0 or column >= len(board[0]):
        return False

    #cell = board[len(board) - 1][column]



    while not board[len(board) - (1+rise)][column] == None:
        rise += 1
        if (len(board) - (rise)) < 1:
            rise = 0
            return False
        #cell = board[len(board)-(1 + rise)][column]



    if board[len(board)-(1 + rise)][column] == None:
        board[len(board)-(1 + rise)][column] = symbol
        rise = 0
        return True

        # bring column choice to bottom
        # check if empty
        # if not put it on an empty


def show_board(board):
    for row in board:
        print(" | ", end='')
        for cell in row:
            symbol = cell if cell is not None else '_'
            print(symbol, end=" | ")
        print()

def announce_turn(player):
    print()
    print(f"it's {player} turn. Here's the board:")
    print()


def find_winner(board):
    sequences = get_win_sequence(board)


    string_win = ""
    for line in sequences:
            check_string = string_win.join(map(str, line))

            #check_string = string_win.join(sequences)

            linex = "xxxx"
            lineo = "oooo"

            if lineo in check_string or linex in check_string:
                return True

    # win by columns

    return False

def get_win_sequence(board):
    sequences = []

    rows = board
    sequences.extend(rows)

    # win by columns
    for col_idx in range(0, 7):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
            board[3][col_idx],
            board[4][col_idx],
            board[5][col_idx],

        ]
        sequences.append(col)

    diagonals = [
        [board[3][0], board[2][1], board[1][2],board[0][3]],
        [board[4][0], board[3][1], board[2][2], board[1][3], board[0][4]],
        [board[5][0], board[4][1], board[3][2], board[2][3],board[1][4], board[0][5]],
        [board[5][1], board[4][2], board[3][3], board[2][4], board[1][5], board[0][6]],
        [board[5][2], board[4][3], board[3][4], board[2][5], board[1][6]],
        [board[5][3], board[4][4], board[3][5], board[2][6]],
        [board[2][0], board[3][1], board[4][2], board[5][3]],
        [board[1][0], board[2][1], board[3][2], board[4][3], board[5][4]],
        [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5]],
        [board[0][1], board[1][2], board[2][3], board[3][4], board[4][5], board[5][6]],
        [board[0][2], board[1][3], board[2][4], board[3][5], board[4][6]],
        [board[0][3], board[1][4], board[2][5], board[3][6],]
    ]
    sequences.extend(diagonals)

    return sequences


if __name__ == '__main__':
    main()