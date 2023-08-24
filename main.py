from Apps.Controller.user_controller import *
from Resources.View.login import fill_in
from Resources.View.dashboard_view import *

def display_menu():
    print("Menu:")
    print("1. Open Login")
    print("2. Option 2")
    print("3. Exit")

def open_login():
    print("Opening Login...")
    fill_in()

def option_2():
    print("You selected Option 2.")
    # Perform actions for Option 2
    create_user_from_input()

def exit_program():
    print("Exiting the program.")
    return True

def main():
    options = {
        "1": open_login,
        "2": option_2,
        "3": exit_program
    }

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice in options:
            if options[choice]():
                break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


