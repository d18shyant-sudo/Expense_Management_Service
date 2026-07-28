import random
from datetime import datetime, timedelta

otp_store = {}

def save_otp(email):
    otp = str(random.randint(100000, 999999))

    otp_store[email] = {
        "otp": otp,
        "expires": datetime.utcnow() + timedelta(minutes=5)
    }

    return otp


def verify_otp(email, otp):
    if email not in otp_store:
        return False

    data = otp_store[email]

    if datetime.utcnow() > data["expires"]:
        del otp_store[email]
        return False

    if data["otp"] != otp:
        return False

    del otp_store[email]
    return True