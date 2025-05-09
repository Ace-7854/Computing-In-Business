from csv_module import cls_csv
from database_module import database_manager, table, new_table
from env_module import get_conn_string, get_file_path

def display_all_items(records):
    for record in records:
        print(record)
        print('\n')

def main():
    csv = cls_csv(get_file_path())
    display_all_items(csv.read_csv())

    oracle_database = database_manager(get_conn_string())

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