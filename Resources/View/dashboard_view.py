from Apps.Controller.services_controller import *
from Apps.Controller.user_controller import *

def display_dash():
    print("Dashboard Menu:")
    print("1. View Profiles")
    print("2. Manage Products")
    print("3. Manage Services")
    print("4. Exit")

def manage_profiles():
    print("You selected to view profile.")
    # Implement profile view logic here

def manage_products():
    print("You selected to manage products.")
    # Implement product management logic here

def manage_services(user_id):  # Accept user_id as a parameter
    print("You selected to manage services.")
    create_service_from_input(user_id)  # Pass user_id to the function

    # Implement service management logic here

def dash(user_id):
    while True:
        display_dash()
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_profiles()

        elif choice == "2":
            manage_products()

        elif choice == "3":
            manage_services(user_id)  # Pass the user_id

        elif choice == "4":
            print("Logging out...")
            return

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":

    dash()