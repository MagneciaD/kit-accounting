from Apps.Model.User import User

def create_user_from_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = User(name, email, password)
    user.save()

create_user_from_input()


