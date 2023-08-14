from Apps.Model.User import User

def create_user(name, email, password):
    user = User(name, email, password)
    user.save()

