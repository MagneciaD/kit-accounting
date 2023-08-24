from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

class Product:
    def _init_(self, product_id, user_id, product_name, description, price):
        self.product_id = product_id
        self.user_id = user_id
        self.product_name = product_name
        self.description = description
        self.price = price

    def save(self):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO products (product_id, user_id, product_name, description, price)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (self.product_id, self.user_id, self.product_name, self.description, self.price)

            cursor.execute(query, values)
            conn.commit()
            print("Product created successfully.")

        except mysql.connector.Error as err:
            print("Error creating Product: {}".format(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def read_all():
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = "SELECT * FROM products"
            cursor.execute(query)
            product_data_list = cursor.fetchall()

            products = []
            for product_data in product_data_list:
                product = Product(product_data[0], product_data[1], product_data[2], product_data[3], product_data[4])
                products.append(product)

            return products

        except mysql.connector.Error as err:
            print("Error reading services: {}".format(err))
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = """
            UPDATE products
            SET user_id = %s, product_name = %s, description = %s, price = %s
            WHERE product_id = %s
            """
            values = (self.user_id, self.product_name, self.description, self.price, self.product_id)

            cursor.execute(query, values)
            conn.commit()
            print("Product updated successfully.")

        except mysql.connector.Error as err:
            print("Error updating product: {}".format(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def read(product_id):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = "SELECT * FROM services WHERE product_id = %s"
            values = (product_id,)

            cursor.execute(query, values)
            product_data = cursor.fetchone()

            if product_data:
                product = Product(product_data[0], product_data[1], product_data[2], product_data[3], product_data[4])
                return product
            else:
                print("product not found.")
                return None

        except mysql.connector.Error as err:
            print("Error reading product: {}".format(err))
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def delete(product_id):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = "DELETE FROM products WHERE s_id = %s"
            values = (product_id,)

            cursor.execute(query, values)
            conn.commit()
            print("product deleted successfully.")

        except mysql.connector.Error as err:
            print("Error deleting product: {}".format(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()