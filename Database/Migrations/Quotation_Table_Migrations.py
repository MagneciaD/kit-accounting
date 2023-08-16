from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_quotation_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        table_name = 'Quotation'

        if not table_exists(cursor, table_name):
            query = """
            CREATE TABLE Quotation (
                id INT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
                quotation_id VARCHAR(255) NOT NULL,
                user_id VARCHAR(20) NOT NULL,
                org_id VARCHAR(20) NOT NULL,
                qi_id VARCHAR(20) NOT NULL,
                quotation_date DATE NOT NULL,
                validity_period DATE NOT NULL,
                quote_status VARCHAR(255) NOT NULL,
                vat DECIMAL(10, 2) NOT NULL,
                total DECIMAL(10, 2) NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                PRIMARY KEY (id),
                UNIQUE KEY (quotation_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (org_id) REFERENCES organizations(org_id),
                FOREIGN KEY (qi_id) REFERENCES items(qi_id)


            );
            """
            cursor.execute(query)
            conn.commit()
            print("Table 'Quotation' created successfully.")
        else:
            print("Table 'Quotation' already exists.")

    except mysql.connector.Error as err:
        print("Error creating table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def drop_quotation_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS Quotation"
        cursor.execute(query)
        conn.commit()

        print("Table 'Quotation' dropped successfully.")

    except mysql.connector.Error as err:
        print("Error dropping table:{}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
# Call the functions as needed
create_quotation_table()
# drop_items_table()