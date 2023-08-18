# Import the User class from the correct module
import random
import string
from Apps.Model.User import User

def generate_user_id():
    numbers = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    user_id = 'USER' + numbers
    return user_id

# Create user
def create_user_from_input():
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user_id = generate_user_id()

        # Create a User instance
        user = User(user_id, name, email, password)

        # Assuming the User class has a save() method
        user.save()

        print("User created and saved successfully!")

    except Exception as e:
        print("An error occurred:", e)

def generate_user_id():
    numbers = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    user_id = 'USER' + numbers
    return user_id

def create_user_from_input():
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user_id = generate_user_id()

        # Create a User instance
        user = User(user_id, name, email, password)

        # Assuming the User class has a save() method
        user.save()

        print("User created and saved successfully!")

    except Exception as e:
        print("An error occurred:", e)

# Read User
def read_all_users():
    users = User.read_all()

    if users:
        for user in users:
            print(f"User ID: {user.id}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print()  # Add a blank line between users
    else:
        print("No users found.")

# Read by ID
def read_user_by_id():
    user_id = int(input("Enter the user ID you want to read: "))

    user = User.read(user_id)

    if user:
        print(f"User ID: {user.id}")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
    else:
        print("User not found.")

def update_user_from_input(user_id):
    name = input("Enter the new name: ")
    email = input("Enter the new email: ")
    password = input("Enter the new password: ")

    user = User(user_id, name, email, password)  # Pass all required arguments
    user.update()

# Controller
def delete_user_by_id(user_id):
    User.delete_by_id(user_id)
    print(f"User with ID {user_id} has been deleted.")


# Call the create_user_from_input() function to create a new user
# create_user_from_input()

# Call the function to read and display all users
# read_all_users()

# Call the read_user_by_id() function to read a user by their ID
# read_user_by_id()

# Call the update_user_from_input() function to update a user
# user_id_to_update = int(input("Enter the user ID you want to update: "))
# update_user_from_input(user_id_to_update)

# Prompt the user to enter the ID of the user they want to delete
# user_id_to_delete = int(input("Enter the ID of the user you want to delete: "))
# delete_user_by_id(user_id_to_delete)
