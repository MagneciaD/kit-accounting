from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_organizations_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        table_name = 'organizations'

        if not table_exists(cursor, table_name):
            query = """
            CREATE TABLE organizations (
                id INT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
                org_id VARCHAR(20) NOT NULL,
                user_id VARCHAR(20) NOT NULL,
                company_name VARCHAR(30) NOT NULL,
                company_address VARCHAR(255) NOT NULL,
                email_address VARCHAR(20) NOT NULL,
                company_logo VARCHAR(20) NOT NULL,
                phone_no INT(20) NOT NULL,
                website_link VARCHAR(255),
                PRIMARY KEY (id),
                UNIQUE (org_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
            """
            cursor.execute(query)
            conn.commit()
            print("Table 'organizations' created successfully.")
        else:
            print("Table 'organizations' already exists.")

    except mysql.connector.Error as err:
        print("Error creating table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def drop_organizations_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS organizations"
        cursor.execute(query)
        conn.commit()

        print("Table 'organizations' dropped successfully.")

    except mysql.connector.Error as err:
        print("Error dropping table: {}".format(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
create_organizations_table()
# drop_organizations_table()
