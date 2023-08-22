import mysql.connector

from Resources.View.dashboard_view import *

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kit-accounting-db"
)

def authenticate(email, password):
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    cursor.close()
    return user


def fill_in():
    print("Login Page")
    username = input("Email: ")
    password = input("Password: ")

    user = authenticate(username, password)

    if user:
        print("Welcome to K.I.T")
        dash()  # Call the main function from the dashboard_view module
    else:
        print("Invalid credentials.")

if __name__ == "__main__":
    fill_in()
