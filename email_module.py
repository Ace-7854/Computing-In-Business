import smtplib
from email.message import EmailMessage
from env_module import get_email, get_password

class email_manager:
    def __init__(self,reciever):
        self.reciever = reciever

    def get_email_approval(self):
        pass

    def get_email_denied(self):
        pass

    def get_hr_conf(self):
        pass

    def get_email_submission(self, name, dept, ref_reason):
        subject = """Referral Submission Confirmation – Occupational Health"""
        
        body = f"""\
        Dear {name},
        
        Thank you for submitting a referral to the Occupational Health service.
        
        We confirm that your referral for Jane Doe has been successfully received on 12 May 2025 at 10:15 AM. The Occupational Health team will now begin processing the referral and will be in touch if further information is required.
        
        Referral Details:
        - Employee Name: {name}
        - Department: {dept}
        - Reason for Referral: {ref_reason}
        
        You will receive an update once the referral has been reviewed and the appointment is scheduled.
        
        If you have any questions or need to make changes to the referral, please contact the Occupational Health team at ohsupport@example.com quoting the reference number REF-001245.
        
        Thank you,  
        Occupational Health Services  
        BAE Systems
        """
        self.send_email(subject, body, self.reciever)

    def send_email(self, subject:str, body:str, to_email:str):
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
