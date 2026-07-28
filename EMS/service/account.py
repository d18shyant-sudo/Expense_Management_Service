from repository.account import AccountRepository
import bcrypt
import jwt
import logging
logging.basicConfig(level=logging.INFO)

from datetime import datetime, timedelta

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
        username: str,db
    ):

        expires_at = (
            datetime.utcnow()
            + timedelta(minutes=15)
        )
        user = (
                    AccountRepository.get_employee_by_username(username,db)
                )

        payload = {
        "employee_id": str(user.id),
        "username": username,
        "role": user.role.role_name,
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

        account = (
            AccountRepository
            .get_by_username(
                username,
                db
            )
        )
        account_id = (
            AccountRepository.get_employee_by_username(username,db)
        )
        logging.info("credentials in db:",account.password)
        if not account:
            return None
        
        if not AccountService.verify(
            password,
            account.password
        ):
            return None
        
        token, expires_at = (
            AccountService
            .create_access_token(
                username,db
            )
        )

        return {
            "token": token,
            "expires_at":
                expires_at.isoformat(),
            "authentication_type":
                "Bearer",
            "employee_id":
                str(account_id.id)
        }