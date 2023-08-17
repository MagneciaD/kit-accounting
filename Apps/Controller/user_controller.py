# Import the User class from the correct module
import random
import string
from Apps.Model.User import User

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

# Call the function to create and save a user
create_user_from_input()
