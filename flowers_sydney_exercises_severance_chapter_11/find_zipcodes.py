"""
Extracts matches to 4 different zip code patterns from an input file.

Matched patterns include:
99999 (traditional 5-digit zip code)
99999-9999 (more modern zip+4 format
"""

import re


def main():
    print('Extract matches to 4 different zip code patterns from an input file.\n')
    data_directory_name = 'data'
    infile_name = input('Please enter the input file name:')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf8')
    zipcodes_found = []

    for line in infile:
        zipcodes = re.findall(r'\d{5}-\d{4}|\d{5}', line)
        zipcodes_found.extend(zipcodes)

    infile.close()

    if not zipcodes_found:
        print('\nNo zip codes were found in the input file.')
    else:
        print('\nThe following zip codes were found in the input file:')
        for zipcode in zipcodes_found:
            print(f'    {zipcode}')


main()
