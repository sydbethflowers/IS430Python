""" Simulate the 2-player dice game called, Going to Boston. """

from random import randint


def main():
    rounds_won_a = 0
    rounds_won_b = 0
    print('Welcome to Going to Boston.\n')
    rounds_to_play = get_number_of_rounds()

    for i in range(1, rounds_to_play + 1):
        round_score_a, round_score_b,  = play_round(i)
        rounds_won_a += round_score_a
        rounds_won_b += round_score_b

    if rounds_to_play != 0:
        print_game_results(rounds_won_a, rounds_won_b)


def get_number_of_rounds():
    MAX_ROUNDS = 1000
    MIN_ROUNDS = 1
    valid_value = False
    rounds_as_string = prompt_for_number_of_rounds()

    while not valid_value:
        if rounds_as_string == '' or rounds_as_string == '0':
            print('No rounds were requested. Come play again soon.')
            return 0
        try:
            rounds = int(rounds_as_string)
            if MIN_ROUNDS <= rounds < MAX_ROUNDS:
                valid_value = True
            else:
                print(f'A value between 0 and 1000 was expected. You entered {rounds}.')
                rounds_as_string = input('Please enter the number of rounds to be played (<Enter> to stop): ')

        except ValueError:
            print(f'An integer was expected. You entered {rounds_as_string}.')
            rounds_as_string = input('Please enter the number of rounds to be played (<Enter> to stop): ')

    return rounds


def prompt_for_number_of_rounds():
    return input('Please enter the number of rounds to be played (<Enter> to stop): ')


def play_round(round_number):
    print(f'\nPlaying Round {round_number}:')
    turn_score_a = play_turn('A')
    print(f'===>Player A\'s turn score is {turn_score_a}')
    turn_score_b = play_turn('B')
    print(f'===>Player B\'s turn score is {turn_score_b}')
    if turn_score_a > turn_score_b:
        print('Player A wins the round.')
        a_round_score = 1
        b_round_score = 0
    elif turn_score_b > turn_score_a:
        print('Player B wins the round.')
        a_round_score = 0
        b_round_score = 1
    else:
        print('The players tie this round.')
        a_round_score = 0
        b_round_score = 0
    return a_round_score, b_round_score


def play_turn(player_name):
    print(f'Player {player_name}\'s turn...')
    rolls = roll_dice(3)
    choice1 = choose_value(rolls)
    print(f'Player {player_name} rolls {rolls} and keeps {choice1}.')
    rolls = roll_dice(2)
    choice2 = choose_value(rolls)
    print(f'Player {player_name} rolls {rolls} and keeps {choice2}.')
    rolls = roll_dice(1)
    choice3 = choose_value(rolls)
    print(f'Player {player_name} rolls and keeps {choice3}.')
    choice_added = choice1 + choice2 + choice3

    return choice_added


def roll_dice(number_of_dice):
    return [randint(1, 6) for _ in range(number_of_dice)]


def choose_value(these_rolls):
    return max(these_rolls)


def print_game_results(rounds_won_a, rounds_won_b):
    print(f'\nGame Results:')
    if rounds_won_a == 1:
        print(f'Player A has won {rounds_won_a} round.')
    else:
        print(f'Player A has won {rounds_won_a} rounds.')

    if rounds_won_b == 1:
        print(f'Player B has won {rounds_won_b} round.')
    else:
        print(f'Player B has won {rounds_won_b} rounds.')

    if rounds_won_a > rounds_won_b:
        print(f'Player A wins the game.')
    elif rounds_won_b > rounds_won_a:
        print(f'Player B wins the game.')
    else:
        print(f'The players tie the game.')


main()
