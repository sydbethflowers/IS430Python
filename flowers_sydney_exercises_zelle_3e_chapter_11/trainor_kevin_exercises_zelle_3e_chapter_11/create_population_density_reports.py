"""print a report of country records from a file in two different sort orders."""
# Please DO NOT DISTRIBUTE exercise solutions

from my_countries import Country


def main():
    countries = get_countries()

    countries.sort(key=by_country_name)
    print_report(countries, 'BY COUNTRY NAME')

    countries.sort(key=by_population_density_per_square_mile, reverse=True)
    print_report(countries, 'BY DESCENDING POPULATION DENSITY PER SQUARE MILE')


def get_countries():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    my_countries = []
    for line in infile:
        country_name, population_as_string, area_in_miles_as_string = line.split(';')
        my_countries.append(
            Country(country_name, int(population_as_string), int(area_in_miles_as_string))
        )
    infile.close()
    return my_countries


def print_report(these_countries, report_title):
    print()
    print()
    print(f'{report_title:^65}')
    print()
    print(f'{"Country":<20}{"Population":>15}{"Area":>15}{"Density":>15}')
    print(f'{"":<20}{"":>15}{"(SQMI)":>15}{"(/SQMI)":>15}')

    for country in these_countries:
        print(f'{country.country_name:<20}'
              f'{country.population:>15,}'
              f'{country.area_in_square_miles:>15,}'
              f'{country.calculate_population_density_per_square_mile():15,}')


def by_country_name(a_country_instance):
    return a_country_instance.country_name


def by_population_density_per_square_mile(a_country_instance):
    return a_country_instance.calculate_population_density_per_square_mile()


main()
