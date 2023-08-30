from Database.Migrations.connection import create_connection

class Client:
    def __init__(self, client_id, user_id, first_name, last_name, email, client_address, phone_no, timestamp):
        self.client_id = client_id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.client_address = client_address
        self.phone_no = phone_no
        self.timestamp = timestamp

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO clients (client_id, user_id, first_name, last_name, email, client_address, phone_no, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (self.client_id, self.user_id, self.first_name, self.last_name, self.email,
                  self.client_address, self.phone_no, self.timestamp)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Client saved successfully!")
        except Exception as e:
            print(f"Error saving client: {e}")

        cursor.close()
        conn.close()

    def update(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        UPDATE clients
        SET user_id = %s, first_name = %s, last_name = %s, email = %s, client_address = %s, phone_no = %s, timestamp = %s
        WHERE client_id = %s
        """
        values = (self.user_id, self.first_name, self.last_name, self.email, self.client_address,
                  self.phone_no, self.timestamp, self.client_id)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Client updated successfully!")
        except Exception as e:
            print(f"Error updating client: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read_all():
        conn = create_connection()
        cursor = conn.cursor()

        query = "SELECT client_id, user_id, first_name, last_name, email, client_address, phone_no, timestamp FROM clients"

        try:
            cursor.execute(query)
            client_data_list = cursor.fetchall()
            clients = []
            for client_data in client_data_list:
                client = Client(client_data[0], client_data[1], client_data[2], client_data[3], client_data[4],
                                client_data[5], client_data[6], client_data[7])
                clients.append(client)
            return clients
        except Exception as e:
            print(f"Error reading clients: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read_by_client_id(client_id):
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        SELECT client_id, user_id, first_name, last_name, email, client_address, phone_no, timestamp
        FROM clients
        WHERE client_id = %s
        """
        values = (client_id,)

        try:
            cursor.execute(query, values)
            client_data = cursor.fetchone()
            if client_data:
                client = Client(client_data[0], client_data[1], client_data[2], client_data[3], client_data[4],
                                client_data[5], client_data[6], client_data[7])
                return client
            else:
                print("Client not found.")
                return None
        except Exception as e:
            print(f"Error reading client: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_by_client_id(client_id):
        conn = create_connection()
        cursor = conn.cursor()

        query = "DELETE FROM clients WHERE client_id = %s"
        values = (client_id,)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Client deleted successfully!")
        except Exception as e:
            print(f"Error deleting client: {e}")
        finally:
            cursor.close()
            conn.close()
