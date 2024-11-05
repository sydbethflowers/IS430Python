"""
Check if a vessel is eligible to pass through the Panama Canal
using a validation function that returns a list of error messages.
"""


def main():
    print('This program checks candidate vessels for compliance with the new Panamax limits.')
    tonnage = int(input('Please enter the tonnage of the vessel in DWT: '))
    length = int(input('Please enter the length of the vessel in feet: '))
    beam = int(input('Please enter the beam of the vessel in feet: '))
    height = int(input('Please enter the height of the vessel in feet: '))
    draft = int(input('Please enter the draft of the vessel in feet: '))
    capacity = int(input('Please enter the capacity of the vessel in TEU: '))

    errors = check_vessel_qualification(tonnage, length, beam, height, draft, capacity)

    if len(errors) == 0:
        print('This vessel is eligible to transit the Panama Canal.')
    else:
        print('This vessel is NOT ELIGIBLE to transit the Panama Canal for the following reasons: ')
        for message in errors:
            print(message)


def check_vessel_qualification(tonnage, length, beam, height, draft, capacity):
    error_messages = []

    if tonnage > 120000:
        error_messages.append('Tonnage cannot be greater than 120,000 DWT.')
    if length > 1201:
        error_messages.append('Length cannot be greater than 1,201 feet.')
    if beam > 168:
        error_messages.append('Beam cannot be greater than 168 feet.')
    if height > 190:
        error_messages.append('Height cannot be greater than 190 feet.')
    if draft > 50:
        error_messages.append('Draft cannot be greater than 50 feet.')
    if capacity > 14000:
        error_messages.append('Capacity cannot be greater than 14,000 TEU.')

    return error_messages


main()
