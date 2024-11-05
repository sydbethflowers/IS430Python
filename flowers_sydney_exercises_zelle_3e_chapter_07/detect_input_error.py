"""Ask a user to input 5 integers and handle any bad input with graceful exit."""


from sys import exit


def main():
    print("This program prompts you for 5 integers.")
    print("Valid integer inputs are echoed back to the user.")
    print("Invalid inputs cause an error message and a graceful exit.")

    try:
        for i in range(1, 6):
            user_input = get_my_integer_from_user()
            int(user_input)
            print(f"You have entered the integer {user_input}.")
    except ValueError:
        print(f"An integer was expected. You entered \"{user_input}\".")
        print("Program is ending. Please run it again with proper inputs.")
        exit()
    finally:
        print("\nThanks for playing.")


def get_my_integer_from_user():
    user_input = input('\nPlease enter an integer: ')
    return user_input


main()
