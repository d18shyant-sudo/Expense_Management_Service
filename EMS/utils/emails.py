import os
import smtplib
import random

from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

otp_store = {}

def save_otp(email):
    otp = str(random.randint(100000, 999999))
    otp_store[email] = otp

    print(f"Generated OTP for {email}: {otp}")

    return otp


def send_otp(receiver_email, otp):
    msg = MIMEText(f"Your OTP is {otp}")

    msg["Subject"] = "Password Reset OTP"
    msg["From"] = EMAIL
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(EMAIL, PASSWORD)

    server.sendmail(
        EMAIL,
        receiver_email,
        msg.as_string()
    )

    server.quit()