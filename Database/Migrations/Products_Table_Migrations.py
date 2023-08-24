from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_products_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        table_name = 'products'

        if not table_exists(cursor, table_name):
            query = """
            CREATE TABLE products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_id VARCHAR(20) NOT NULL,
                user_id VARCHAR(20) NOT NULL,
                product_name VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                price FLOAT(20.1) NOT NULL,
                UNIQUE (product_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            );
            """
            cursor.execute(query)
            conn.commit()
            print("Table 'products' created successfully.")
        else:
            print("Table 'products' already exists.")

    except mysql.connector.Error as err:
        print("Error creating table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def drop_products_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS products"
        cursor.execute(query)
        conn.commit()

        print("Table 'products' dropped successfully.")

    except mysql.connector.Error as err:
        print("Error dropping table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
create_products_table()
# drop_products_table()