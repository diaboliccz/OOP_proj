
import os
import smtplib
from email.message import EmailMessage
from random import randint
from dotenv import load_dotenv

load_dotenv()

def send_verification_email(user):
    token = generate_verification_token()
    user.set_email_verification_token(token)
    
    email_subject = 'Your Email Verification Code'
    email_body = f'Dear {user.full_name},\n\n Please use the following verification code to verify your account:\n\n{token}\n\nBest regards,\nAgoda Team'
    
    send_email(user._email, email_subject, email_body)

def generate_verification_token():
    return randint(100000, 999999)

def send_email(to, subject, body):
    email = EmailMessage()
    email.set_content(body)
    email['Subject'] = subject
    email['From'] = os.environ['EMAIL_ADDRESS']
    email['To'] = to
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
            smtp.send_message(email)
            print(f'Email sent to {to}')
    except Exception as e:
        print(f'Error sending email: {e}')
