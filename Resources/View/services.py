import mysql.connector
from Apps.Controller.services_controller import *
from Resources.View.dashboard_view import *

print("Services Page")


def add_service(user_id):
    print("You selected to add a new service.")
    create_service_from_input(user_id)

def display_all_services():
    print("You selected to read all services.")
    read_all_services()

def read_service():
    print("You selected to read a service by ID.")
    read_service_by_id()

def update_service():
    print("You selected to update a service.")
    service_id_to_update = input("Enter the service ID you want to update: ")
    update_service_from_input(service_id_to_update)

def delete_service():
    print("You selected to delete a service.")
    service_id_to_delete = input("Enter the ID of the service you want to delete: ")
    delete_service_by_id(service_id_to_delete)

def display_services_menu():
    print("Services Menu:")
    print("1. Add Service")
    print("2. Read All Services")
    print("3. Read Service by ID")
    print("4. Update Service")
    print("5. Delete Service")
    print("6. Go back to main menu")

def services_dashboard(user_id):
    while True:
        display_services_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_service(user_id)
        elif choice == "2":
            read_all_services()
        elif choice == "3":
            read_service()
        elif choice == "4":
            update_service()
        elif choice == "5":
            delete_service()
        elif choice == "6":
            print("Going back to the main menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    services_dashboard(user_id)
