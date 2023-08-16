from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_clients_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        table_name = 'clients'

        if not table_exists(cursor, table_name):
            query = """
            CREATE TABLE clients (
                id INTEGER PRIMARY KEY,
                client_id VARCHAR(20) NOT NULL UNIQUE,
                user_id VARCHAR(20) NOT NULL,
                org_id VARCHAR(20) NOT NULL,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                client_address VARCHAR(255) NOT NULL,
                phone_no VARCHAR(255) NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                UNIQUE (client_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (org_id) REFERENCES organizations(org_id)
                

            );
            """
            cursor.execute(query)
            conn.commit()
            print("Table 'clients' created successfully.")
        else:
            print("Table 'clients' already exists.")

    except mysql.connector.Error as err:
        print("Error creating table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def drop_clients_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS clients"
        cursor.execute(query)
        conn.commit()

        print("Table 'clients' dropped successfully.")

    except mysql.connector.Error as err:
        print("Error dropping table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
create_clients_table()
# drop_clients_table()
