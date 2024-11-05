"""Practice using the State class."""

from my_states import State


def main():
    s1 = State('Wisconsin', 150000.25, 10500.25)
    print(str(s1))
    print(s1)
    print(s1.state_name)
    print(s1.land_area_in_square_miles)
    print(s1.water_area_in_square_miles)
    print(s1.calculate_total_area_in_square_miles())

    s2 = State('Illinois', 100000.25, 500.25)
    s3 = State('Florida', 125000.25, 20500.25)

    states = [s1, s2, s3]

    print(states)


main()
