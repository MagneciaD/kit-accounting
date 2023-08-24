import mysql.connector
from Resources.View.dashboard_view import *


def services_in():
    db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kit-accounting-db"
    )

    print("Services Page")

    while True:
        add_service = input("Enter a service: ")
        description = input("Enter service description: ")
        price = input("Enter service price: ")


if __name__ == "__main__":
    services_in()
