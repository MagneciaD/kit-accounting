import mysql.connector
from Apps.Controller.user_controller import *
from Resources.View.login import *
from Resources.View.dashboard_view import *


def display_menu():
    print("Menu:")
    print("1. Open Login")
    print("2. Open Register")
    print("3. Exit")

def open_login():
    return login()  # Return the user_id from the login function

def open_register():
    print("User Registration Page.")
    # Perform actions for Option 2
    create_user_from_input()

def exit_program():
    print("Exiting the program.")
    return True

def main():
    options = {
        "1": open_login,
        "2": open_register,
        "3": exit_program
    }

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice in options:
            if choice == "1":
                user_id = options[choice]()  # Get the user_id from the login function
                if user_id:
                    dash(user_id)  # Pass the user_id to the dashboard
                else:
                    print("Login failed.")
            elif choice == "3":
                if options[choice]():
                    break
            else:
                options[choice]()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
