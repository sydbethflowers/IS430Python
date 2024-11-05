""" Simulate the 2-player dice game called, Going to Boston with improvements. """

import random
import string


def main():
    print('Welcome to Going to Boston.\n')
    rounds_to_play = get_number_of_rounds()
    num_players = get_number_of_players()

    rounds_won = {player: 0 for player in player_name_create(num_players)}
    for i in range(1, rounds_to_play + 1):
        round_scores = play_round(i, rounds_won.keys())
        for player, score in round_scores.items():
            rounds_won[player] += score

    if rounds_to_play != 0:
        print_game_results(rounds_won)


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
                print(f'A value between 1 and 1000 was expected. You entered {rounds}.')
                rounds_as_string = input('Please enter the number of rounds to be played (<Enter> to stop): ')
        except ValueError:
            print(f'An integer was expected. You entered {rounds_as_string}.')
            rounds_as_string = input('Please enter the number of rounds to be played (<Enter> to stop): ')

    return rounds


def get_number_of_players():
    MAX_PLAYERS = 26
    MIN_PLAYERS = 2
    valid_players = False
    players_as_string = prompt_for_number_of_players()

    while not valid_players:
        if players_as_string == '' or players_as_string == '0':
            print('No players were entered. Come play again soon.')
            return exit(0)
        try:
            players = int(players_as_string)
            if MIN_PLAYERS <= players < MAX_PLAYERS:
                valid_players = True
            else:
                print(f'A value between 2 and 26 was expected. You entered {players}.')
                players_as_string = input('Please enter the number of players participating: ')
        except ValueError:
            print(f'An integer was expected. You entered {players_as_string}.')
            players_as_string = input('Please enter the number of players participating: ')

    return players


def prompt_for_number_of_rounds():
    return input('Please enter the number of rounds to be played (<Enter> to stop): ')


def prompt_for_number_of_players():
    return input('Please enter the number of players participating: ')


def player_name_create(num_players):
    players = []
    for _ in range(num_players):
        player_letter = random.choice(string.ascii_uppercase)
        players.append(player_letter)
    return players


def play_round(round_number, players):
    print(f'\nPlaying Round {round_number}:')
    round_scores = {player: play_turn(player) for player in players}

    max_score = max(round_scores.values())
    winners = [player for player, score in round_scores.items() if score == max_score]

    for player in players:
        if player in winners:
            print(f'Player {player} wins the round.')
            round_scores[player] = 1
        else:
            round_scores[player] = 0

    return round_scores


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
    return [random.randint(1, 6) for _ in range(number_of_dice)]


def choose_value(these_rolls):
    return max(these_rolls)


def print_game_results(rounds_won):
    print(f'\nGame Results:')
    for player, rounds in rounds_won.items():
        if rounds == 1:
            print(f'Player {player} has won {rounds} round.')
        else:
            print(f'Player {player} has won {rounds} rounds.')

    max_wins = max(rounds_won.values())
    winners = [player for player, rounds in rounds_won.items() if rounds == max_wins]

    if len(winners) == 1:
        print(f'Player {winners[0]} wins the game.')
    else:
        print(f'The game is a tie between: Players {", ".join(winners)}.')


main()
