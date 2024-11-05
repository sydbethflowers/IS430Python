""" Demonstrates processing data records."""


def main():
    data_directory_name = 'data'

    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r')

    outfile_name = 'name_badges_' + infile_name
    outfile_path_and_name = f'{data_directory_name}/{outfile_name}'
    outfile = open(outfile_path_and_name, 'w', encoding='utf-8')
    line_count = 0
    line = infile.readline()

    while line != '':
        line_count += 1
        first_name, last_name = line.split()
        content = f'{last_name.upper()},{first_name}'
        print(content, file=outfile)
        line = infile.readline()

    infile.close()

    print(f'\n{line_count} records were read from {infile_name}')
    print(f'\n{line_count} records were written to {outfile_name}')


main()
