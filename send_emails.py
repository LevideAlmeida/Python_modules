# Sending E-mails with python
import os
import pathlib
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load .env
load_dotenv()

# HTML file path
FILE_PATH = pathlib.Path(__file__).parent / 'email.html'

# Sender and Recipient data
sender = os.getenv('FROM_EMAIL', '')
recipient = sender
subject = "Send email with python"


def send_email(sender: str, recipient: str, recipient_name: str,
               html_file: pathlib.Path, subject: str):

    # SMTP Settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('FROM_EMAIL', '')
    smtp_password = os.getenv('EMAIL_PASSWORD', '')

    # Text mensage
    with open(html_file, 'r') as file:
        file_text = file.read()
        template = Template(file_text)
        email_text = template.substitute(name=recipient_name)

    # MIMEMultipart
    mime_multipart = MIMEMultipart()
    mime_multipart['from'] = sender
    mime_multipart['to'] = recipient
    mime_multipart['subject'] = subject

    email_body = MIMEText(email_text, 'html', 'utf-8')
    mime_multipart.attach(email_body)

    # sent email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(mime_multipart)
        print('Email sucessfully sent!!🎉🎉')


if __name__ == '__main__':
    send_email(sender, recipient, "Levi", FILE_PATH, subject)
