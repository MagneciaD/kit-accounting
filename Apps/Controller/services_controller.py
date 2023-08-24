from Apps.Model.Services import Service
import random
import string

def generate_service_id():
    numbers = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    service_id = 'SVC' + numbers
    return service_id

def create_service_from_input(user_id):
    try:
        print("User ID inside create_service_from_input:", user_id)
        service_name = input("Enter service name: ")
        description = input("Enter service description: ")
        price = float(input("Enter service price: "))
        service_id = generate_service_id()

        service = Service(service_id, user_id, service_name, description, price)
        service.save()

        print("Service created and saved successfully!")

    except Exception as e:
        print("An error occurred:", e)

def read_all_services():
    services = Service.read_all()

    if services:
        for service in services:
            print(f"Service ID: {service.id}")
            print(f"Service Name: {service.service_name}")
            print(f"Description: {service.description}")
            print(f"Price: {service.price}")
            print()  # Add a blank line between services
    else:
        print("No services found.")

def read_service_by_id():
    service_id = input("Enter the service ID you want to read: ")

    service = Service.read(service_id)

    if service:
        print(f"Service ID: {service.id}")
        print(f"Service Name: {service.service_name}")
        print(f"Description: {service.description}")
        print(f"Price: {service.price}")
    else:
        print("Service not found.")

def update_service_from_input(service_id):
    service_name = input("Enter the new service name: ")
    description = input("Enter the new service description: ")
    price = float(input("Enter the new service price: "))

    service = Service(service_id, None, service_name, description, price)
    service.update()

def delete_service_by_id(service_id):
    service = Service()
    service.id = service_id
    service.delete()
    print(f"Service with ID {service_id} has been deleted.")

# Call the create_service_from_input function to create a new service
# create_service_from_input()

# Call the function to read and display all services
# read_all_services()

# Call the read_service_by_id() function to read a service by its ID
# read_service_by_id()

# Call the update_service_from_input() function to update a service
# service_id_to_update = input("Enter the service ID you want to update: ")
# update_service_from_input(service_id_to_update)

# Prompt the user to enter the ID of the service they want to delete
# service_id_to_delete = input("Enter the ID of the service you want to delete: ")
# delete_service_by_id(service_id_to_delete)
