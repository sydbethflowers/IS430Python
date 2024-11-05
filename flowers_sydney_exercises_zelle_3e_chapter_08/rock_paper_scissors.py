""" Demonstrate playing Rock, Paper, Scissors with python. """


from random import choice

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'


def main():
    print('Welcome to The Rock-Paper-Scissors Game.\n')
    value_a, value_b = play_turn()

    while value_a == value_b:
        value_a, value_b = play_turn()

    if (
        (value_a == 'ROCK' and value_b == 'SCISSORS') or
        (value_a == 'SCISSORS' and value_b == 'PAPER') or
        (value_a == 'PAPER' and value_b == 'ROCK')
    ):
        print('Player A wins!')
    else:
        print('Player B wins!')


def play_turn():
    a_value = rock_paper_scissors()
    b_value = rock_paper_scissors()
    print(f'Player A gets {a_value}. Player B gets {b_value}.')
    return a_value, b_value


def rock_paper_scissors():
    return choice([ROCK, PAPER, SCISSORS])


main()
