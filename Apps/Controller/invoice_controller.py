from Database.Migrations.connection import create_connection
import mysql.connector
from mysql.connector import errorcode

def table_exists(cursor, table_name):
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

def create_invoice(invoice_data):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO invoice (
            invoice_id, client_id, user_id, org_id, qi_id, invoice_date,
            vat, tot_price, pay_status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (
            invoice_data['invoice_id'], invoice_data['client_id'],
            invoice_data['user_id'], invoice_data['org_id'],
            invoice_data['qi_id'], invoice_data['invoice_date'],
            invoice_data['vat'], invoice_data['tot_price'],
            invoice_data['pay_status']
        )
        cursor.execute(query, data)
        conn.commit()

        print("Invoice created successfully.")

    except mysql.connector.Error as err:
        print("Error creating invoice:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def read_invoice(invoice_id):
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM invoice WHERE invoice_id = %s"
        cursor.execute(query, (invoice_id,))
        invoice = cursor.fetchone()

        if invoice:
            return invoice
        else:
            print("Invoice not found.")
            return None

    except mysql.connector.Error as err:
        print("Error reading invoice:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_invoice(invoice_id, new_data):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        UPDATE invoice
        SET
            client_id = %s,
            user_id = %s,
            org_id = %s,
            qi_id = %s,
            invoice_date = %s,
            vat = %s,
            tot_price = %s,
            pay_status = %s
        WHERE invoice_id = %s
        """
        data = (
            new_data['client_id'], new_data['user_id'], new_data['org_id'],
            new_data['qi_id'], new_data['invoice_date'], new_data['vat'],
            new_data['tot_price'], new_data['pay_status'], invoice_id
        )
        cursor.execute(query, data)
        conn.commit()

        print("Invoice updated successfully.")

    except mysql.connector.Error as err:
        print("Error updating invoice:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_invoice(invoice_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "DELETE FROM invoice WHERE invoice_id = %s"
        cursor.execute(query, (invoice_id,))
        conn.commit()

        print("Invoice deleted successfully.")

    except mysql.connector.Error as err:
        print("Error deleting invoice:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the functions as needed
# create_invoice_table()
# drop_invoice_table()

# Example usage:
create_invoice({
    'invoice_id': 'inv123',
    'client_id': 'client456',
    'user_id': 'user789',
    'org_id': 'org123',
    'qi_id': 'item456',
    'invoice_date': '2023-08-16 10:00:00',
    'vat': 10.0,
    'tot_price': 100.0,
    'pay_status': 'Paid'
})

# invoice = read_invoice('inv123')
# if invoice:
#     print("Invoice:", invoice)

# update_invoice('inv123', {
#     'client_id': 'client789',
#     'user_id': 'user123',
#     'org_id': 'org456',
#     'qi_id': 'item789',
#     'invoice_date': '2023-08-17 09:00:00',
#     'vat': 15.0,
#     'tot_price': 150.0,
#     'pay_status': 'Pending'
# })

# delete_invoice('inv123')
