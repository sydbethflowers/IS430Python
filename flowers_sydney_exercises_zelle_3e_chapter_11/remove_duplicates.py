"""Demonstrate two ways to remove duplicate values from a list"""


def main():
    list_with_duplicates = [1, 1, 2, 2, 2, 3, 4, 5, 5]
    print(f'Includes Duplicates: {list_with_duplicates}')

    list_without_duplicates = create_new_list_without_duplicates(list_with_duplicates)
    print(f'No Duplicates: {list_without_duplicates}')


def create_new_list_without_duplicates(value_list):
    # intuitive version
    unique_values = []

    for value in value_list:
        if value not in unique_values:
            unique_values.append(value)
    return unique_values

    # more clever version
    # return list(set(value_list))


main()
