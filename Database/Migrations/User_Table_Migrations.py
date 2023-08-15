from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_users_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        table_name = 'users'

        if not table_exists(cursor, table_name):
            query = """
            CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT(20) NOT NULL,
                name VARCHAR(255),
                email VARCHAR(255),
                password VARCHAR(255)
            )
            """
            cursor.execute(query)
            conn.commit()
            print("Table 'users' created successfully.")
        else:
            print("Table 'users' already exists.")

    except mysql.connector.Error as err:
        print("Error creating table:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def drop_users_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS users"
        cursor.execute(query)
        conn.commit()

        print("Table 'users' dropped successfully.")

    except mysql.connector.Error as err:
        print("Error dropping table:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
create_users_table()
# drop_users_table()
