import tkinter as tk
from tkinter import messagebox
from Apps.Controller.user_controller import create_user

class RegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        self.open_registration()

    def open_registration(self):
        registration_window = tk.Toplevel(self.root)
        registration_window.title("User Registration")

        self.name_label = tk.Label(registration_window, text="Name:")
        self.name_entry = tk.Entry(registration_window)

        self.email_label = tk.Label(registration_window, text="Email:")
        self.email_entry = tk.Entry(registration_window)

        self.password_label = tk.Label(registration_window, text="Password:")
        self.password_entry = tk.Entry(registration_window, show="*")

        self.register_button = tk.Button(registration_window, text="Register", command=self.register)

        self.name_label.pack()
        self.name_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.register_button.pack()

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not name or not email or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            self.result = (name, email, password)  # Store the registration inputs
            self.root.destroy()  # Close the main window

def main():
    root = tk.Tk()
    app = RegistrationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
