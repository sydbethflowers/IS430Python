"""
Print registration renewal invoices for all vehicles.

Supports all subclasses of Vehicle.
"""

from my_vehicles_challenge import construct_vehicle_instance


def main():
    vehicles = get_vehicles()
    vehicles.sort(key=by_first_name)
    vehicles.sort(key=by_last_name)
    vehicles.sort(key=by_city)
    print_invoices(vehicles)


def get_vehicles():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    my_vehicles = []
    for line in infile:
        vehicle = construct_vehicle_instance(line)
        my_vehicles.append(vehicle)
    infile.close()
    return my_vehicles


def print_invoices(these_vehicles):
    invoices_printed = 0
    separator_line = f'\n\n{"-" * 45}'
    for vehicle in these_vehicles:
        title, name_and_address, detail = vehicle.get_invoice_content()
        print(separator_line)
        print(f'\n{title.upper()}')
        print()
        for line in name_and_address:
            print(line)
        print()
        for content_tuple in detail:
            caption, value = content_tuple
            print(f'{caption + ":":<20}    {value}')
        print()
        print(f'AMOUNT DUE: $ {vehicle.determine_annual_registration_fee():0.2f}')
        invoices_printed += 1

    print(separator_line)
    print(f'\n\n{invoices_printed} invoices have been printed.')


def by_first_name(vehicle_instance):
    return vehicle_instance.first_name


def by_last_name(vehicle_instance):
    return vehicle_instance.last_name


def by_city(vehicle_instance):
    return vehicle_instance.city


main()
