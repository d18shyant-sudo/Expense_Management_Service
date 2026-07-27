from sqlalchemy.orm import Session
from models.account import Account
from service.account import AccountService

class Regsiter_Account:
    def add_account(detail,db):
        is_exist = db.query(Account).filter(Account.email==detail.email).first()
        if is_exist:
             return []
        new_user = Account(username=detail.username,password=AccountService.encrypt(detail.password),email=detail.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user