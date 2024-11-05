"""  Count the number of lines in which the word 'whale' is found in different contexts. """

import re


def main():
    print('Count lines that contain the string "whale" in the input file.\n')
    data_directory_name = 'data'
    infile_name = input('Please enter your input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    line_count_contain = 0
    line_count_begin = 0
    line_count_end = 0
    line_count_begin_or_end = 0
    line_count_begin_and_end = 0

    for line in infile:
        if re.search(r'whale', line, re.IGNORECASE):
            line_count_contain += 1

        if re.search(r'^whale', line, re.IGNORECASE):
            line_count_begin += 1

        if re.search(r'whale$', line, re.IGNORECASE):
            line_count_end += 1

        if re.search(r'^whale|whale$', line, re.IGNORECASE):
            line_count_begin_or_end += 1

        if re.search(r'^whale', line, re.IGNORECASE) and re.search(r'whale$', line, re.IGNORECASE):
            line_count_begin_and_end += 1

    infile.close()

    print(f'\n{line_count_contain} lines in file contain target string.')
    print(f'\n{line_count_begin} lines in file contain target string at the beginning.')
    print(f'\n{line_count_end} lines in file contain target string at the end.')
    print(f'\n{line_count_begin_or_end} lines in file contain target string at the beginning or the end.')
    print(f'\n{line_count_begin_and_end} lines in file contain target string at the beginning and the end.')


main()
