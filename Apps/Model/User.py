from Database.Migrations.connection import create_connection

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values = (self.name, self.email, self.password)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("User created successfully!")
        except Exception as e:
            print(f"Error creating user: {e}")

        cursor.close()
        conn.close()

    def update(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s"
        values = (self.name, self.email, self.password, self.id)  # Assuming you have an 'id' attribute for each user

        try:
            cursor.execute(query, values)
            conn.commit()
            print("User updated successfully!")
        except Exception as e:
            print(f"Error updating user: {e}")

        cursor.close()
        conn.close()

    @staticmethod
    def read(user_id):
        conn = create_connection()
        cursor = conn.cursor()

        query = "SELECT id, name, email FROM users WHERE id = %s"
        values = (user_id,)

        try:
            cursor.execute(query, values)
            user_data = cursor.fetchone()
            if user_data:
                user = User(user_data[1], user_data[2], '')  # Pass an empty string for password for security reasons
                user.id = user_data[0]
                return user
            else:
                print("User not found.")
                return None
        except Exception as e:
            print(f"Error reading user: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def delete(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = "DELETE FROM users WHERE id = %s"
        values = (self.id,)  # Assuming you have an 'id' attribute for each user

        try:
            cursor.execute(query, values)
            conn.commit()
            print("User deleted successfully!")
        except Exception as e:
            print(f"Error deleting user: {e}")

        cursor.close()
        conn.close()
