""" module of my land mammals """

from dataclasses import dataclass
from is430_unit_test_helpers import assert_equal, assert_equal_int


@dataclass
class LandMammal:
    mammal_name: str
    minimum_mass_in_pounds: int
    maximum_mass_in_pounds: int

    def calculate_range_of_mass_in_pounds(self):
        return self.maximum_mass_in_pounds - self.minimum_mass_in_pounds


def main():
    print('Unit testing output as follows...')

    print('\nTest Case: Test constructor')
    expected_mammal_name = 'African Elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    s1 = LandMammal(expected_mammal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    assert_equal(expected_mammal_name, s1.mammal_name)
    assert_equal_int(expected_minimum_mass_in_pounds, s1.minimum_mass_in_pounds, 0)
    assert_equal_int(expected_maximum_mass_in_pounds, s1.maximum_mass_in_pounds, 0)

    print('\nTest Case: Test calculate_range_of_mass_in_pounds method')
    expected_mammal_name = 'African Elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    expected_range_of_mass_in_pounds = 14000
    s1 = LandMammal(expected_mammal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    assert_equal_int(expected_range_of_mass_in_pounds, s1.calculate_range_of_mass_in_pounds(), 0)


if __name__ == '__main__':
    main()
