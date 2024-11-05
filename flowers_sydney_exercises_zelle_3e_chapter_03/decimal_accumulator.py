"""Demonstrate decimal type and accumulator pattern."""
from decimal import Decimal


def main():
    accumulated_sum = Decimal('0')
    pairs_to_collect = int(input('Please enter the quantity of number pairs that you wish to enter: '))


    for i in range(1, pairs_to_collect + 1):
            value = Decimal(input(f'Please enter decimal value {i} of {pairs_to_collect}: '))
            accumulated_sum += value


    print(f'The accumulated sum of the remainders is {accumulated_sum}.')


main()
