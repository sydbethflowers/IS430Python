"""Convert a measurement in pounds to stones."""


def main():
    pounds = eval(input('Please enter a measurement in pounds: '))
    stones = (pounds *  0.0714286)
    print(stones)


main()
