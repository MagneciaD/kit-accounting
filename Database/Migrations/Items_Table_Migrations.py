from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_items_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        table_name = 'items'

        if not table_exists(cursor, table_name):
            query = """
            CREATE TABLE items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                qi_id VARCHAR(20) NOT NULL,
                user_id VARCHAR(20) NOT NULL,
                name VARCHAR(255) NOT NULL,
                item_quality INT(20) NOT NULL,
                price VARCHAR(255) NOT NULL,
                sub_total DECIMAL(25) NOT NULL,
                UNIQUE (qi_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id)

            );
            """
            cursor.execute(query)
            conn.commit()
            print("Table 'items' created successfully.")
        else:
            print("Table 'items' already exists.")

    except mysql.connector.Error as err:
        print("Error creating table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def drop_items_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS items"
        cursor.execute(query)
        conn.commit()

        print("Table 'items' dropped successfully.")

    except mysql.connector.Error as err:
        print("Error dropping table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
create_items_table()
# drop_items_table()
