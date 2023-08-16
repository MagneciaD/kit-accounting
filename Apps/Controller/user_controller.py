from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_user(user_data):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO users (user_id, name, email, password)
        VALUES (%s, %s, %s, %s)
        """
        data = (user_data['user_id'], user_data['name'], user_data['email'], user_data['password'])
        cursor.execute(query, data)
        conn.commit()

        print("User created successfully.")

    except mysql.connector.Error as err:
        print("Error creating user:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def read_user(user_id):
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

        if user:
            return user
        else:
            print("User not found.")
            return None

    except mysql.connector.Error as err:
        print("Error reading user:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_user(user_id, new_data):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        UPDATE users
        SET name = %s, email = %s, password = %s
        WHERE user_id = %s
        """
        data = (new_data['name'], new_data['email'], new_data['password'], user_id)
        cursor.execute(query, data)
        conn.commit()

        print("User updated successfully.")

    except mysql.connector.Error as err:
        print("Error updating user:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_user(user_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DELETE FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()

        print("User deleted successfully.")

    except mysql.connector.Error as err:
        print("Error deleting user:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
# create_users_table()
# drop_users_table()

# Example usage:
# create_user({
#     'user_id': 'user123',
#     'name': 'John Doe',
#     'email': 'john@example.com',
#     'password': 'securepass'
# })

# user = read_user('user123')
# if user:
#     print("User:", user)

# update_user('user123', {
#     'name': 'Jane Smith',
#     'email': 'jane@example.com',
#     'password': 'newpass'
# })

# delete_user('user123')
