from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

class Service:
    def __init__(self, service_id, user_id, service_name, description, price):
        self.service_id = service_id
        self.user_id = user_id
        self.service_name = service_name
        self.description = description
        self.price = price

    def save(self):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO services (service_id, user_id, service_name, description, price)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (self.service_id, self.user_id, self.service_name, self.description, self.price)

            cursor.execute(query, values)
            conn.commit()
            print("Service created successfully.")

        except mysql.connector.Error as err:
            print("Error creating service: {}".format(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def read_all():
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = "SELECT * FROM services"
            cursor.execute(query)
            service_data_list = cursor.fetchall()

            services = []
            for service_data in service_data_list:
                service = Service(service_data[0], service_data[1], service_data[2], service_data[3], service_data[4])
                services.append(service)

            return services

        except mysql.connector.Error as err:
            print("Error reading services: {}".format(err))
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = """
            UPDATE services
            SET user_id = %s, service_name = %s, description = %s, price = %s
            WHERE service_id = %s
            """
            values = (self.user_id, self.service_name, self.description, self.price, self.service_id)

            cursor.execute(query, values)
            conn.commit()
            print("Service updated successfully.")

        except mysql.connector.Error as err:
            print("Error updating service: {}".format(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def read(service_id):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = "SELECT * FROM services WHERE service_id = %s"
            values = (service_id,)

            cursor.execute(query, values)
            service_data = cursor.fetchone()

            if service_data:
                service = Service(service_data[0], service_data[1], service_data[2], service_data[3], service_data[4])
                return service
            else:
                print("Service not found.")
                return None

        except mysql.connector.Error as err:
            print("Error reading service: {}".format(err))
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def delete(service_id):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            query = "DELETE FROM services WHERE s_id = %s"
            values = (service_id,)

            cursor.execute(query, values)
            conn.commit()
            print("Service deleted successfully.")

        except mysql.connector.Error as err:
            print("Error deleting service: {}".format(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
