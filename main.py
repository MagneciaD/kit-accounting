import tkinter as tk
from tkinter import messagebox
from Apps.Controller.user_controller import *
from Resources.View.auth.login import *
from Resources.View.admin.dashboard_view import *

class FrontendApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Application Menu")

        # Create buttons for each option
        self.login_button = tk.Button(self.root, text="Open Login", command=self.open_login)
        self.register_button = tk.Button(self.root, text="Open Register", command=self.open_register)
        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_program)

        # Pack buttons
        self.login_button.pack()
        self.register_button.pack()
        self.exit_button.pack()

    def open_login(self):
        user_id = login()  # Return the user_id from the login function
        if user_id:
            dash(user_id)  # Pass the user_id to the dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_register(self):
        print("User Registration Page.")
        create_user_from_input()

    def exit_program(self):
        if messagebox.askyesno("Exit Program", "Are you sure you want to exit?"):
            self.root.quit()

def main():
    root = tk.Tk()
    app = FrontendApp(root)
    root.mainloop()

if __name__ == "__main__":
  main()
