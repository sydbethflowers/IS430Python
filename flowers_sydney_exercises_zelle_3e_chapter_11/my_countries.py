"""
Module contains the Country class and related test code.
"""
# Please DO NOT DISTRIBUTE exercise solutions

from dataclasses import dataclass
from is430_unit_test_helpers import assert_equal


@dataclass
class Country:
    country_name: str
    population: int
    area_in_square_miles: int

    def calculate_population_density_per_square_mile(self):
        return round(float(self.population) / float(self.area_in_square_miles))


def main():
    print('Unit testing output follows...')

    print('\nTest Case #1: Test constructor')
    expected_country_name = 'Australia'
    expected_population = 25273752
    expected_area_in_square_miles = 2969907
    c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    assert_equal(expected_country_name, c1.country_name)
    assert_equal(expected_population, c1.population)
    assert_equal(expected_area_in_square_miles, c1.area_in_square_miles)

    print('\nTest Case #2: Test calculate_population_density_per_square_mile method')
    expected_country_name = 'Australia'
    expected_population = 25273752
    expected_area_in_square_miles = 2969907
    expected_population_density_per_square_mile = 9
    c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    actual_population_density_per_square_mile = c1.calculate_population_density_per_square_mile()
    assert_equal(expected_population_density_per_square_mile, actual_population_density_per_square_mile)


if __name__ == '__main__':
    main()
