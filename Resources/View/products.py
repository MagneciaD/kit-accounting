import mysql.connector
from Resources.View.dashboard_view import *


def products_in():
    db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kit-accounting-db"
    )

    print("Products Page")

    while True:
        add_product = input("Enter a Product: ")
        description = input("Enter service Description: ")
        price = input("Enter service Price: ")
        break


if __name__ == "__main__":
    products_in()
