import tkinter as tk
from Resources.View.admin.dashboard_view import dash
from Apps.Controller.login_controller import login

class LoginFrame(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("User Login")

        self.email_label = tk.Label(self, text="Enter your email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.password_label = tk.Label(self, text="Enter your password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.on_login_button_click)
        self.login_button.pack()

    def on_login_button_click(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        user_id = login(email, password)

        if user_id is not None:
            self.destroy()  # Close the login window
            dash(user_id)
