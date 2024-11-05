"""Read a flexibly formatted file of number entries and accumulate the sum of these entries."""


def main():
    data_directory_name = 'data'
    input_file_name = input("Please enter the name of a file to be analyzed: ")
    infile_path_and_filename = f"{data_directory_name}/{input_file_name}"
    infile = open(infile_path_and_filename, 'r')
    line_count = 0
    entries_count = 0
    entries_sum = 0

    print(f'\nENTRIES:')
    for line in infile:
        line_count += 1
        entries = line.split()
        for entry in entries:
            entry_float = float(entry)
            print(f'{entry_float}')
            entries_count += line.count(entry)
            entries_sum += entry_float

    print(f'\n{line_count} lines were processed from input file: {input_file_name}')
    print(f'\n{entries_count} entries were processed.')
    print(f'\nThe accumulated total of the entries was {entries_sum:.3f}')

    infile.close()


main()
