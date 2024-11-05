"""Find the highest value from a given file."""


from sys import maxsize

MAX_INT_VALUE = maxsize


def main():
    line_count = 0
    highest_entry_so_far = -maxsize - 1

    data_directory_name = 'data'
    input_file_name = input('Please enter the name of the input file: ')
    infile_path_and_filename = f'{data_directory_name}/{input_file_name}'
    infile = open(infile_path_and_filename, 'r')

    for line in infile:
        line_count += 1
        entry = int(line)
        if entry > highest_entry_so_far:
            highest_entry_so_far = entry

    if line_count == 0:
        print('\nThe input file was empty. No values could be analyzed.')
    else:
        print(f'\nThere are {line_count} entries in the input list.')
        print(f'The highest value is {highest_entry_so_far}.')


main()
