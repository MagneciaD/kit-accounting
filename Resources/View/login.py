import mysql.connector
from Resources.View.dashboard_view import *


def authenticate_user(conn, email, password):
    cursor = conn.cursor()
    query = "SELECT user_id, email, password FROM users WHERE email=%s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user and user[2] == password:
        return True, user[0]  # Return user_id along with the authentication result
    else:
        return False, None

def fill_in():
    db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kit-accounting-db"
    )

    print("Login Page")

    while True:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if authenticate_user(db_conn, email, password):
            print("Login successful. Welcome, {}!".format(email))
            auth_result, user_id = authenticate_user(db_conn, email, password)
            if auth_result:
                dash(user_id)
                break
        else:
            print("Login failed. Invalid email or password.")

    db_conn.close()


if __name__ == "__main__":
    fill_in()