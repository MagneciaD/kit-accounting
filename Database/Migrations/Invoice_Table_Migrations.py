from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_invoice_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        table_name = 'invoice'

        if not table_exists(cursor, table_name):
            query = """
            CREATE TABLE invoice (
                id INT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
                invoice_id VARCHAR(255) NOT NULL,
                client_id INT(20) UNSIGNED NOT NULL,
                user_id INT(20) UNSIGNED NOT NULL,
                org_id VARCHAR(20) NOT NULL,
                invoice_date DATETIME NOT NULL,
                vat DECIMAL(10,2) NOT NULL,
                tot_price DECIMAL(8,2) NOT NULL,
                pay_status VARCHAR(255) NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                PRIMARY KEY (id),
                UNIQUE (invoice_id)
            )
            """
            cursor.execute(query)
            conn.commit()
            print("Table 'invoice' created successfully.")
        else:
            print("Table 'invoice' already exists.")

    except mysql.connector.Error as err:
        print("Error creating table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def drop_invoice_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS invoice"
        cursor.execute(query)
        conn.commit()

        print("Table 'invoice' dropped successfully.")

    except mysql.connector.Error as err:
        print("Error dropping table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
create_invoice_table()
# drop_invoice_table()
