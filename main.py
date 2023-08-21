from Apps.Controller.user_controller import *
from Apps.View.login import *
from Apps.View.dashboard_view import *


def display_menu():
    print("Menu:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Opening Login...")
            fill_in()

        elif choice == "2":
            print("You selected Option 2.")
            # Perform actions for Option 2
            create_user_from_input()
            dash()

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()