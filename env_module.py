import os
from dotenv import load_dotenv

def get_conn_string() -> str:
    load_dotenv()

    return os.environ['connection_string']

def get_csv_file_path() -> str:
    load_dotenv()

    return os.environ['csv_file_path']


# submission_txt_pth=assets/emails/Submisssion_email.txt
# hr_recieved_txt_path=assets/emails/hr_recieved_ref.txt
# hr_response_app=assets/emails/hr_response_approved.txt
# hr_response_den=assets/emails/hr_response_denied.txt

def get_email():
    load_dotenv()

    return os.environ['email']

def get_password():
    load_dotenv()

    return os.environ['email_pass']

def get_reciever():
    load_dotenv()

    return os.environ['reciever']