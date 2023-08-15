from Database.Migrations.connection import create_connection

def create_items_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        qi_id VARCHAR(255),
        user_id INT(255),
        name VARCHAR(255),
        item_quality INT(20),
        price VARCHAR(255),
        sub_total DECIMAL(25)
        
    )
    """
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def drop_items_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = "DROP TABLE IF EXISTS items"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()
