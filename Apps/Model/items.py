from Database.Migrations.connection import create_connection
import mysql.connector

class Items:
    def __init__(self, qi_id, user_id, name, item_quality, price, sub_total):
        self.qi_id = qi_id
        self.user_id = user_id
        self.name = name
        self.item_quality = item_quality
        self.price = price
        self.sub_total = sub_total

    def save(self):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO items (qi_id, user_id, name, item_quality, price, sub_total)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (self.qi_id, self.user_id, self.name, self.item_quality, self.price, self.sub_total)

            cursor.execute(query, values)
            conn.commit()
            print("Item saved successfully.")

        except mysql.connector.Error as err:
            print("Error saving item: {}".format(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # Implement other CRUD methods like update, read, and delete here

# Example usage:
item = Items("qi123", "user123", "Item Name", 3, "10.99", "32.97")
item.save()
