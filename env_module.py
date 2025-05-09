import os
from dotenv import load_dotenv

def get_conn_string() -> str:
    load_dotenv()

    return os.environ['connection_string']

def get_file_path() -> str:
    load_dotenv()

    return os.environ['csv_file_path']