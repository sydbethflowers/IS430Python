""" Using a dictionary, lookup ribbon colors based on the placement of a winner. """


def main():
    ribbon_name_dictionary = create_ribbon_dictionary()
    entry_as_string = input('Please enter place finished (1, 2, 3...): ')

    while entry_as_string != '':
        try:
            ribbon_placement = int(entry_as_string)
            ribbon_color = determine_ribbon_color(ribbon_placement, ribbon_name_dictionary)
            print(f'Ribbon Awarded: {ribbon_color}\n')
        except ValueError:
            print(f'An integer was expected. You entered {entry_as_string}.')
        entry_as_string = input('Please enter place finished (1, 2, 3...): ')

    print('\nThanks for playing.')


def create_ribbon_dictionary():
    ribbon_names = {
        1: 'Blue',
        2: 'Red',
        3: 'Orange',
        4: 'Gold',
        5: 'Green',
        6: 'Purple'
    }
    return ribbon_names


def determine_ribbon_color(ribbon_placement, ribbon_name_dictionary):
    if ribbon_placement < 1:
        ribbon_color = 'ERROR - Place must be greater than zero.'
    elif ribbon_placement > 7:
        ribbon_color = 'White'
    else:
        ribbon_color = ribbon_name_dictionary.get(ribbon_placement, f'Ribbon Awarded: {ribbon_placement}\n')

    return ribbon_color


main()
