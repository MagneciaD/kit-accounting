from Apps.Controller.products_controller import create_product_from_input
from Resources.View.services import services_dashboard
from Resources.View.products import products_dashboard
from Resources.View.clients_view import clients_dashboard
from Resources.View.profile_view import *

def manage_profiles(user_id):
    print("You selected to manage profiles.")
    profile_dashboard(user_id)
    # Implement profile management logic here

def manage_products(user_id):
    print("You selected to manage products.")
    products_dashboard(user_id)
    # Implement product management logic here

def manage_services(user_id):
    print("You selected to manage services.")
    services_dashboard(user_id)
    # Implement service management logic here

def manage_clients(user_id, org_id):
    print("You selected to manage clients.")
    clients_dashboard(user_id, org_id)

def display_dash():
    print("Dashboard Menu:")
    print("1. Manage Profiles")
    print("2. Manage Products")
    print("3. Manage Services")
    print("4. Manage Clients")
    print("5. Exit")

def dash(user_id):
    print("Welcome to Dashboard")
    while True:
        display_dash()
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_profiles(user_id)
        elif choice == "2":
            manage_products(user_id)
        elif choice == "3":
            manage_services(user_id)
        elif choice == "4":
            manage_clients(user_id, org_id)
        elif choice == "5":
            print("Exiting the dashboard.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    org_id = 456
    dash(user_id)
