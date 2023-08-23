from Apps.Model.User import User
from Apps.Controller.user_controller import *
from Resources.View.profile_view import *



def display_dash():
    print("Dashboard Menu:")
    print("1. View Profiles")
    print("2. Manage Products")
    print("3. Manage Services")
    print("4. Exit")

def manage_profiles(user, organization):
    display_user_profile(user)
    display_organization_profile(organization)

def manage_products():
    print("You selected to manage products.")
    # Implement product management logic here

def manage_services():
    print("You selected to manage services.")
    # Implement service management logic here

def dash():
    logged_in_user_id = int(input("Enter your user ID: "))

    # Retrieve user and organization information based on the user ID
    user = User.read(logged_in_user_id)
    organization = Organization.read_by_user_id(logged_in_user_id)

    while True:
        display_dash()
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_profiles(user, organization)

        elif choice == "2":
            manage_products()

        elif choice == "3":
            manage_services()

        elif choice == "4":
            print("Logging out...")
            return

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    dash()
