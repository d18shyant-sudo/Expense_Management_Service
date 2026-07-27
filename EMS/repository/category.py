from models import *
from engine import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
class categories:
    def get_category(db:Session):
        results = db.query(category.Category).all()
        return results