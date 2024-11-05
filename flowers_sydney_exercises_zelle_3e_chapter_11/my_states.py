"""
Module contains the State class and related test code.
"""

from dataclasses import dataclass
from is430_unit_test_helpers import assert_equal, assert_equal_float


@dataclass
class State:
    state_name: str
    land_area_in_square_miles: float
    water_area_in_square_miles: float

    def calculate_total_area_in_square_miles(self):
        return self.land_area_in_square_miles + self.water_area_in_square_miles


def main():
    print('Unit testing output follows...')

    print('\nTest Case #1: Test constructor')
    expected_state_name = 'Alaska'
    expected_land_area_in_square_miles = 570640.95
    expected_water_area_in_square_miles = 94743.10
    s1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    assert_equal(expected_state_name, s1.state_name)
    assert_equal(expected_land_area_in_square_miles, s1.land_area_in_square_miles)
    assert_equal(expected_water_area_in_square_miles, s1.water_area_in_square_miles)

    print('\nTest Case #2: Test calculate_total_area_in_square_miles method')
    expected_state_name = 'Alaska'
    expected_land_area_in_square_miles = 570640.95
    expected_water_area_in_square_miles = 94743.10
    expected_total_area_in_square_miles = 665384.05
    s1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    assert_equal_float(expected_total_area_in_square_miles, s1.calculate_total_area_in_square_miles(), 0.0001)


if __name__ == '__main__':
    main()
