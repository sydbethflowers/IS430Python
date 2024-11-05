"""
Module contains the Vehicle hierarchy of classes and related code.

Includes subclasses:
    Car
    Truck
    Motorcycle
    Snowmobile
Includes simple factory method construct_vehicle_instance
"""
from dataclasses import dataclass
from is430_unit_test_helpers import assert_equal, assert_equal_float, PASSED


@dataclass
class Vehicle:
    """A super-class to represent a vehicle"""
    first_name: str
    last_name: str
    street_address_1: str
    street_address_2: str
    city: str
    state: str
    zipcode: str
    make: str
    model: str
    year: int
    color: str
    vehicle_id: str

    def get_invoice_content(self):
        title = 'Registration Renewal Invoice'

        name_and_address = []
        name_and_address.append(f'{self.first_name} {self.last_name}')
        name_and_address.append(self.street_address_1)
        if self.street_address_2:
            name_and_address.append(self.street_address_2)
        name_and_address.append(f'{self.city}, {self.state} {self.zipcode}')

        detail = [
            ('Make', self.make),
            ('Model', self.model),
            ('Year', f'{self.year}'),
            ('Color', self.color),
            ('Vehicle ID', self.vehicle_id)
        ]
        return title, name_and_address, detail


@dataclass
class Car(Vehicle):
    """A subclass of Vehicle to represent a car"""
    fuel_type: str

    def determine_annual_registration_fee(self):
        """
        Determines annual registration fee for a car.

        :return: annual_registration_fee (float)
        """
        if self.fuel_type == 'Electric':
            annual_fee = 100.00
        elif self.fuel_type == 'Hybrid':
            annual_fee = 200.00
        elif self.fuel_type == 'Fossil':
            annual_fee = 300.00
        else:
            raise ValueError(f'Expected fuel type of Electric, Hybrid, or Fossil. This value is {self.fuel_type}.')
        return annual_fee

    def get_invoice_content(self):
        title, name_and_address, detail = super().get_invoice_content()
        title = f'Car {title}'
        detail.append(('Fuel Type', self.fuel_type))
        return title, name_and_address, detail


@dataclass
class Truck(Vehicle):
    """A subclass of Vehicle to represent a truck"""
    gross_weight: int

    def determine_annual_registration_fee(self):
        """
        determines annual registration fee for a truck.

        :return: annual_registration_fee (float)
        """
        if self.gross_weight < 14001:
            annual_fee = 400.00
        else:
            annual_fee = 700.00
        return annual_fee

    def get_invoice_content(self):
        title, name_and_address, detail = super().get_invoice_content()
        title = f'Truck {title}'
        detail.append(('Gross Weight', f'{self.gross_weight:,}'))
        return title, name_and_address, detail



@dataclass
class Motorcycle(Vehicle):
    """A subclass of Vehicle to represent a motorcycle"""
    displacement_in_ccs: int

    def determine_annual_registration_fee(self):
        """
        determines annual registration fee for a motorcycle.

        :return: annual_registration_fee (float)
        """
        if self.displacement_in_ccs < 1000:
            annual_fee = 75.00
        else:
            annual_fee = 150.00
        return annual_fee

    def get_invoice_content(self):
        title, name_and_address, detail = super().get_invoice_content()
        title = f'Motorcycle {title}'
        detail.append(('Displacement in ccs', f'{self.displacement_in_ccs:,}'))
        return title, name_and_address, detail


@dataclass
class Snowmobile(Vehicle):
    """A subclass of Vehicle to represent a snowmobile"""

    def determine_annual_registration_fee(self):
        """
        determines annual registration fee for a snowmobile.

        :return: annual_registration_fee (float)
        """
        annual_fee = 45.00
        return annual_fee

    def get_invoice_content(self):
        title, name_and_address, detail = super().get_invoice_content()
        title = f'Snowmobile {title}'
        return title, name_and_address, detail


