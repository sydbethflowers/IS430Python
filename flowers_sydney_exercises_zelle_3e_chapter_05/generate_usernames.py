"""Generates a file of username assignments from a file of natural-order names."""


def main():
    line_count = 0
    data_directory_name = 'data'
    input_file_name = input("Please enter the name of a file to be analyzed: ")
    infile_path_and_filename = f"{data_directory_name}/{input_file_name}"
    infile = open(infile_path_and_filename, 'r')
    output_file_name = 'username_assignments.txt'
    outfile_path_and_filename = f"{data_directory_name}/{output_file_name}"
    outfile = open(outfile_path_and_filename, 'w', encoding='utf-8')

    for line in infile:
        line_count += 1
        first_name, last_name = line.split()
        user_name = f'{first_name[:1]}{last_name[:7]}'
        user_name = user_name.lower()
        names = f'{first_name} {last_name},{user_name}'
        print(names, file=outfile)

    print(f'\n{line_count} lines were processed from input file: {input_file_name}')
    print(f'\nCreated username assignments file as: {output_file_name}')

    infile.close()
    outfile.close()


main()
