""" Demonstrate flexible user interaction to enter as many inputs as desired using while. """


def main():
    print('Welcome to Flexible Float Adding Machine. \n')
    entry_count = 0
    sum_of_entries = 0
    entry_as_string = input('Please enter a float value to be added (<Enter> to stop): ')

    while entry_as_string != '':
        entry = float(entry_as_string)
        entry_count += 1
        sum_of_entries += entry
        entry_as_string = input('Please enter a float value to be added (<Enter> to stop): ')

    if entry_count == 0:
        print('\nNo entries were provided.')
    else:
        print(f'\nThe sum of these {entry_count} entries is {sum_of_entries:.2f}')


main()
