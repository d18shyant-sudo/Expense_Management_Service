from models import *
from engine import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
class employee:
    def get_all_employees(db:Session):
        result = db.query(employees.Employee).all()
        return result
    def get_employees_name(name,db:Session):
        result = db.query(employees.Employee).filter(employees.Employee.name == name).first()
        return result
    def get_employees_role(role_of_employee,db:Session):
        results = (db.query(employees.Employee).join(employees.Employee.role).filter(role.Role.role_name == role_of_employee).all())
        return results
    def get_employees_department(department_name,db:Session):
        result = (db.query(employees.Employee).join(employees.Employee.department).filter(departments.Department.name == department_name).all())
        return result