import random

def main():
        show_header()
        play_game('You','Computer')

def show_header():
    print("-----------------------------")
    print(" Rock Paper Scissors V1 ")
    print("----------------------------")

def play_game(player_1,player_2):
    rounds = 2
    wins_p1 = 0
    wins_p2 = 0

    rolls = ['rock', 'paper','scissors']

    while wins_p1 < rounds and wins_p2 < rounds:

        roll1 = get_roll(player_1, rolls)
        # roll2 = get_roll(player_2,rolls)
        roll2 = random.choice(rolls)

        if not roll1:
                print("Try again!")
                continue

        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")

        # test for a winner

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        print(f"Round {wins_p1 + wins_p2 + 1} is over")
        if winner is None:
            print("It was a tie.")
        else:
            if winner == player_1:
                wins_p1 += 1
                print(f"The winner is {winner}")
            elif winner == player_2:
                wins_p2 += 1
                print(f"The winner is {winner}")
    if wins_p1 >= rounds:
        overall_winner = player_1
    else:
        overall_winner = player_2

    print(f'{overall_winner} wins the game!')


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("game was tied")
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_2
        elif roll2 == 'scissors':
            winner = player_1
    elif roll1 == 'paper':
        if roll2 == 'scissors':
            winner = player_2
        elif roll2 == 'rock':
            winner = player_1
    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_2
        elif roll2 == 'paper':
            winner = player_1
    return winner


def get_roll(player_name,rolls):

    print('available options:')
    for idx, r in enumerate(rolls, start=1):
        print(f'{idx}.{r}')

    player_select = input(f'{player_name}Pick your roll: ')
    player_int = int(player_select) - 1

    if player_int <0 or player_int >= len(rolls):
        print(f'Yeahhhhh {player_name}, I am gonna need you to not do that.')
        return None

    roll = rolls[player_int]
    # roll = input(f"{player_name}, what is your roll? [rock, paper, scissors]: ")
    # roll = roll.lower().strip()
    # if roll not in rolls:
       # print(f"Sorry {player_name}, {roll} is not a valid play!")
       # return None

    return roll

if __name__ == '__main__':
    main()

