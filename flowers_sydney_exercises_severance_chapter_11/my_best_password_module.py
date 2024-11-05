"""
A module for validating a password candidate using re.search() function and top 100 most common passwords.

FUNCTIONS:
    validate_password()
"""

import re
from is430_unit_test_helpers import assert_equal


def read_file_and_find_common_passwords():
    infile = open('data/top_100_most_common_passwords.txt', 'r', encoding='utf8')
    most_common_passwords = []
    for line in infile:
        most_common_passwords.append(line.strip())
    return most_common_passwords


def validate_password(candidate, most_common_passwords):
    """
    Validate a candidate for a password for compliance with organizational standards.

    :param candidate: str value is the proposed new password
    :param most_common_passwords: list of common passwords to check against
    :return: a list of error message string. Candidate password is valid when list is empty.
    """
    answer = []

    if len(candidate) < 6:
        answer.append('Password must be at least 6 characters long.')

    if not re.search(r'[A-Z]', candidate):
        answer.append('Password must contain at least one upper-case letter (A-Z).')

    if not re.search(r'[a-z]', candidate):
        answer.append('Password must contain at least one lower-case letter (a-z).')

    if not re.search(r'[0-9]', candidate):
        answer.append('Password must contain at least one digit (0-9).')

    if not re.search(r'[!@#$%^&*]', candidate):
        answer.append('Password must contain at least one special character (!@#$%^&*).')

    if re.search(r'opensesame', candidate, re.IGNORECASE):
        answer.append('Password may not contain "opensesame" in any case.')

    if re.search(r'password', candidate, re.IGNORECASE):
        answer.append('Password may not contain "password" in any case.')

    if re.search(r'secret', candidate, re.IGNORECASE):
        answer.append('Password may not contain "secret" in any case.')

    if re.search(r'\s', candidate):
        answer.append('Password may not contain a space.')

    if candidate in most_common_passwords:
        answer.append('Password must not be on the list of common passwords.')

    return answer


def main():
    print('Unit testing output...')

    common_passwords = read_file_and_find_common_passwords()

    print('\nTest case 1: password meets all criteria')
    input_password = 'Bc&456'
    expected_result = []
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 2: password too short')
    input_password = 'Ab#45'
    expected_result = ['Password must be at least 6 characters long.']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 3: password missing upper case letter')
    input_password = 'ac&456'
    expected_result = ['Password must contain at least one upper-case letter (A-Z).']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 4: password missing lower-case letter')
    input_password = 'A*3456'
    expected_result = ['Password must contain at least one lower-case letter (a-z).']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 5: password missing special character')
    input_password = 'Aa3456'
    expected_result = ['Password must contain at least one special character (!@#$%^&*).']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 6: password contains word opensesame')
    input_password = 'Aa%opensesame456'
    expected_result = ['Password may not contain "opensesame" in any case.']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 7: password missing multiple of the criteria')
    input_password = '12345'
    msg_1 = 'Password must be at least 6 characters long.'
    msg_2 = 'Password must contain at least one upper-case letter (A-Z).'
    msg_3 = 'Password must contain at least one lower-case letter (a-z).'
    msg_4 = 'Password must contain at least one special character (!@#$%^&*).'
    msg_5 = 'Password must not be on the list of common passwords.'
    expected_result = [msg_1, msg_2, msg_3, msg_4, msg_5]
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 8: password missing digit')
    input_password = 'Aa#dfy'
    expected_result = ['Password must contain at least one digit (0-9).']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 9: password contains word password')
    input_password = 'Ab#password45'
    expected_result = ['Password may not contain "password" in any case.']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 10: password contains word secret')
    input_password = 'Ab#secret45'
    expected_result = ['Password may not contain "secret" in any case.']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)

    print('\nTest case 11: password contains a space')
    input_password = 'Ab# 456'
    expected_result = ['Password may not contain a space.']
    actual_result = validate_password(input_password, common_passwords)
    assert_equal(expected_result, actual_result)


if __name__ == '__main__':
    main()
