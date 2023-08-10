from Database.Migrations.User_Table_Migration import create_users_table
from Database.Migrations.User_Table_Migration import drop_users_table
from Database.Migrations.Organizations_Table_Migration import create_organizations_table
from Database.Migrations.Organizations_Table_Migration import drop_organizations_table

MIGRATIONS_RUN_FLAG = False

def run_migrations():
    global MIGRATIONS_RUN_FLAG
    if not MIGRATIONS_RUN_FLAG:
        create_users_table()
        create_organizations_table()
        # call other migration functions here
        MIGRATIONS_RUN_FLAG = True
    else:
        print("Migrations have already been run.")
        drop_users_table()
        drop_organizations_table()

if __name__ == "__main__":
    run_migrations()
