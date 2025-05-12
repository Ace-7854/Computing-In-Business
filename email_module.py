import smtplib
from email.message import EmailMessage
from env_module import get_email, get_password

def send_email(subject:str, body:str, to_email:str):
    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = get_email()
    msg['To'] = to_email

    # Connect to Gmail SMTP and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(get_email(), get_password())
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)
