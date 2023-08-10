from Database.Migrations.connection import create_connection

def create_organizations_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE Organization (
    id INT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    org_id VARCHAR(255) NOT NULL,
    user_id INT(20) UNSIGNED NOT NULL,
    company_name VARCHAR(30) NOT NULL,
    company_address VARCHAR(255) NOT NULL,
    email_address VARCHAR(20) NOT NULL,
    company_logo VARCHAR(20) NOT NULL,
    phone_no TEXT NOT NULL,
    website_link VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE (org_id),
    FOREIGN KEY (user_id) REFERENCES User(id)
)

    """
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def drop_organizations_table():
    conn = create_connection()
    cursor = conn.cursor()

    query = "DROP TABLE IF EXISTS users"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()