import mysql.connector
from Apps.Controller.user_controller import create_user_from_input
from Resources.View.auth.login import login
from Resources.View.admin.dashboard_view import dash

class FrontendApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Application Menu")

class AppMenu:
    def __init__(self):
        self.options = {
            "1": self.open_login,
            "2": self.open_register,
            "3": self.exit_program
        }

    @staticmethod
    def display_menu():
        print("Menu:")
        print("1. Open Login")
        print("2. Open Register")
        print("3. Exit")

    @staticmethod
    def open_login():
        return login()  # Return the user_id from the login function

    @staticmethod
    def open_register():
        print("User Registration Page.")
        create_user_from_input()

    @staticmethod
    def exit_program():
        print("Exiting the program.")
        return True

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice in self.options:
                if choice == "1":
                    user_id = self.options[choice]()  # Get the user_id from the login function
                    if user_id:
                        dash(user_id)  # Pass the user_id to the dashboard
                    else:
                        print("Login failed.")
                elif choice == "3":
                    if self.options[choice]():
                        break
                else:
                    self.options[choice]()
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    app_menu = AppMenu()
    app_menu.run()
