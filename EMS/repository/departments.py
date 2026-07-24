from models import *
from engine import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime
class department:
    def get_departments(db:Session):
        results = db.query(departments.Department).all()
        return results
    @staticmethod
    def create_department(
        create_department_detail,
        db: Session
    ):
        # verification check for the department,manager,finance_admin
        existing_department = (
            db.query(departments.Department)
            .filter(
                departments.Department.name == create_department_detail.name
            )
            .first()
        )

        if existing_department:
            return "DEPARTMENT_ALREADY_EXISTS"

        manager = (
            db.query(employees.Employee)
            .filter(
                employees.Employee.name ==
                create_department_detail.manager_name
            )
            .first()
        )

        if manager:
            return "MANAGER_ALREADY_EXISTS"

        finance_admin = (
            db.query(employees.Employee)
            .filter(
                employees.Employee.name ==
                create_department_detail.finance_admin_name
            )
            .first()
        )

        if finance_admin:
            return "FINANCE_ADMIN_ALREADY_EXISTS"
        
        #retriving the role ID
        manager_role = (db.query(role.Role).filter(role.Role.role_name=="Manager")).first()

        finance_admin_role = (db.query(role.Role).filter(role.Role.role_name=="Finance_admin")).first()

        
        manager_of_department = employees.Employee(name=create_department_detail.manager_name,role_id=manager_role.id,email=create_department_detail.manager_email)
        finance_admin_of_department = employees.Employee(name=create_department_detail.finance_admin_name,role_id=finance_admin_role.id,email=create_department_detail.finance_admin_email)
        db.add_all([manager_of_department,finance_admin_of_department])
        db.flush()
        department = departments.Department(
            name=create_department_detail.name,
            manager_id=manager_of_department.id,
            finance_admin_id=finance_admin_of_department.id
        )
        db.add(department)
        db.flush()
        manager_of_department.department_id = department.id
        finance_admin_of_department.department_id = department.id
        db.commit()
        db.refresh(department)

        return department
    @staticmethod
    def update_department(
        department_id,
        update_department_detail,
        db
    ):

        department = (
            db.query(departments.Department)
            .filter(
                Department.id == department_id
            )
            .first()
        )

        if not department:
            return "DEPARTMENT_NOT_FOUND"

        if update_department_detail.name is not None:
            department.name = update_department_detail.name

        if update_department_detail.manager_name is not None:
            department.manager.name= update_department_detail.manager_name

        if update_department_detail.finance_admin_name is not None:
            department.finance_admin.name = update_department_detail.finance_admin_name
            
        department.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(department)

        return department