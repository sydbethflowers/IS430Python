"""Demonstrate mixed type division and accumulator pattern."""


def main():
    accumulator = 0.0
    pairs_to_collect = int(input('Please enter the quantity of number pairs that you wish to enter: '))


    for i in range(1, pairs_to_collect + 1):
            print(f'Now collecting number pair {i} of {pairs_to_collect}... ')
            dividend = float(input('Please enter an float for the dividend: '))
            divisor = int(input('Please enter an integer for the divisor: '))
            quotient = dividend / divisor
            print(f'The quotient is {quotient:.3f}.')
            accumulator += quotient
            print()

    rounded_accumulator = round(accumulator, 3)
    print(f'The accumulated sum of the remainders is {rounded_accumulator}.')


main()
