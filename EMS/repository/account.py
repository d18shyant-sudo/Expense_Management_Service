from sqlalchemy.orm import Session

from models.account import Account
from models.employees import Employee

class AccountRepository:

    @staticmethod
    def get_by_username(
        username: str,
        db: Session
    ):
        return (
            db.query(Account)
            .filter(
                Account.username == username
            )
            .first()
        )

    @staticmethod
    def get_employee_by_username(
        username: str,
        db: Session
    ):
        return (
            db.query(Employee)
            .filter(
                Employee.name == username
            )
            .first()
        )