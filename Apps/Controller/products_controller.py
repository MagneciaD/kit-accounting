from Apps.Model.Products import Product
import random
import string

def generate_product_id():
    numbers = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    product_id = 'PDT' + numbers
    return product_id

def create_product_from_input(user_id):
    try:
        print("User ID inside create_product_from_input:", user_id)
        product_name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        product_id = generate_product_id()

        product = Product(product_id, user_id, product_name, description, price)
        product.save()

        print("Product created and saved successfully!")

    except Exception as e:
        print("An error occurred:", e)

def read_all_products():
    products = Product.read_all()

    if products:
        for product in products:
            print(f"Product ID: {product.id}")
            print(f"Product Name: {product.product_name}")
            print(f"Description: {product.description}")
            print(f"Price: {product.price}")
            print()  # Add a blank line between products
    else:
        print("No product found.")

def read_product_by_id():
    product_id = input("Enter the product ID you want to read: ")

    product = Product.read(product_id)

    if product:
        print(f"Product ID: {product.id}")
        print(f"Product Name: {product.product_name}")
        print(f"Description: {product.description}")
        print(f"Price: {product.price}")
    else:
        print("Product not found.")

def update_product_from_input(product_id):
    product_name = input("Enter the new product name: ")
    description = input("Enter the new product description: ")
    price = float(input("Enter the new product price: "))

    product = Product(product_id, None, product_name, description, price)
    product.update()

def delete_product_by_id(product_id):
    product = Product()
    product.id = product_id
    product.delete()
    print(f"product with ID {product_id} has been deleted.")

# Call the create_product_from_input function to create a new product
# create_product_from_input()

# Call the function to read and display all product
# read_all_products()

# Call the read_product_by_id() function to read a product by its ID
# read_product_by_id()

# Call the update_product_from_input() function to update a product
# product_id_to_update = input("Enter the product ID you want to update: ")
# update_product_from_input(product_id_to_update)

# Prompt the user to enter the ID of the product they want to delete
# product_id_to_delete = input("Enter the ID of the product you want to delete: ")
# delete_product_by_id(product_id_to_delete)