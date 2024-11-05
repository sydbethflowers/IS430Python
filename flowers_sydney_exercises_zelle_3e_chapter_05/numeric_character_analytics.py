"""Analyze the quantity of numeric characters in a user given sentence."""


def main():
    numeric_chars = "0123456789"
    line = input('Please enter a line of text to be analyzed: ')
    words = line.split()

    print()
    for word in words:
        numeric_char_count = 0
        for char in numeric_chars:
            numeric_char_count += word.count(char)
        print(f'"{word}" contains {numeric_char_count} numeric characters.')

    print(f'\n{len(words)} words were analyzed.')


main()
