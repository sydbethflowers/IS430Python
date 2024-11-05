"""
Using a dictionary, lookup ribbons to be awarded to race finishers based upon
a series of place values entered by the user.
"""
# Please DO NOT DISTRIBUTE exercise solutions


def main():
    race_ribbon_dictionary = create_ribbon_dictionary()
    entry_as_string = input('Please enter place finished (1, 2, 3...): ')

    while entry_as_string != '':
        try:
            place = int(entry_as_string)
            ribbon = determine_race_ribbon(place, race_ribbon_dictionary)
            print(f'Ribbon Awarded: {ribbon}\n')
        except ValueError:
            print(f'An integer value was expected. You entered {entry_as_string}')
        entry_as_string = input('Please enter place finished (1, 2, 3...): ')

    print('\nThanks for playing.')


def determine_race_ribbon(place_number, race_ribbons):
    if place_number < 1:
        ribbon = 'ERROR - Place must be greater than zero.'
    else:
        ribbon = race_ribbons.get(place_number, 'White')
    return ribbon


def create_ribbon_dictionary():
    ribbon_dictionary = {
        1: 'Blue',
        2: 'Red',
        3: 'Orange',
        4: 'Gold',
        5: 'Green',
        6: 'Purple'
    }
    return ribbon_dictionary


main()
