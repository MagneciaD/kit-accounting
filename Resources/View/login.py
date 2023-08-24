import mysql.connector
from Resources.View.dashboard_view import *


def authenticate_user(conn, email, password):
    cursor = conn.cursor()
    query = "SELECT email, password FROM users WHERE email=%s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user and user[1] == password:
        return True
    else:
        return False


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
            dash()
            break
        else:
            print("Login failed. Invalid email or password.")

    db_conn.close()


if __name__ == "__main__":
    fill_in()
