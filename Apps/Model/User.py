from Database.Migrations.connection import create_connection

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = "INSERT INTO users (user_id, name, email, password) VALUES (%s, %s, %s, %s)"
        values = (self.user_id, self.name, self.email, self.password)

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
        values = (self.name, self.email, self.password, self.user_id)  # Use self.user_id instead of self.id

        try:
            cursor.execute(query, values)
            conn.commit()
            print("User updated successfully!")
        except Exception as e:
            print(f"Error updating user: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read_all():
        conn = create_connection()
        cursor = conn.cursor()

        query = "SELECT id, name, email FROM users"

        try:
            cursor.execute(query)
            user_data_list = cursor.fetchall()
            users = []
            for user_data in user_data_list:

                user = User(user_data[0], user_data[1], user_data[2], '')  # Pass an empty string for password for security reasons
                user.id = user_data[0]
                users.append(user)
            return users
        except Exception as e:
            print(f"Error reading users: {e}")
            return []

        finally:
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
                user = User(user_data[0], user_data[1], user_data[2], '')  # Pass an empty string for password for security reasons
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

    @staticmethod
    def delete_by_id(user_id):
        conn = create_connection()
        cursor = conn.cursor()

        query = "DELETE FROM users WHERE id = %s"
        values = (user_id,)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("User deleted successfully!")
        except Exception as e:
            print(f"Error deleting user: {e}")

        cursor.close()
        conn.close()