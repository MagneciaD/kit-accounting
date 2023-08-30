import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kit-accounting-db"
)

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def update(self):
        cursor = db.cursor()
        query = """
                   UPDATE users
                   SET name = %s, email = %s, password = %s
                   WHERE user_id = %s
               """
        values = (self.name, self.email, self.password, self.user_id)
        cursor.execute(query, values)
        db.commit()  # Commit the changes to the database
        cursor.close()
        print("User information updated successfully.")
        pass

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

    print("Fetching user info for user ID:", user_id)

    if user_info:
        print("User Information:")
        print(f"First Name: {user_info[0]}")
        print(f"Email: {user_info[1]}")
        print()
        print("Organization Information:")
        print(f"Company Name: {user_info[2]}")
        print(f"Company Address: {user_info[3]}")
        print(f"Email Address: {user_info[4]}")
        print(f"Phone Number: {user_info[5]}")
        print(f"Website: {user_info[6] if user_info[6] else 'N/A'}")
    else:
        print("User not found.")

def update_user_info(user_id):
    name = input("Enter the new name: ")
    email = input("Enter the new email: ")
    password = input("Enter the new password: ")

    user = User(user_id, name, email, password)
    user.update()

def display_user_profile(user_id):
    print("Profile:")
    print("1. Edit User")
    print("2. Edit Organization")
    print("exit. Exit")

def profile_dashboard(user_id):
    while True:
        display_user_profile(user_id)
        choice = input("Enter your choice: ")

        if choice == "1":
            update_user_info(user_id)
        elif choice == "exit":
            break

if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    display_user_info(user_id)
    profile_dashboard(user_id)

    db.close()  # Close the database connection
