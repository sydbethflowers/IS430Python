""" Demonstrates recovery from bad user input using while. """


def main():
    print('Welcome to Flexible Float Adding Machine. \n')
    entry_count = 0
    sum_of_entries = 0
    entry_as_string = input('Please enter a float value to be added (<Enter> to stop): ')

    while entry_as_string != '':
        try:
            entry = float(entry_as_string)
            entry_count += 1
            sum_of_entries += entry
        except ValueError:
            print(f'A float value was expected. You entered {entry_as_string}.')
        entry_as_string = input('Please enter a float value to be added (<Enter> to stop): ')

    if entry_count == 0:
        print('\nNo entries were provided.')
    else:
        print(f'\nThe sum of these {entry_count} entries is {sum_of_entries:.2f}')


main()
