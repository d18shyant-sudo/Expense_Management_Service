from datetime import datetime, timedelta

import bcrypt
import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from repository.account import AccountRepository
from schema.account import (
    ForgotPasswordRequest,
    VerifyOtpRequest,
    ResetPasswordRequest,
)
from utils.emails import send_otp
from utils.otp_store import save_otp, verify_otp


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


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
    def verify(
        password: str,
        hashed_password: str
    ) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )

    @staticmethod
    def create_access_token(
        username: str,
        db: Session
    ):

        account = AccountRepository.get_by_username(
            username,
            db
        )

        if account is None:
            return None, None

        employee = AccountRepository.get_employee_by_email(
            account.email,
            db
        )

        if employee is None:
            return None, None

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
    def login(username: str, password: str, db: Session):
      account = AccountRepository.get_by_username(username, db)
      if account is None:
        raise ValueError("invalid_credentials")

      if not AccountService.verify(password, account.password):
        raise ValueError("invalid_credentials")

      employee = AccountRepository.get_employee_by_email(account.email, db)
      if employee is None:
          raise ValueError("account_not_linked")

      token, expires_at = AccountService.create_access_token(username, db)

      return {
    "token": token,
    "expires_at": expires_at.isoformat(),
    "authentication_type": "Bearer",
    "employee_id": str(employee.id)
}
        

    @staticmethod
    def forgot_password(
        payload: ForgotPasswordRequest,
        db: Session
    ):

        account = AccountRepository.get_by_email(
            payload.email,
            db
        )

        if account is None:
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
    def verify_otp(
        payload: VerifyOtpRequest
    ):

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
    def reset_password(
        payload: ResetPasswordRequest,
        db: Session
    ):

        account = AccountRepository.get_by_email(
            payload.email,
            db
        )

        if account is None:
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