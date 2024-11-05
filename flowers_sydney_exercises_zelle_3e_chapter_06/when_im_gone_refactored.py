"""Print the song When I'm Gone by Phil Ochs."""
# text from https://celebratingphilochs.com/when-im-gone/


def main():
    write_title_and_credit()
    verse_1_and_8()
    verse_2()
    verse_3()
    verse_4()
    verse_5()
    verse_6()
    verse_7()
    verse_1_and_8()
    finale()


def write_title_and_credit():
    print('When I\'m Gone by Phil Ochs')
    print()


def verse_1_and_8():
    print('There’s no place in this world where I’ll belong when I’m gone')
    print('And I won’t know the right from the wrong when I’m gone')
    print('And you won’t find me singin’ on this song when I’m gone')
    repeated_line()


def repeated_line():
    print('So I guess I’ll have to do it while I’m here')


def verse_2():
    print()
    print('And I won’t feel the flowing of the time when I’m gone')
    print('All the pleasures of love will not be mine when I’m gone')
    print('My pen won’t pour a lyric line when I’m gone')
    repeated_line()
    print()


def verse_3():
    print('And I won’t breathe the bracing air when I’m gone')
    print('And I can’t even worry ’bout my cares when I’m gone')
    print('Won’t be asked to do my share when I’m gone')
    repeated_line()
    print()


def verse_4():
    print('And I won’t be running from the rain when I’m gone')
    print('And I can’t even suffer from the pain when I’m gone')
    print('Can’t say who’s to praise and who’s to blame when I’m gone')
    repeated_line()
    print()


def verse_5():
    print('Won’t see the golden of the sun when I’m gone')
    print('And the evenings and the mornings will be one when I’m gone')
    print('Can’t be singing louder than the guns when I’m gone')
    repeated_line()
    print()


def verse_6():
    print('All my days won’t be dances of delight when I’m gone')
    print('And the sands will be shifting from my sight when I’m gone')
    print('Can’t add my name into the fight while I’m gone')
    repeated_line()
    print()


def verse_7():
    print('And I won’t be laughing at the lies when I’m gone')
    print('And I can’t question how or when or why when I’m gone')
    print('Can’t live proud enough to die when I’m gone')
    repeated_line()
    print()


def finale():
    print('So I guess I’ll have to do it, I guess I’ll have to do it')
    print('Guess I’ll have to do it while I’m here')


main()
