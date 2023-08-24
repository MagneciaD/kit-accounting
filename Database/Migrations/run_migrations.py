from Database.Migrations.User_Table_Migrations import create_users_table
from Database.Migrations.User_Table_Migrations import drop_users_table
from Database.Migrations.Organization_Table_Migrations import create_organizations_table
from Database.Migrations.Organization_Table_Migrations import drop_organizations_table
from Database.Migrations.Invoice_Table_Migrations import create_invoice_table
from Database.Migrations.Invoice_Table_Migrations import drop_invoice_table
from Database.Migrations.Client_Table_Migrations import create_clients_table
from Database.Migrations.Client_Table_Migrations import drop_clients_table
from Database.Migrations.Items_Table_Migrations import create_items_table
from Database.Migrations.Items_Table_Migrations import drop_items_table
from Database.Migrations.Quotation_Table_Migrations import create_quotation_table
from Database.Migrations.Quotation_Table_Migrations import drop_quotation_table
from Database.Migrations.Services_Table_Migrations import create_services_table
from Database.Migrations.Services_Table_Migrations import drop_services_table

MIGRATIONS_RUN_FLAG = False


def run_migrations():
    global MIGRATIONS_RUN_FLAG
    if not MIGRATIONS_RUN_FLAG:
        create_users_table()
        create_organizations_table()
        create_invoice_table()
        create_clients_table()
        create_items_table()
        create_quotation_table()
        create_services_table()
        # call other migration functions here
        MIGRATIONS_RUN_FLAG = True
    else:
        print("Migrations have already been run.")
        drop_users_table()
        drop_organizations_table()
        drop_invoice_table()
        drop_clients_table()
        drop_items_table()
        drop_quotation_table()
        drop_services_table()

if __name__ == "__main__":
    run_migrations()
