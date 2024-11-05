"""Demonstrate integer division."""


def main():
    dividend = int(input('Please enter an integer for the dividend: '))
    divisor = int(input('Please enter an integer for the quotient: '))
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(f"\nThe quotient is {quotient} and the remainder is {remainder}.")


main()
