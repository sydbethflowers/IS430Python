""" Validate a password choice using my_better_password_module. """

from my_better_password_module import validate_password


def main():
    while True:
        password_candidate = input('\nPlease enter a candidate password (<Enter> to cancel):  ')
        error_messages = validate_password(password_candidate)
        if password_candidate == "":
            print('Password change has been canceled.')

        elif len(error_messages) == 0:
            print('Your new password has been accepted.')
        else:
            print('\nThis was not an acceptable choice.')
            print('Please correct the following problems:')
            for message in error_messages:
                print(f'    {message}')


main()
