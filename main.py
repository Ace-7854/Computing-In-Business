from csv_module import cls_csv
from database_module import database_manager, table, new_table
from env_module import get_conn_string, get_csv_file_path, get_reciever
from email_module import email_manager

def display_all_items(records):
    for record in records:
        print(record)

def table_check(oracle_database:database_manager):
    tbls = oracle_database.get_all_tables()

    dept_tbl = False
    dept_em_tbl = False
    user_tbl = False

    for tbl in tbls:
        if tbl.lower() == "departmentemail_tbl":
            dept_em_tbl = True
        elif tbl.lower() == "user_tbl":
            user_tbl = True
        elif tbl.lower() == "department_tbl":
            dept_tbl = True
    
    if not dept_tbl:
        oracle_database.create_tbl_dept()
    if not dept_em_tbl:
        oracle_database.create_tbl_dept_email()
    if not user_tbl:
        oracle_database.create_tbl_user()    

    for tbl in tbls:
        if tbl.lower() != "departmentemail_tbl" and tbl.lower() != "user_tbl" and tbl.lower() != "department_tbl":
            oracle_database.drop_tbl(tbl)

def main():
    csv = cls_csv(get_csv_file_path())
    display_all_items(csv.read_csv())

    oracle_database = database_manager(get_conn_string())
    table_check(oracle_database)

    email_sender = email_manager(get_reciever())

    oracle_database.close_connection()
    
"""
index 0: Full Name
Index 1: Email
Index 2: Alphanumeric  
Index 3: Employee Start Date
Index 4: Current Line Manager
Index 5: Line Manager Department
Index 6: Department
Index 7: Department email
"""

if __name__ == "__main__":
    main()