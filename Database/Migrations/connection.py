import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='kit-accounting-db'
    )
    return conn
