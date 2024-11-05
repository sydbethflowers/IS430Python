"""
Print mammal reports in two different sort orders

By Mammal Name
By Descending Range of Mass in Pounds
"""

from my_land_mammals import LandMammal


def main():
    mammals = get_mammals()

    mammals.sort(key=by_mammal_name)
    print_report(mammals, 'BY LAND MAMMAL NAME')

    mammals.sort(key=by_range_of_mass_in_pounds, reverse=True)
    print_report(mammals, 'BY DESCENDING RANGE OF MASS IN POUNDS')


def get_mammals():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf8')
    my_mammals = []
    for line in infile:
        mammal_name, minimum_mass_in_pounds_string, maximum_mass_in_pounds_string = line.split(',')
        my_mammals.append(
            LandMammal(mammal_name, int(minimum_mass_in_pounds_string), int(maximum_mass_in_pounds_string))
        )
    infile.close()
    return my_mammals


def print_report(these_mammals, report_title):
    print()
    print()
    print(f'{report_title:^60}')
    print()
    print(f'{"Land Mammal":<20}{"Minimum Mass":>15}{"Maximum Mass":>15}{"Range of Mass":>15}')
    print(f'{"Name":<20}{"in Pounds":>15}{"in Pounds":>15}{"in Pounds":>15}')

    for mammal in these_mammals:
        print(f'{mammal.mammal_name:<20}{mammal.minimum_mass_in_pounds:>15,}{mammal.maximum_mass_in_pounds:>15,}'
              f'{mammal.calculate_range_of_mass_in_pounds():>15,}')


def by_mammal_name(a_mammal_instance):
    return a_mammal_instance.mammal_name


def by_range_of_mass_in_pounds(a_mammal_instance):
    return a_mammal_instance.calculate_range_of_mass_in_pounds()


main()
