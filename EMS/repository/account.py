from sqlalchemy.orm import Session

from models.account import Account
from models.employees import Employee


class AccountRepository:

    @staticmethod
    def get_by_username(username, db):
        return (
            db.query(Account)
            .filter(Account.username == username)
            .first()
        )

    @staticmethod
    def get_by_email(email, db):
        return (
            db.query(Account)
            .filter(Account.email == email)
            .first()
        )

    @staticmethod
    def get_employee_by_email(email, db):
        return (
            db.query(Employee)
            .filter(Employee.email == email)
            .first()
        )

    @staticmethod
    def update_password(email, hashed_password, db):
      account = (
        db.query(Account)
        .filter(Account.email == email)
        .first()
    )

      if account:
        account.password = hashed_password
        db.commit()
        db.refresh(account)

        return account

    @staticmethod
    def save(db):
        db.commit()