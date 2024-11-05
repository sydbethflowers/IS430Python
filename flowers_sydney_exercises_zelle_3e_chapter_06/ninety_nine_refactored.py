"""Print the song 99 Bottles of Beer as adapted for a programming exercise."""


def main():
    song_title()
    beer_verse()
    last_line()


def song_title():
    print('99 Bottles of Beer')
    print('Traditional')
    print()


def beer_verse():
    for beers in range(99, 0, -1):
        print(f'{beers} bottles of beer on the wall, {beers} bottles of beer.')
        print(f'Take one down and pass it around, {beers - 1} bottles of beer on the wall.')
        print()


def last_line():
    print('No more bottles of beer on the wall, no more bottles of beer.')
    print('Go to the store and buy some more, 99 bottles of beer on the wall.')


main()
