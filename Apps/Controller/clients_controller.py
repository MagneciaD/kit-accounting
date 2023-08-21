import random
import string
from Database.Migrations.connection import create_connection
from Apps.Model.Clients import Client
from Apps.Model.User import User

def generate_client_id():
    numbers = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    client_id = 'CLIENT' + numbers
    return client_id

def create_client_from_input():
    try:
        # Retrieve user_id from the User table
        user_id = input("Enter user ID: ")
        user = User.read_user_by_id(user_id)

        if not user:
            print("User not found.")
            return

        org_id = input("Enter organization ID: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        client_address = input("Enter client address: ")
        phone_no = input("Enter phone number: ")
        timestamp = input("Enter timestamp: ")
        client_id = generate_client_id()

        # Create a Client instance
        client = Client(client_id, user_id, org_id, first_name, last_name, email, client_address, phone_no, timestamp)

        # Assuming the Client class has a save() method
        client.save()

        print("Client created and saved successfully!")

    except Exception as e:
        print("An error occurred:", e)

def read_all_clients():
    clients = Client.read_all()

    if clients:
        for client in clients:
            print(f"Client ID: {client.client_id}")
            print(f"User ID: {client.user_id}")
            print(f"Organization ID: {client.org_id}")
            print(f"First Name: {client.first_name}")
            print(f"Last Name: {client.last_name}")
            print(f"Email: {client.email}")
            print(f"Client Address: {client.client_address}")
            print(f"Phone Number: {client.phone_no}")
            print(f"Timestamp: {client.timestamp}")
            print()  # Add a blank line between clients
    else:
        print("No clients found.")

def read_client_by_client_id():
    client_id = input("Enter the client ID you want to read: ")

    client = Client.read_by_client_id(client_id)

    if client:
        print(f"Client ID: {client.client_id}")
        print(f"User ID: {client.user_id}")
        print(f"Organization ID: {client.org_id}")
        print(f"First Name: {client.first_name}")
        print(f"Last Name: {client.last_name}")
        print(f"Email: {client.email}")
        print(f"Client Address: {client.client_address}")
        print(f"Phone Number: {client.phone_no}")
        print(f"Timestamp: {client.timestamp}")
    else:
        print("Client not found.")

def update_client_from_input(client_id):
    user_id = input("Enter new user ID: ")
    org_id = input("Enter new organization ID: ")
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    email = input("Enter new email: ")
    client_address = input("Enter new client address: ")
    phone_no = input("Enter new phone number: ")
    timestamp = input("Enter new timestamp: ")

    client = Client(client_id, user_id, org_id, first_name, last_name, email, client_address, phone_no, timestamp)
    client.update()

def delete_client_by_client_id(client_id):
    Client.delete_by_client_id(client_id)
    print(f"Client with ID {client_id} has been deleted.")

# Call the create_client_from_input() function to create a new client
create_client_from_input()

# Call the function to read and display all clients
read_all_clients()

# Call the read_client_by_client_id() function to read a client by their ID
read_client_by_client_id()

# Call the update_client_from_input() function to update a client
client_id_to_update = input("Enter the client ID you want to update: ")
update_client_from_input(client_id_to_update)

# Prompt the user to enter the ID of the client they want to delete
client_id_to_delete = input("Enter the ID of the client you want to delete: ")
delete_client_by_client_id(client_id_to_delete)
