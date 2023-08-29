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
        print("Creating a New Product")
        product_name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = None
        while price is None:
            try:
                price = float(input("Enter product price: "))
            except ValueError:
                print("Invalid input. Please enter a valid price.")

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
            print(f"Product ID: {product.product_id}")  # Corrected attribute name
            print(f"Product Name: {product.product_name}")
            print(f"Description: {product.description}")
            print(f"Price: {product.price}")
            print()
    else:
        print("No products found.")


def read_products_by_id():
    product_id = input("Enter the service ID you want to read: ")

    product = Product.read(product_id)

    if product:
        print(f"Product ID: {product.product_id}")
        print(f"Product Description: {product.description}")
        print(f"Product Name: {product.product_name}")
        print(f"Price: {product.price}")  # Display service_price
    else:
        print("Product not found.")

def update_product_from_input(product_id):
    product_name = input("Enter the new Product name: ")
    description = input("Enter the new Product description: ")
    price = float(input("Enter the new Product price: "))

    product = Product(product_id, None, product_name, description, price)
    product.update()

def delete_product_by_id(product_id):
    try:
        Product.delete(product_id)  # Call the static delete method directly
        print(f"Product with ID {product_id} has been deleted.")
    except Exception as e:
        print("An error occurred:", e)

# Other functions (read_product_by_id, update_product_from_input, delete_product_by_id) remain the same


