from Database.Migrations.connection import create_connection

class Organization:
    def __init__(self, org_id, user_id, company_name, company_address, email_address, phone_no, website_link):
        self.org_id = org_id
        self.user_id = user_id
        self.company_name = company_name
        self.company_address = company_address
        self.email_address = email_address
        self.phone_no = phone_no
        self.website_link = website_link

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        # Check if org_id is unique
        org_id_query = "SELECT COUNT(*) FROM organizations WHERE org_id = %s"
        cursor.execute(org_id_query, (self.org_id,))
        if cursor.fetchone()[0] > 0:
            print("Error: org_id already exists.")
            cursor.close()
            conn.close()
            return

        # Check if user_id is unique
        user_id_query = "SELECT COUNT(*) FROM organizations WHERE user_id = %s"
        cursor.execute(user_id_query, (self.user_id,))
        if cursor.fetchone()[0] > 0:
            print("Error: user_id already exists.")
            cursor.close()
            conn.close()
            return

        # Insert data if both org_id and user_id are unique
        query = "INSERT INTO organizations (org_id, user_id, company_name, company_address, email_address, phone_no, website_link) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (self.org_id, self.user_id, self.company_name, self.company_address, self.email_address, self.phone_no, self.website_link)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Organization created successfully!")
        except Exception as e:
            print(f"Error creating organization: {e}")

        cursor.close()
        conn.close()

    @classmethod
    def find_by_id(cls, org_id):
        conn = create_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM organizations WHERE org_id = %s"
        cursor.execute(query, (org_id,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            return cls(*result)
        else:
            return None

    def update(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = "UPDATE organizations SET company_name = %s, company_address = %s, email_address = %s, phone_no = %s, website_link = %s WHERE org_id = %s"
        values = (self.company_name, self.company_address, self.email_address, self.phone_no, self.website_link, self.org_id)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Organization updated successfully!")
        except Exception as e:
            print(f"Error updating organization: {e}")

        cursor.close()
        conn.close()

    def delete(self):
        conn = create_connection()
        cursor = conn.cursor()

        query = "DELETE FROM organizations WHERE org_id = %s"
        cursor.execute(query, (self.org_id,))
        conn.commit()
        print("Organization deleted successfully!")

        cursor.close()
        conn.close()

# Usage
# Create
org = Organization(
    org_id=1,
    user_id=1,
    company_name="Example Company",
    company_address="123 Main St, City",
    email_address="info@example.com",
    phone_no="123-456-7890",
    website_link="https://www.google.com"
)

org.save()

# Read
org_retrieved = Organization.find_by_id(1)
if org_retrieved:
    print("Organization found:", org_retrieved.company_name)
else:
    print("Organization not found.")

# Update
org_retrieved.company_name = "Updated Company Name"
org_retrieved.update()

# Delete
org_retrieved.delete()
