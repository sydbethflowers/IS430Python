"""Counts color names in the slot machine file ignoring duplicate values on the same line."""
# Please DO NOT DISTRIBUTE exercise solutions


def main():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    color_count = {}

    for line in infile:
        slot_values = line.split()
        unique_slot_values = find_unique_slot_values(slot_values)
        for slot_value in unique_slot_values:
            color_count[slot_value] = color_count.get(slot_value, 0) + 1

    infile.close()

    these_keys = list(color_count.keys())
    these_keys.sort()

    print()
    print(f'{"COLOR":<10}{"COUNT":>7}')
    for this_key in these_keys:
        print(f'{this_key:<10}{color_count.get(this_key):>7,}')


def find_unique_slot_values(this_slot_value_list):
    these_unique_slot_values = []

    for value in this_slot_value_list:
        if value not in these_unique_slot_values:
            these_unique_slot_values.append(value)

    return these_unique_slot_values


main()
