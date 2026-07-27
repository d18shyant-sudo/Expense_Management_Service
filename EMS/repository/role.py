from models import *
from engine import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
class roles:
    def get_roles(db:Session):
        results = db.query(role.Role).all()
        return results