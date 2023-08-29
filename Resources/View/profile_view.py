import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kit-accounting-db"
)

def display_user_info(user_id):
    cursor = db.cursor()
    query = """
        SELECT u.name, u.email,
               o.company_name, o.company_address, o.email_address,
               o.phone_no, o.website_link
        FROM users u
        JOIN organizations o ON u.user_id = o.user_id
        WHERE u.user_id = %s
    """
    cursor.execute(query, (user_id,))
    user_info = cursor.fetchone()
    cursor.close()

    print("Fetching user info for user ID:", user_id)  # Debugging line

    if user_info:
        print("User Information:")
        print(f"First Name: {user_info[0]}")
        print(f"Email: {user_info[1]}")
        print(f"Company Name: {user_info[2]}")
        print(f"Company Address: {user_info[3]}")
        print(f"Email Address: {user_info[4]}")
        print(f"Phone Number: {user_info[5]}")
        print(f"Website: {user_info[6] if user_info[6] else 'N/A'}")
    else:
        print("User not found.")
