from Database.Migrations.connection import create_connection
import mysql.connector

class Item:
    def __init__(self, qi_id, user_id, name, item_quality, price, sub_total):
        self.qi_id = qi_id
        self.user_id = user_id
        self.name = name
        self.item_quantity = item_quality
        self.price = price
        self.sub_total = sub_total


    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO items (qi_id, user_id, name, item_quality, price, sub_total)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (self.qi_id, self.user_id, self.name, self.item_quality, self.price, self.sub_total)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Item saved successfully!")
        except Exception as e:
            print(f"Error saving item: {e}")

        cursor.close()
        conn.close()

    def update(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        UPDATE items
        SET user_id = %s, name = %s, item_quality = %s, price = %s, sub_total = %s
        WHERE qi_id = %s
        """
        values = (self.user_id, self.name, self.item_quality, self.price, self.sub_total, self.qi_id)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Item updated successfully!")
        except Exception as e:
            print(f"Error updating item: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read_all():
        conn = create_connection()
        cursor = conn.cursor()

        query = "SELECT qi_id, user_id, name, item_quality, price, sub_total FROM items"

        try:
            cursor.execute(query)
            item_data_list = cursor.fetchall()
            items = []
            for item_data in item_data_list:
                item = Item(item_data[0], item_data[1], item_data[2], item_data[3], item_data[4], item_data[5])
                items.append(item)
            return items
        except Exception as e:
            print(f"Error reading items: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read_by_qi_id(qi_id):
        conn = create_connection()
        cursor = conn.cursor()

        query = "SELECT qi_id, user_id, name, item_quality, price, sub_total FROM items WHERE qi_id = %s"
        values = (qi_id,)

        try:
            cursor.execute(query, values)
            item_data = cursor.fetchone()
            if item_data:
                item = Item(item_data[0], item_data[1], item_data[2], item_data[3], item_data[4], item_data[5])
                return item
            else:
                print("Item not found.")
                return None
        except Exception as e:
            print(f"Error reading item: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_by_qi_id(qi_id):
        conn = create_connection()
        cursor = conn.cursor()

        query = "DELETE FROM items WHERE qi_id = %s"
        values = (qi_id,)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Item deleted successfully!")
        except Exception as e:
            print(f"Error deleting item: {e}")
        finally:
            cursor.close()
            conn.close()
