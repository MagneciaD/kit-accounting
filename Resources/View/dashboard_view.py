import mysql.connector
from Resources.View.services import *
from Apps.Controller.products_controller import *
from Apps.Controller.user_controller import *


def manage_profiles():
    print("You selected to view profile.")
    # Implement profile view logic here


def manage_products(user_id):
    print("You selected to manage products.")
    create_product_from_input(user_id)
    # Implement product management logic here


def manage_services(user_id):
    print("You selected to manage services.")
    services_dashboard(user_id)
    # create_service_from_input(user_id)
    # read_service_by_id()
    # Implement service management logic here


def display_dash():
    print("Dashboard Menu:")
    print("1. View Profiles")
    print("2. Manage Products")
    print("3. Manage Services")
    print("4. Exit")


def dash(user_id):
    print("Welcome to Dashboard")
    while True:
        display_dash()
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_profiles()
        elif choice == "2":
            manage_products(user_id)
        elif choice == "3":
            manage_services(user_id)
        elif choice == "4":
            print("Exiting the dashboard.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    dash(user_id)
