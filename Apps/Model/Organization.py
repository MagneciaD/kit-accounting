from Database.Migrations.connection import create_connection
import mysql.connector

class Organization:
    def __init__(self, org_id, user_id, company_name, company_address, email_address, company_logo, phone_no, website_link=None):
        self.org_id = org_id
        self.user_id = user_id
        self.company_name = company_name
        self.company_address = company_address
        self.email_address = email_address
        self.company_logo = company_logo
        self.phone_no = phone_no
        self.website_link = website_link
        self.user_id = user_id

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO organizations (org_id, user_id, company_name, company_address, email_address, company_logo, phone_no, website_link)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            self.org_id, self.user_id, self.company_name, self.company_address,
            self.email_address, self.company_logo, self.phone_no, self.website_link
        )

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Organization created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating organization: {err}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read(org_id):
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        SELECT org_id, user_id, company_name, company_address, email_address, company_logo, phone_no, website_link
        FROM organizations WHERE org_id = %s
        """
        values = (org_id,)

        try:
            cursor.execute(query, values)
            org_data = cursor.fetchone()
            if org_data:
                org = Organization(*org_data)
                return org
            else:
                print("Organization not found.")
                return None
        except mysql.connector.Error as err:
            print(f"Error reading organization: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    def update(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        UPDATE organizations
        SET user_id = %s, company_name = %s, company_address = %s, email_address = %s,
        company_logo = %s, phone_no = %s, website_link = %s
        WHERE org_id = %s
        """
        values = (
            self.user_id, self.company_name, self.company_address, self.email_address,
            self.company_logo, self.phone_no, self.website_link, self.org_id
        )

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Organization updated successfully!")
        except mysql.connector.Error as err:
            print(f"Error updating organization: {err}")
        finally:
            cursor.close()
            conn.close()

    def delete(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = "DELETE FROM organizations WHERE org_id = %s"
        values = (self.org_id,)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Organization deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error deleting organization: {err}")
        finally:
            cursor.close()
            conn.close()