def construct_vehicle_instance(vehicle_record):
    if vehicle_record.startswith('Car'):
        vehicle = construct_car_instance(vehicle_record)
    elif vehicle_record.startswith('Truck'):
        vehicle = construct_truck_instance(vehicle_record)
    elif vehicle_record.startswith('Motorcycle'):
        vehicle = construct_motorcycle_instance(vehicle_record)
    elif vehicle_record.startswith('Snowmobile'):
        vehicle = construct_snowmobile_instance(vehicle_record)
    else:
        raise ValueError(f'Car, Truck, Motorcycle, or Snowmobile was expected. This line starts with: {vehicle_record[0:10]}')
    return vehicle


def construct_car_instance(record):
    record = record.strip()
    data_fields = record.split(',')
    vehicle_type, first_name, last_name, street_address_1, street_address_2 = data_fields[0:5]
    city, state, zipcode, make, model, year, color, vehicle_id, fuel_type = data_fields[5:]
    vehicle = Car(first_name,
                  last_name,
                  street_address_1,
                  street_address_2,
                  city,
                  state,
                  zipcode,
                  make,
                  model,
                  int(year),
                  color,
                  vehicle_id,
                  fuel_type)
    return vehicle


def construct_truck_instance(record):
    record = record.strip()
    data_fields = record.split(',')
    vehicle_type, first_name, last_name, street_address_1, street_address_2 = data_fields[0:5]
    city, state, zipcode, make, model, year, color, vehicle_id, gross_weight = data_fields[5:]
    vehicle = Truck(first_name,
                    last_name,
                    street_address_1,
                    street_address_2,
                    city,
                    state,
                    zipcode,
                    make,
                    model,
                    int(year),
                    color,
                    vehicle_id,
                    int(gross_weight))
    return vehicle


def construct_motorcycle_instance(record):
    record = record.strip()
    data_fields = record.split(',')
    vehicle_type, first_name, last_name, street_address_1, street_address_2 = data_fields[0:5]
    city, state, zipcode, make, model, year, color, vehicle_id, displacement_in_ccs = data_fields[5:]
    vehicle = Motorcycle(first_name,
                    last_name,
                    street_address_1,
                    street_address_2,
                    city,
                    state,
                    zipcode,
                    make,
                    model,
                    int(year),
                    color,
                    vehicle_id,
                    int(displacement_in_ccs))
    return vehicle


def construct_snowmobile_instance(record):
    record = record.strip()
    data_fields = record.split(',')
    vehicle_type, first_name, last_name, street_address_1, street_address_2 = data_fields[0:5]
    city, state, zipcode, make, model, year, color, vehicle_id = data_fields[5:]
    vehicle = Snowmobile(first_name,
                    last_name,
                    street_address_1,
                    street_address_2,
                    city,
                    state,
                    zipcode,
                    make,
                    model,
                    int(year),
                    color,
                    vehicle_id)
    return vehicle


