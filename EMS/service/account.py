from repository.account import AccountRepository
import bcrypt
import jwt

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
            + timedelta(hours=1)
        )
        user = (
                    AccountRepository.get_employee_by_username(username,db)
                )

        payload = {
            "username": username,
            "exp": expires_at,
            "role":user.role.role_name
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