import tkinter as tk
from tkinter import messagebox
from Apps.Controller.user_controller import create_user
from Resources.View.auth.login_frame import LoginFrame
from Resources.View.auth import register_frame
from Resources.View.auth.register_frame import RegistrationApp


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
        login_frame = LoginFrame(self.root)

    def open_register(self):
        registration_frame = RegistrationApp(self.root)
        self.root.wait_window(registration_frame.root)  # Wait for the registration window to close

        if registration_frame.result:  # Assuming RegistrationApp sets a result attribute
            name, email, password = registration_frame.result
            result = create_user(name, email, password)
            if result.isdigit():
                messagebox.showinfo("Registration Successful", f"User registered successfully! User ID: {result}")
            else:
                messagebox.showerror("Error", f"An error occurred: {result}")

    def exit_program(self):
        if messagebox.askyesno("Exit Program", "Are you sure you want to exit?"):
            self.root.quit()

def main():
    root = tk.Tk()
    app = FrontendApp(root)
    root.mainloop()

if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    main()

