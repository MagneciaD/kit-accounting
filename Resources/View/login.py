import mysql.connector
from Resources.View.dashboard_view import *

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kit-accounting-db"
)

# Dictionary to store active sessions
active_sessions = {}

def authenticate(email, password):
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    cursor.close()
    return user

def create_session(user_id):
    session_id = len(active_sessions) + 1
    active_sessions[session_id] = user_id
    return session_id

def fill_in():

    print("Login Page")
    username = input("Email: ")
    password = input("Password: ")

    user = authenticate(username, password)

    if user:
        print("Welcome to K.I.T")
        session_id = create_session(user[0])
        dash(session_id)  # Call the main function from the dashboard_view module
    else:
        print("Invalid credentials.")

def dash(session_id):
    user_id = active_sessions.get(session_id)

    if user_id is not None:
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        cursor.close()

        # Retrieve organization data using user_id

    if user:
        email = 3  # Assuming index 3 corresponds to the "username" (email) column
        print(f"Hello, {user[email]}!")
        while True:
            display_dash()
            choice = input("Enter your choice: ")

            if choice == "1":
                manage_profiles()

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
        print("Session expired or user not logged in.")


if __name__ == "__main__":
    fill_in()
