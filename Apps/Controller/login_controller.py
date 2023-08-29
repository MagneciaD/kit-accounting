import mysql.connector
import tkinter as tk
from Resources.View.admin.dashboard_view import dash
from Resources.View.profile_view import display_user_info

def authenticate_user(conn, email, password):
    cursor = conn.cursor()
    query = "SELECT user_id, email, password FROM users WHERE email=%s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user and user[2] == password:
        return True, user[0]  # Return user_id along with the authentication result
    else:
        return False, None

def login(email, password):
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
        else:
            print("Login failed. Please check your credentials.")
            return None
    else:
        print("Empty Fields. Please enter both email and password.")
        return None




