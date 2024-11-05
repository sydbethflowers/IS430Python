"""Build and print a Mad Lib sentence."""


def main():
    first_word = input('Please enter the first word: ')
    second_word = input('Please enter the second word: ')
    third_word = input('Please enter the third word: ')
    fourth_word = input('Please enter the fourth word: ')
    fifth_word = input('Please enter the fifth word: ')
    sixth_word = input('Please enter the sixth word: ')

    print(first_word, second_word, third_word, fourth_word, fifth_word, sixth_word + '.')

main()
