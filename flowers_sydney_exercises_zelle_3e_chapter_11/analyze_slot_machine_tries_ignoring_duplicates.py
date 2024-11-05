"""Counts number of rows a color appears in."""


def main():
    data_directory_name = 'data'
    infile_name = input('Please enter your input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r')
    color_count = {}

    for line in infile:
        slot_values = line.split()
        unique_values = set(slot_values)
        for slot_value in unique_values:
            color_count[slot_value] = color_count.get(slot_value, 0) + 1

    infile.close()

    these_keys = list(color_count.keys())
    these_keys.sort()

    print()
    print(f'{"COLOR":<10}{"COUNT":<7}')
    for this_key in these_keys:
        print(f'{this_key:<10}{color_count[this_key]:<7,}')


main()
