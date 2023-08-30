# Import the User class from the correct module
import random
import string
from Apps.Model.items import Item

def generate_qi_id():
    numbers = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    qi_id = 'QI' + numbers
    return qi_id

def create_item_from_input():
    try:
        user_id = input("Enter user ID: ")
        name = input("Enter item name: ")
        item_quantity = input("Enter item quality: ")
        price = float(input("Enter item price: "))
        sub_total = float(input("Enter sub total: "))
        qi_id = generate_qi_id()

        # Create an Item instance
        item = Item(qi_id, user_id, name, item_quality, price, sub_total)

        # Assuming the Item class has a save() method
        item.save()

        print("Item created and saved successfully!")

    except Exception as e:
        print("An error occurred:", e)

def read_all_items():
    items = Item.read_all()

    if items:
        for item in items:
            print(f"Item ID: {item.qi_id}")
            print(f"User ID: {item.user_id}")
            print(f"Name: {item.name}")
            print(f"Item Quality: {item.item_quality}")
            print(f"Price: {item.price}")
            print(f"Sub Total: {item.sub_total}")
            print()  # Add a blank line between items
    else:
        print("No items found.")

def read_item_by_qi_id():
    qi_id = input("Enter the item ID you want to read: ")

    item = Item.read_by_qi_id(qi_id)

    if item:
        print(f"Item ID: {item.qi_id}")
        print(f"User ID: {item.user_id}")
        print(f"Name: {item.name}")
        print(f"Item Quality: {item.item_quality}")
        print(f"Price: {item.price}")
        print(f"Sub Total: {item.sub_total}")
    else:
        print("Item not found.")

def update_item_from_input(qi_id, user_id):
    name = input("Enter new item name: ")
    item_quality = input("Enter new item quality: ")
    price = float(input("Enter new item price: "))
    sub_total = float(input("Enter new sub total: "))

    item = Item(qi_id, user_id, name, item_quality, price, sub_total)
    item.update()


def delete_item_by_qi_id(qi_id):
    Item.delete_by_qi_id(qi_id)
    print(f"Item with ID {qi_id} has been deleted.")

# Call the create_item_from_input() function to create a new item
create_item_from_input()

# Call the function to read and display all items
# read_all_items()

# Call the read_item_by_qi_id() function to read an item by its ID
read_item_by_qi_id()

# Prompt the user to enter the ID of the item they want to update
item_qi_id_to_update = input("Enter the item ID you want to update: ")

# Prompt the user to enter the new user ID
# new_user_id = input("Enter new user ID: ")
# update_item_from_input(item_qi_id_to_update, new_user_id)


# Prompt the user to enter the ID of the item they want to delete
# item_qi_id_to_delete = input("Enter the ID of the item you want to delete: ")
# delete_item_by_qi_id(item_qi_id_to_delete)
