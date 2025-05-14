import os
from dotenv import load_dotenv

def get_conn_string() -> str:
    load_dotenv()

    return os.environ['connection_string']

def get_csv_file_path() -> str:
    load_dotenv()

    return os.environ['csv_file_path']

def get_email():
    load_dotenv()

    return os.environ['email']

def get_password():
    load_dotenv()

    return os.environ['email_pass']

def get_reciever():
    load_dotenv()

    return os.environ['reciever']