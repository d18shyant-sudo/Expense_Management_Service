from models import *
from engine import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
class department:
    def get_departments(db:Session):
        results = db.query(departments.Department).all()
        return results