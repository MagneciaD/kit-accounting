from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_services_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        table_name = 'services'

        if not table_exists(cursor, table_name):
            query = """
            CREATE TABLE services (
                id INT AUTO_INCREMENT PRIMARY KEY,
                service_id VARCHAR(20) NOT NULL,
                user_id VARCHAR(20) NOT NULL,
                service_name VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                price FLOAT(20.1) NOT NULL,
                UNIQUE (service_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            );
            """
            cursor.execute(query)
            conn.commit()
            print("Table 'services' created successfully.")
        else:
            print("Table 'services' already exists.")

    except mysql.connector.Error as err:
        print("Error creating table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def drop_services_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS services"
        cursor.execute(query)
        conn.commit()

        print("Table 'services' dropped successfully.")

    except mysql.connector.Error as err:
        print("Error dropping table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
create_services_table()
# drop_services_table()
