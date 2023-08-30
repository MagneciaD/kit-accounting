import tkinter as tk
from tkinter import messagebox
from Resources.View.admin.services_view import services_dashboard
from Resources.View.admin.products_view import products_dashboard
from Resources.View.admin.clients_view import clients_dashboard
from Resources.View.admin.profile_view import *

def manage_profiles(user_id):
    profile_dashboard(user_id)
    messagebox.showinfo("Manage Profiles", "You selected to manage profiles.")
    # Implement profile management logic here

def manage_products(user_id):
    products_dashboard(user_id)
    messagebox.showinfo("Manage Products", "You selected to manage products.")
    # Implement product management logic here

def manage_services(user_id):
    services_dashboard(user_id)
    messagebox.showinfo("Manage Services", "You selected to manage services.")
    # Implement service management logic here

def manage_clients(user_id):
    clients_dashboard(user_id)
    messagebox.showinfo("Manage Clients", "You selected to manage clients.")
    # Implement client management logic here

def exit_dashboard():
    root.destroy()

def dash(user_id):
    root = tk.Tk()
    root.title("Dashboard Menu")

    profiles_button = tk.Button(root, text="Manage Profiles", command=lambda: manage_profiles(user_id))
    products_button = tk.Button(root, text="Manage Products", command=lambda: manage_products(user_id))
    services_button = tk.Button(root, text="Manage Services", command=lambda: manage_services(user_id))
    clients_button = tk.Button(root, text="Manage Clients", command=lambda: manage_clients(user_id))
    exit_button = tk.Button(root, text="Exit", command=exit_dashboard)

    profiles_button.pack()
    products_button.pack()
    services_button.pack()
    clients_button.pack()
    exit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    dash(user_id)
