from Database.Migrations.connection import create_connection

def create_client_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE Client (
    id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL UNIQUE,
    user_id INTEGER NOT NULL,
    org_id INT NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    client_address VARCHAR(255) NOT NULL,
    phone_no VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

    """
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def drop_client_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = "DROP TABLE IF EXISTS client"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()
