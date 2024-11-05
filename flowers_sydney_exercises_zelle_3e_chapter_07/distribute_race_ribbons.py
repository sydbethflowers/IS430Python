""" A program that determines which ribbon a child earns."""


def main():
    placement = int(input('Please enter place finished (1, 2, 3...): '))
    place_ribbon = lookup_place_ribbon(placement)
    print(f'\nRibbon Awarded: {place_ribbon}')


def lookup_place_ribbon(placement):
    if placement == 1:
        place_ribbon = 'Blue'
    elif placement == 2:
        place_ribbon = 'Red'
    elif placement == 3:
        place_ribbon = 'Orange'
    elif placement == 4:
        place_ribbon = 'Gold'
    elif placement == 5:
        place_ribbon = 'Green'
    elif placement == 6:
        place_ribbon = 'Purple'
    elif placement >= 7:
        place_ribbon = 'White'
    else:
        place_ribbon = 'ERROR - Place must be greater than zero'
    return place_ribbon


main()
