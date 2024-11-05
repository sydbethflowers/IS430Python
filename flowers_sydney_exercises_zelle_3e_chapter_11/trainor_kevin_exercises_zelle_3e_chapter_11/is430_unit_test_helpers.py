"""
Module contains simple unit testing helper code for use in Kevin Trainor's IS430 course.
"""

PASSED = 'Passed'
FAILED = 'Failed'


def assert_equal(expected, actual):
    if expected == actual:
        print(PASSED)
    else:
        print(FAILED)
        print(f'EXPECTED: {expected}')
        print(f'ACTUAL: {actual}')


def assert_equal_float(expected, actual, acceptable_error):
    if not isinstance(expected, float):
        raise TypeError(f'Expected value is not a float. It is a {type(expected)}.')
    if not isinstance(actual, float):
        raise TypeError(f'Actual value is not a float. It is a {type(actual)}.')
    if not isinstance(acceptable_error, float):
        raise TypeError(f'Acceptable error value is not a float. It is a {type(acceptable_error)}.')
    actual_error = expected - actual
    abs_actual_error = abs(actual_error)
    abs_acceptable_error = abs(acceptable_error)
    if abs_actual_error <= abs_acceptable_error:
        print(PASSED)
    else:
        print(FAILED)
        print(f'EXPECTED: {expected}')
        print(f'ACTUAL: {actual}')
        print(f'ACCEPTABLE ERROR: {acceptable_error}')
        print(f'ACTUAL ERROR: {actual_error}')


def main():
    print('Unit testing output follows...')

    print('\nTest Case #1: assert_equal with strings')
    expected = 'hi mom'
    actual = 'hi mom'
    assert_equal(expected, actual)

    print('\nTest Case #2: assert_equal with ints')
    expected = 257
    actual = 257
    assert_equal(expected, actual)

    print('\nTest Case #3: assert_equal with booleans')
    expected = False
    actual = False
    assert_equal(expected, actual)

    print('\nTest Case #4: assert_equal with lists')
    expected = [1, 2, 3, 4]
    actual = [1, 2, 3, 4]
    assert_equal(expected, actual)

    print('\nTest Case #4: assert_equal with tuples')
    expected = (1, 2, 3, 4)
    actual = (1, 2, 3, 4)
    assert_equal(expected, actual)

    print('\nTest Case #4: assert_equal_float with floats')
    expected = 7.7
    actual = 1.1 + 2.2 + 4.4
    acceptable_error = 0.001
    assert_equal_float(expected, actual, acceptable_error)


if __name__ == '__main__':
    main()
