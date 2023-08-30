import random
import string
from Database.Migrations.connection import create_connection
from Apps.Model.Clients import Client
from Apps.Model.User import *

def generate_client_id():
    numbers = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    client_id = 'CLT' + numbers
    return client_id

def create_client_from_input(user_id):
    try:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        client_address = input("Enter client address: ")
        phone_no = input("Enter phone number: ")
        timestamp = input("Enter timestamp: ")
        client_id = generate_client_id()

        client = Client(client_id, user_id, first_name, last_name, email, client_address, phone_no, timestamp)
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
            print(f"First Name: {client.first_name}")
            print(f"Last Name: {client.last_name}")
            print(f"Email: {client.email}")
            print(f"Client Address: {client.client_address}")
            print(f"Phone Number: {client.phone_no}")
            print(f"Timestamp: {client.timestamp}")
            print()  # Add a blank line between services
    else:
        print("No clients found.")

def read_client():
    client_id = input("Enter the client ID you want to read: ")

    client = Client.read_by_client_id(client_id)

    if client:
        print(f"Client ID: {client.client_id}")
        print(f"User ID: {client.user_id}")
        print(f"First Name: {client.first_name}")
        print(f"Last Name: {client.last_name}")
        print(f"Email: {client.email}")
        print(f"Client Address: {client.client_address}")
        print(f"Phone Number: {client.phone_no}")
        print(f"Timestamp: {client.timestamp}")
    else:
        print("Client not found.")


def update_client(client_id):
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    email = input("Enter new email: ")
    client_address = input("Enter new client address: ")
    phone_no = input("Enter new phone number: ")

    client = Client(client_id, None, first_name, last_name, email, client_address, phone_no)
    client.update()


def delete_client(client_id):
    try:
        Client.delete_by_client_id(client_id)  # Call the static delete method directly
        print(f"Client with ID {client_id} has been deleted.")
    except Exception as e:
        print("An error occurred:", e)


def print_client_details(client):
    print(f"Client ID: {client.client_id}")
    print(f"User ID: {client.user_id}")
    print(f"First Name: {client.first_name}")
    print(f"Last Name: {client.last_name}")
    print(f"Email: {client.email}")
    print(f"Client Address: {client.client_address}")
    print(f"Phone Number: {client.phone_no}")
    print(f"Timestamp: {client.timestamp}")
    print()  # Add a blank line between clients

# ========================================================================================

# Call the create_client_from_input() function to create a new client
# user_id = input("Enter user ID: ")
# create_client_from_input(user_id)

# Call the function to read and display all clients
# read_all_clients()

# Call the read_client_by_client_id() function to read a client by their ID
# client_id_to_read = input("Enter the client ID you want to read: ")
# read_client_by_client_id(client_id_to_read)

# Call the update_client_from_input() function to update a client
# client_id_to_update = input("Enter the client ID you want to update: ")
# update_client_from_input(client_id_to_update)

# Prompt the user to enter the ID of the client they want to delete
# client_id_to_delete = input("Enter the ID of the client you want to delete: ")
# delete_client_by_client_id(client_id_to_delete)

# print_client_details(client)