def main():
    print('Unit testing output follows...')

    # common unit testing variables for all vehicle types
    expected_first_name = 'Maria'
    expected_last_name = 'Gonzalez'
    expected_street_address_1 = '401 Splendid Way'
    expected_street_address_2 = 'Unit A'
    expected_city = 'Glenview'
    expected_state = 'IL'
    expected_zipcode = '60025'
    expected_make = 'American Auto Company'
    expected_model = 'Spirit'
    expected_year = 2020
    expected_color = 'White'
    expected_vehicle_id = 'VEH1234567890'
    expected_title = 'Registration Renewal Invoice'
    expected_name_and_address = [
        'Maria Gonzalez',
        '401 Splendid Way',
        'Unit A',
        'Glenview, IL 60025'
    ]
    expected_detail = [
        ('Make', expected_make),
        ('Model', expected_model),
        ('Year', str(expected_year)),
        ('Color', expected_color),
        ('Vehicle ID', expected_vehicle_id)
    ]

    print('\nTest Case: Test Vehicle constructor')
    vehicle_1 = Vehicle(expected_first_name,
                        expected_last_name,
                        expected_street_address_1,
                        expected_street_address_2,
                        expected_city,
                        expected_state,
                        expected_zipcode,
                        expected_make,
                        expected_model,
                        int(expected_year),
                        expected_color,
                        expected_vehicle_id)
    assert_equal(expected_first_name, vehicle_1.first_name)
    assert_equal(expected_last_name, vehicle_1.last_name)
    assert_equal(expected_street_address_1, vehicle_1.street_address_1)
    assert_equal(expected_street_address_2, vehicle_1.street_address_2)
    assert_equal(expected_city, vehicle_1.city)
    assert_equal(expected_state, vehicle_1.state)
    assert_equal(expected_zipcode, vehicle_1.zipcode)
    assert_equal(expected_make, vehicle_1.make)
    assert_equal(expected_model, vehicle_1.model)
    assert_equal(expected_year, vehicle_1.year)
    assert_equal(expected_color, vehicle_1.color)
    assert_equal(expected_vehicle_id, vehicle_1.vehicle_id)

    print('\nTest Case: Test Vehicle get_invoice_content method')
    vehicle_1 = Vehicle(expected_first_name,
                        expected_last_name,
                        expected_street_address_1,
                        expected_street_address_2,
                        expected_city,
                        expected_state,
                        expected_zipcode,
                        expected_make,
                        expected_model,
                        int(expected_year),
                        expected_color,
                        expected_vehicle_id)
    actual_invoice_content = vehicle_1.get_invoice_content()
    actual_title, actual_name_and_address, actual_detail = actual_invoice_content
    assert_equal(expected_title, actual_title)
    assert_equal(expected_name_and_address, actual_name_and_address)
    assert_equal(expected_detail, actual_detail)

    # common unit testing variables for the Car subtype
    expected_year = 2022
    expected_color = 'Green'
    expected_vehicle_id = 'CAR123456789'

    print('\nTest Case: Test Car constructor')
    expected_fuel_type = 'Electric'
    expected_make = 'Nissan'
    expected_model = 'Leaf'
    car_1 = Car(expected_first_name,
                expected_last_name,
                expected_street_address_1,
                expected_street_address_2,
                expected_city,
                expected_state,
                expected_zipcode,
                expected_make,
                expected_model,
                expected_year,
                expected_color,
                expected_vehicle_id,
                expected_fuel_type)
    assert_equal(expected_first_name, car_1.first_name)
    assert_equal(expected_last_name, car_1.last_name)
    assert_equal(expected_street_address_1, car_1.street_address_1)
    assert_equal(expected_street_address_2, car_1.street_address_2)
    assert_equal(expected_city, car_1.city)
    assert_equal(expected_state, car_1.state)
    assert_equal(expected_zipcode, car_1.zipcode)
    assert_equal(expected_make, car_1.make)
    assert_equal(expected_model, car_1.model)
    assert_equal(expected_year, car_1.year)
    assert_equal(expected_color, car_1.color)
    assert_equal(expected_vehicle_id, car_1.vehicle_id)
    assert_equal(expected_fuel_type, car_1.fuel_type)

    print('\nTest Case: Test Car get_invoice_content method')
    expected_fuel_type = 'Electric'
    expected_make = 'Nissan'
    expected_model = 'Leaf'
    car_1 = Car(expected_first_name,
                expected_last_name,
                expected_street_address_1,
                expected_street_address_2,
                expected_city,
                expected_state,
                expected_zipcode,
                expected_make,
                expected_model,
                expected_year,
                expected_color,
                expected_vehicle_id,
                expected_fuel_type)
    expected_title = 'Car Registration Renewal Invoice'
    expected_detail = [
        ('Make', expected_make),
        ('Model', expected_model),
        ('Year', str(expected_year)),
        ('Color', expected_color),
        ('Vehicle ID', expected_vehicle_id),
        ('Fuel Type', expected_fuel_type)
    ]
    actual_invoice_content = car_1.get_invoice_content()
    actual_title, actual_name_and_address, actual_detail = actual_invoice_content
    assert_equal(expected_title, actual_title)
    assert_equal(expected_name_and_address, actual_name_and_address)
    assert_equal(expected_detail, actual_detail)

    print('\nTest Case: Test Car determine_annual_registration_fee method, fuel_type = Electric')
    expected_fuel_type = 'Electric'
    expected_make = 'Nissan'
    expected_model = 'Leaf'
    expected_annual_registration_fee = 100.00
    car_2 = Car(expected_first_name,
                expected_last_name,
                expected_street_address_1,
                expected_street_address_2,
                expected_city,
                expected_state,
                expected_zipcode,
                expected_make,
                expected_model,
                expected_year,
                expected_color,
                expected_vehicle_id,
                expected_fuel_type)
    assert_equal_float(expected_annual_registration_fee, car_2.determine_annual_registration_fee(), 0.001)

    print('\nTest Case: Test Car determine_annual_registration_fee method, fuel_type = Hybrid')
    expected_fuel_type = 'Hybrid'
    expected_make = 'Toyota'
    expected_model = 'Camry Hybrid'
    expected_annual_registration_fee = 200.00
    car_3 = Car(expected_first_name,
                expected_last_name,
                expected_street_address_1,
                expected_street_address_2,
                expected_city,
                expected_state,
                expected_zipcode,
                expected_make,
                expected_model,
                expected_year,
                expected_color,
                expected_vehicle_id,
                expected_fuel_type)
    assert_equal_float(expected_annual_registration_fee, car_3.determine_annual_registration_fee(), 0.001)

    print('\nTest Case: Test Car determine_annual_registration_fee method, fuel_type = Fossil')
    expected_fuel_type = 'Fossil'
    expected_make = 'Mini'
    expected_model = 'Cooper Countryman All4'
    expected_annual_registration_fee = 300.00
    car_4 = Car(expected_first_name,
                expected_last_name,
                expected_street_address_1,
                expected_street_address_2,
                expected_city,
                expected_state,
                expected_zipcode,
                expected_make,
                expected_model,
                expected_year,
                expected_color,
                expected_vehicle_id,
                expected_fuel_type)
    assert_equal_float(expected_annual_registration_fee, car_4.determine_annual_registration_fee(), 0.001)

    print('\nTest Case: Test Car determine_annual_registration_fee method, fuel_type = Plutonium')
    expected_fuel_type = 'Plutonium'
    expected_make = 'NASA'
    expected_model = 'Lunar Rover'
    expected_annual_registration_fee = 300.00
    car_4 = Car(expected_first_name,
                expected_last_name,
                expected_street_address_1,
                expected_street_address_2,
                expected_city,
                expected_state,
                expected_zipcode,
                expected_make,
                expected_model,
                expected_year,
                expected_color,
                expected_vehicle_id,
                expected_fuel_type)
    try:
        assert_equal_float(expected_annual_registration_fee, car_4.determine_annual_registration_fee(), 0.001)
        print('Failed. Error was not caught.')
    except ValueError as ve:
        if str(ve) == 'Expected fuel type of Electric, Hybrid, or Fossil. This value is Plutonium.':
            print(PASSED)
        else:
            print(f'Failed. Unexpected error message: {ve}')

    # common unit testing variables for the Truck subtype
    expected_make = 'Ford'
    expected_model = 'F-550'
    expected_year = 2022
    expected_color = 'Grey'
    expected_vehicle_id = 'TRK123456789'
    expected_gross_weight = 14000

    print('\nTest Case: Test Truck constructor')
    truck_1 = Truck(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id,
                    expected_gross_weight)
    assert_equal(expected_first_name, truck_1.first_name)
    assert_equal(expected_last_name, truck_1.last_name)
    assert_equal(expected_street_address_1, truck_1.street_address_1)
    assert_equal(expected_street_address_2, truck_1.street_address_2)
    assert_equal(expected_city, truck_1.city)
    assert_equal(expected_state, truck_1.state)
    assert_equal(expected_zipcode, truck_1.zipcode)
    assert_equal(expected_make, truck_1.make)
    assert_equal(expected_model, truck_1.model)
    assert_equal(expected_year, truck_1.year)
    assert_equal(expected_color, truck_1.color)
    assert_equal(expected_vehicle_id, truck_1.vehicle_id)
    assert_equal(expected_gross_weight, truck_1.gross_weight)

    print('\nTest Case: Test Truck get_invoice_content method')
    truck_1 = Truck(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id,
                    expected_gross_weight)
    expected_title = 'Truck Registration Renewal Invoice'
    expected_detail = [
        ('Make', expected_make),
        ('Model', expected_model),
        ('Year', str(expected_year)),
        ('Color', expected_color),
        ('Vehicle ID', expected_vehicle_id),
        ('Gross Weight', f'{expected_gross_weight:,}')
    ]
    actual_invoice_content = truck_1.get_invoice_content()
    actual_title, actual_name_and_address, actual_detail = actual_invoice_content
    assert_equal(expected_title, actual_title)
    assert_equal(expected_name_and_address, actual_name_and_address)
    assert_equal(expected_detail, actual_detail)

    print('\nTest Case: Test Truck determine_annual_registration_fee method, gross_weight = 14000')
    expected_gross_weight = 14000
    expected_annual_registration_fee = 400.00
    truck_2 = Truck(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id,
                    expected_gross_weight)
    assert_equal_float(expected_annual_registration_fee, truck_2.determine_annual_registration_fee(), 0.001)

    print('\nTest Case: Test Truck determine_annual_registration_fee method, gross_weight = 14001')
    expected_gross_weight = 14001
    expected_annual_registration_fee = 700.00
    truck_2 = Truck(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id,
                    expected_gross_weight)
    assert_equal_float(expected_annual_registration_fee, truck_2.determine_annual_registration_fee(), 0.001)


   # common unit testing variables for the Motorcycle subtype
    expected_make = 'Harley'
    expected_model = 'F-550'
    expected_year = 1988
    expected_color = 'Blue'
    expected_vehicle_id = 'TRK123456789'
    expected_displacement_in_ccs = 999

    print('\nTest Case: Test Motorcycle constructor')
    motorcycle_1 = Motorcycle(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id,
                    expected_displacement_in_ccs)
    assert_equal(expected_first_name, motorcycle_1.first_name)
    assert_equal(expected_last_name, motorcycle_1.last_name)
    assert_equal(expected_street_address_1, motorcycle_1.street_address_1)
    assert_equal(expected_street_address_2, motorcycle_1.street_address_2)
    assert_equal(expected_city, motorcycle_1.city)
    assert_equal(expected_state, motorcycle_1.state)
    assert_equal(expected_zipcode, motorcycle_1.zipcode)
    assert_equal(expected_make, motorcycle_1.make)
    assert_equal(expected_model, motorcycle_1.model)
    assert_equal(expected_year, motorcycle_1.year)
    assert_equal(expected_color, motorcycle_1.color)
    assert_equal(expected_vehicle_id, motorcycle_1.vehicle_id)
    assert_equal(expected_displacement_in_ccs, motorcycle_1.displacement_in_ccs)

    print('\nTest Case: Test Motorcycle get_invoice_content method')
    motorcycle_1 = Motorcycle(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id,
                    expected_displacement_in_ccs)
    expected_title = 'Motorcycle Registration Renewal Invoice'
    expected_detail = [
        ('Make', expected_make),
        ('Model', expected_model),
        ('Year', str(expected_year)),
        ('Color', expected_color),
        ('Vehicle ID', expected_vehicle_id),
        ('Displacement in ccs', f'{expected_displacement_in_ccs:,}')
    ]
    actual_invoice_content = motorcycle_1.get_invoice_content()
    actual_title, actual_name_and_address, actual_detail = actual_invoice_content
    assert_equal(expected_title, actual_title)
    assert_equal(expected_name_and_address, actual_name_and_address)
    assert_equal(expected_detail, actual_detail)

    print('\nTest Case: Test Motorcycle determine_annual_registration_fee method, displacement_in_ccs = 999')
    expected_displacement_in_ccs = 999
    expected_annual_registration_fee = 75.00
    motorcycle_2 = Motorcycle(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id,
                    expected_displacement_in_ccs)
    assert_equal_float(expected_annual_registration_fee, motorcycle_2.determine_annual_registration_fee(), 0.001)

    print('\nTest Case: Test Motorcycle determine_annual_registration_fee method, displacement_in_ccs = 1000')
    expected_displacement_in_ccs = 1000
    expected_annual_registration_fee = 150.00
    motorcycle_2 = Motorcycle(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id,
                    expected_displacement_in_ccs)
    assert_equal_float(expected_annual_registration_fee, motorcycle_2.determine_annual_registration_fee(), 0.001)


   # common unit testing variables for the Snowmobile subtype
    expected_make = 'Harley'
    expected_model = 'F-550'
    expected_year = 1988
    expected_color = 'Blue'
    expected_vehicle_id = 'TRK123456789'

    print('\nTest Case: Test Snowmobile constructor')
    snowmobile_1 = Snowmobile(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id)
    assert_equal(expected_first_name, snowmobile_1.first_name)
    assert_equal(expected_last_name, snowmobile_1.last_name)
    assert_equal(expected_street_address_1, snowmobile_1.street_address_1)
    assert_equal(expected_street_address_2, snowmobile_1.street_address_2)
    assert_equal(expected_city, snowmobile_1.city)
    assert_equal(expected_state, snowmobile_1.state)
    assert_equal(expected_zipcode, snowmobile_1.zipcode)
    assert_equal(expected_make, snowmobile_1.make)
    assert_equal(expected_model, snowmobile_1.model)
    assert_equal(expected_year, snowmobile_1.year)
    assert_equal(expected_color, snowmobile_1.color)
    assert_equal(expected_vehicle_id, snowmobile_1.vehicle_id)

    print('\nTest Case: Test Snowmobile get_invoice_content method')
    snowmobile_1 = Snowmobile(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id)
    expected_title = 'Snowmobile Registration Renewal Invoice'
    expected_detail = [
        ('Make', expected_make),
        ('Model', expected_model),
        ('Year', str(expected_year)),
        ('Color', expected_color),
        ('Vehicle ID', expected_vehicle_id)
    ]
    actual_invoice_content = snowmobile_1.get_invoice_content()
    actual_title, actual_name_and_address, actual_detail = actual_invoice_content
    assert_equal(expected_title, actual_title)
    assert_equal(expected_name_and_address, actual_name_and_address)
    assert_equal(expected_detail, actual_detail)

    print('\nTest Case: Test Snowmobile determine_annual_registration_fee method')
    expected_annual_registration_fee = 45.00
    snowmobile_2 = Snowmobile(expected_first_name,
                    expected_last_name,
                    expected_street_address_1,
                    expected_street_address_2,
                    expected_city,
                    expected_state,
                    expected_zipcode,
                    expected_make,
                    expected_model,
                    expected_year,
                    expected_color,
                    expected_vehicle_id)
    assert_equal_float(expected_annual_registration_fee, snowmobile_2.determine_annual_registration_fee(), 0.001)


if __name__ == '__main__':
    main()
