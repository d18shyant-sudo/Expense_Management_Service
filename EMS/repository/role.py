from models import *
from engine import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
class roles:
    def get_roles(db:Session):
        results = db.query(role.Role).all()
        return results
    def post_role(db:Session,new_role):
        new_role = role.Role(role_name=new_role.role_name)
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        return new_role
    def update_role(db:Session,updated_role):
        existing_role = db.query(role.Role).filter(role.Role.id == updated_role.role_id).first()
        existing_role._role_name = updated_role
        db.commit()
        db.refresh(existing_role)
        return existing_role