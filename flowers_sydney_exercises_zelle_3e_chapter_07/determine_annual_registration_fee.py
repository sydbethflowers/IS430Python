""" A program that determines which ribbon a child earns. """


def main():
    print(determine_annual_fee('car', 2900) == 125.00)
    print(determine_annual_fee('car', 3100) == 200.00)
    print(determine_annual_fee('car', 1900) == 125.00)
    print(determine_annual_fee('car', 5000) == 200.00)
    print(determine_annual_fee('truck', 2000) == 250.00)
    print(determine_annual_fee('truck', 5000) == 300.00)
    print(determine_annual_fee('truck', 1000) == 250.00)
    print(determine_annual_fee('truck', 9000) == 300.00)

    print(determine_annual_fee('motorcycle', 800) == 100.00)


def determine_annual_fee(vehicle_type, vehicle_weight):
    if vehicle_type == 'car':
        if vehicle_weight < 3000:
            annual_fee = 125.00
        else:
            annual_fee = 200.00
    elif vehicle_type == 'truck':
        if vehicle_weight < 4000:
            annual_fee = 250.00
        else:
            annual_fee = 300.00
    else:
        raise ValueError(f'{vehicle_type} is not a recognized vehicle-type.')
    return annual_fee


main()
