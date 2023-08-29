import tkinter as tk
from tkinter import messagebox
from Apps.Controller.user_controller import create_user

class RegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_entry = tk.Entry(self.root)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")

        self.register_button = tk.Button(self.root, text="Register", command=self.register)

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
            result = create_user(name, email, password)
            if result.isdigit():
                messagebox.showinfo("Registration Successful", f"User registered successfully! User ID: {result}")
            else:
                messagebox.showerror("Error", f"An error occurred: {result}")

def main():
    root = tk.Tk()
    app = RegistrationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
