from repository.account import AccountRepository
from utils.otp_store import save_otp, verify_otp
from utils.emails import send_otp 

import bcrypt
from jose import jwt

from datetime import datetime, timedelta

import logging

logging.basicConfig(level=logging.INFO)


class AccountService:

    @staticmethod
    def encrypt(password: str) -> str:
        password_bytes = password.encode("utf-8")
        hashed = bcrypt.hashpw(
            password_bytes,
            bcrypt.gensalt()
        )
        return hashed.decode("utf-8")

    @staticmethod
    def verify(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )

    @staticmethod
    def create_access_token(username: str, db):

        account = AccountRepository.get_by_username(
            username,
            db
        )

        if account is None:
            raise Exception("Account not found")

        employee = AccountRepository.get_employee_by_email(
            account.email,
            db
        )

        if employee is None:
            raise Exception("Employee not found")

        expires_at = datetime.utcnow() + timedelta(hours=1)

        payload = {
            "sub": username,
            "role": employee.role.role_name,
            "exp": expires_at
        }

        token = jwt.encode(
            payload,
            "secret_key",
            algorithm="HS256"
        )

        return token, expires_at

    @staticmethod
    def login(
        username: str,
        password: str,
        db
    ):

        account = AccountRepository.get_by_username(
            username,
            db
        )

        if account is None:
            return None

        if not AccountService.verify(
            password,
            account.password
        ):
            return None

        employee = AccountRepository.get_employee_by_email(
            account.email,
            db
        )

        if employee is None:
            return None

        token, expires_at = AccountService.create_access_token(
            username,
            db
        )

        return {
            "token": token,
            "expires_at": expires_at.isoformat(),
            "authentication_type": "Bearer",
            "employee_id": str(employee.id)
        }

    @staticmethod
    def forgot_password(payload, db):

        account = AccountRepository.get_by_email(
            payload.email,
            db
        )

        if not account:
            return {
                "message": "Email not found"
            }

        otp = save_otp(payload.email)

        print("OTP:", otp)

        send_otp(
            payload.email,
            otp
        )

        return {
            "message": "OTP sent successfully"
        }

    @staticmethod
    def verify_otp(payload):

        if verify_otp(
            payload.email,
            payload.otp
        ):
            return {
                "message": "OTP verified"
            }

        return {
            "message": "Invalid OTP"
        }

    @staticmethod
    def reset_password(payload, db):

        account = AccountRepository.get_by_email(
            payload.email,
            db
        )

        if not account:
            return {
                "message": "Email not found"
            }

        hashed_password = AccountService.encrypt(
            payload.new_password
        )

        AccountRepository.update_password(
            payload.email,
            hashed_password,
            db
        )

        return {
            "message": "Password reset successfully"
        }