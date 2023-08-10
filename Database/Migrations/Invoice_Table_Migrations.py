from Database.Migrations.connection import create_connection

def create_invoice_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE Invoice (
    id INT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    invoice_id VARCHAR(255) NOT NULL,
    client_id INT(20) UNSIGNED NOT NULL,
    user_id INT(20) UNSIGNED NOT NULL,
    org_id VARCHAR(20) NOT NULL,
    invoice_date DATETIME NOT NULL,
    vat DECIMAL(10,2) NOT NULL,
    tot_price DECIMAL(8,2) NOT NULL,
    pay_status VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (invoice_id),
    FOREIGN KEY (client_id) REFERENCES Client(id),
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (org_id) REFERENCES Organization(id)
)

    """
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def drop_invoice_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = "DROP TABLE IF EXISTS users"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()
