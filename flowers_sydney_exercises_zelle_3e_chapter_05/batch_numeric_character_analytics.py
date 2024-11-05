"""Read an input file. Analyze words on each line, counting numeric characters."""


def main():
    numeric_chars = "0123456789"
    data_directory_name = 'data'
    input_file_name = input("Please enter the name of a file to be analyzed: ")
    infile_path_and_filename = f"{data_directory_name}/{input_file_name}"
    infile = open(infile_path_and_filename, 'r')
    line_count = 0

    for line in infile:
        print(f'\nAnalyzing: {line[:-1]}')
        line_count += 1
        words = line.split()

        for word in words:
            numeric_char_count = 0
            for char in numeric_chars:
                numeric_char_count += word.count(char)
            print(f'"{word}" contains {numeric_char_count} numeric characters.')

        print(f'{len(words)} words were analyzed.')

    print(f'\n{line_count} lines were analyzed from the file: {input_file_name}')

    infile.close()


main()
