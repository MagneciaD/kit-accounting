import mysql.connector
from Apps.Controller.products_controller import *
from Resources.View. admin.dashboard_view import *

def add_product(user_id):
    print("You selected to add a new product.")
    create_product_from_input(user_id)

def display_all_product():
    print("You selected to read all products.")
    read_all_products()

def read_product():
    print("You selected to read a product by ID.")
    read_products_by_id()

def update_product():
    print("You selected to update a product.")
    product_id_to_update = input("Enter the product ID you want to update: ")
    update_product_from_input(product_id_to_update)

def delete_product():
    print("You selected to delete a product.")
    product_id_to_delete = input("Enter the ID of the product you want to delete: ")
    delete_product_by_id(product_id_to_delete)

def display_product_menu():
    print("Products Menu:")
    print("1. Add Product")
    print("2. Read All Products")
    print("3. Read Product by ID")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Go back to main menu")

def products_dashboard(user_id):
    while True:
        display_product_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(user_id)
        elif choice == "2":
            read_all_products()
        elif choice == "3":
            read_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Going back to the main menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    products_dashboard(user_id)
