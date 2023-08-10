from Database.Migrations.connection import create_connection

def create_users_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255)
    )
    """
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def drop_users_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = "DROP TABLE IF EXISTS users"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()
