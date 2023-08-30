import mysql.connector
from Apps.Controller.clients_controller import *
from Resources.View.admin.dashboard_view import *

def add_client(user_id, org_id):
    print("You selected to add a new client.")
    create_client_from_input(user_id, org_id)

def display_all_clients():
    print("You selected to read all clients.")
    read_all_clients()

def read_client_by_id():
    print("You selected to read a client by ID.")
    client_id = input("Enter the client ID you want to read: ")
    read_client(client_id)

def update_client_by_id():
    print("You selected to update a client.")
    client_id_to_update = input("Enter the client ID you want to update: ")
    update_client(client_id_to_update)

def delete_client_by_id():
    print("You selected to delete a client.")
    client_id_to_delete = input("Enter the ID of the client you want to delete: ")
    delete_client(client_id_to_delete)

def display_clients_menu():
    print("Clients Menu:")
    print("1. Add Client")
    print("2. Read All Clients")
    print("3. Read Client by ID")
    print("4. Update Client")
    print("5. Delete Client")
    print("6. Go back to main menu")

def clients_dashboard(user_id, org_id):
    while True:
        display_clients_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_client(user_id, org_id)
        elif choice == "2":
            display_all_clients()
        elif choice == "3":
            read_client_by_id()
        elif choice == "4":
            update_client_by_id()
        elif choice == "5":
            delete_client_by_id()
        elif choice == "6":
            print("Going back to the main menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    org_id = 456
    clients_dashboard(user_id, org_id)
