from csv_module import cls_csv
from database_module import database_manager
from env_module import get_conn_string, get_csv_file_path, get_reciever
from email_module import email_manager
import random


def display_all_items(records):
    for record in records:
        print(record)

def table_check(oracle_database:database_manager):
    tbls = oracle_database.get_all_tables()

    dept_tbl = False
    referral_tbl = False
    user_tbl = False

    for tbl in tbls:
        if tbl.lower() == "referral_tbl":
            referral_tbl = True
        elif tbl.lower() == "user_tbl":
            user_tbl = True
        elif tbl.lower() == "department_tbl":
            dept_tbl = True
    
    if not dept_tbl:
        oracle_database.create_department()
    if not referral_tbl:
        oracle_database.create_referral()
    if not user_tbl:
        oracle_database.create_user()

    for tbl in tbls:
        if tbl.lower() != "referral_tbl" and tbl.lower() != "user_tbl" and tbl.lower() != "department_tbl":
            oracle_database.drop_tbl(tbl)

def main():
    # csv = cls_csv(get_csv_file_path())
    # display_all_items(csv.read_csv())

    oracle_database = database_manager(get_conn_string())
    table_check(oracle_database)
    # email_sender = email_manager(get_reciever())
    # email_sender.get_hr_conf()

    print(oracle_database.get_user_by_email("SmitHa.FinBAE@gmail.com"))

    oracle_database.close_connection()

if __name__ == "__main__":
    main()