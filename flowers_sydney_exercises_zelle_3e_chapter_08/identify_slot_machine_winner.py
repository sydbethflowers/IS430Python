""" Reads a user input file and searches for three blue and two red strings in a line. """


def main():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r')
    line_count = 0
    match_found = False
    line = infile.readline()

    while line != '' and not match_found:
        line_count += 1
        colors_in_line = line.split()
        colors = []
        for color in colors_in_line:
            colors.append(color)
        colors_string = ' '.join(colors)
        red_count = colors.count('Red')
        blue_count = colors.count('Blue')
        if red_count == 3 and blue_count == 2:
            match_found = True
            print(f'\nWinner found on line {line_count}: {colors_string}')
        else:
            line = infile.readline()

    infile.close()

    if line == '':
        print(f'\nNo winning slot values found.\n{line_count} lines read from {infile_name}')


main()
