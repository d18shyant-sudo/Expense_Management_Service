from repository.account import AccountRepository
import bcrypt
import jwt
from passlib.context import CryptContext
from utils.otp_store import verify_otp, save_otp
from utils.emails import send_otp
from schema.account import VerifyOtpRequest
from datetime import datetime, timedelta,UTC


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    return pwd_context.hash(password)




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
    def create_access_token(username: str, db):

     expires_at = datetime.utcnow() + timedelta(hours=1)

     account = AccountRepository.get_by_username(username, db)

     if not account:
        return None, None

     user = AccountRepository.get_employee_by_email(
        account.email,
        db
    )

     if not user:
        return None, None

     payload = {
        "username": username,
        "exp": int(expires_at.timestamp()),
        "role": user.role.role_name
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

     if not account:
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

     if not employee:
        return None

     token, expires_at = (
        AccountService.create_access_token(
            username,
            db
        )
    )

     return {
    "token": token,
    "expires_at": expires_at.isoformat(),
    "authentication_type": "Bearer",
    "employee_id": str(employee.id)
}
    
    @staticmethod
    def forgot_password(payload: ForgotPasswordRequest, db: Session):
      account = AccountRepository.get_by_email(payload.email, db)

      if not account:
        return {"message": "Email not found"}

      otp = save_otp(payload.email)
      print("OTP returned from save_otp():", otp)
      send_otp(payload.email, otp)

      return {"message": "OTP sent successfully"}


    @staticmethod
    def verify_otp(payload: VerifyOtpRequest):
      if verify_otp(payload.email, payload.otp):
        return {"message": "OTP verified"}

      return {"message": "Invalid OTP"}

    
    

    @staticmethod
    def reset_password(payload, db):

     print("RESET EMAIL:", payload.email)

     account = AccountRepository.get_by_email(
        payload.email,
        db
    )

     print("ACCOUNT FOUND:", account)

     if not account:
        return {
            "message": "Email not found"
        }

     hashed_password = hash_password(
        payload.new_password
    )

     account.password = hashed_password

     db.commit()
     db.refresh(account)

     return {
        "message": "Password reset successfully"
    }