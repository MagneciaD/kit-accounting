import mysql.connector
from Resources.View.admin.dashboard_view import *
from Resources.View.profile_view import *


def authenticate_user(conn, email, password):
    cursor = conn.cursor()
    query = "SELECT user_id, email, password FROM users WHERE email=%s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user and user[2] == password:
        return True, user[2]  # Return user_id along with the authentication result
    else:
        return False, None

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email and password:
        db_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kit-accounting-db"
        )

        auth_result, user_id = authenticate_user(db_conn, email, password)
        db_conn.close()

    if auth_result:
        print("Login Successful. Welcome, {}!".format(email))
        return user_id

        # Retrieve and display user profile information
        display_user_info(user_id)

        while True:
            display_dash()
            choice = input("Enter your choice: ")

            if choice == "1":
                display_user_info(user_id)

            elif choice == "2":
                manage_products()

            elif choice == "3":
                manage_services()

            elif choice == "4":
                print("Logging out...")
                del active_sessions[session_id]
                return

            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Empty Fields. Please enter both email and password.")
        return None

def main():
    print("User Login")

    user_id = None
    while user_id is None:
        user_id = login()

    # Call your dashboard function here using the obtained user_id
    dash(user_id)

if __name__ == "__main__":
    login()

    # Close the database connection when done
    db.close()
