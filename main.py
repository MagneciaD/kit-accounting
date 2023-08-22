<<<<<<< HEAD


print ('WELCOME TO KIT')

def display_menu():
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
=======
from Apps.Controller.user_controller import *
from Apps.View.login import *
from Apps.View.dashboard_view import *


def display_menu():
    print("Menu:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
>>>>>>> 6f1f6fb6f85fbd164632c21a83b25727c635bf21

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

<<<<<<< HEAD
        if choice == '1':
            print("You selected Option 1")
        elif choice == '2':
            print("You selected Option 2")
        elif choice == '3':
            print("You selected Option 3")
        elif choice == '4':
            print("Exiting...")
            break
=======
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

>>>>>>> 6f1f6fb6f85fbd164632c21a83b25727c635bf21
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 6f1f6fb6f85fbd164632c21a83b25727c635bf21
