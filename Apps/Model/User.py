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
