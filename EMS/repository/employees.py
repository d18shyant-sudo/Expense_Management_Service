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
    @staticmethod
    def create_employee(
        employee_detail,
        db: Session
    ):

        roles = (
            db.query(role.Role)
            .filter(
                role.Role.role_name == employee_detail.role_name
            )
            .first()
        )

        if not roles:
            return "ROLE_NOT_FOUND"

        department = (
            db.query(departments.Department)
            .filter(
                departments.Department.name ==
                employee_detail.department_name
            )
            .first()
        )

        if not department:
            return "DEPARTMENT_NOT_FOUND"

        employee = Employee(
            name=employee_detail.name,
            email=employee_detail.email,
            role_id=roles.id,
            department_id=department.id,
            is_active=True
        )

        db.add(employee)
        db.commit()
        db.refresh(employee)

        return employee
    @staticmethod
    def update_employee(
        employee_id,
        updated_detail,
        db
    ):

        employee_detail = (
            db.query(employees.Employee)
            .filter(
                employees.Employee.id == employee_id
            )
            .first()
        )

        if not employee_detail:
            return "EMPLOYEE_NOT_FOUND"

        if updated_detail.role_name:

            roles = (
                db.query(role.Role)
                .filter(
                    role.Role.role_name ==
                    updated_detail.role_name
                )
                .first()
            )

            if not roles:
                return "ROLE_NOT_FOUND"

            employee_detail.role_id = roles.id

        if updated_detail.department_name:

            department = (
                db.query(departments.Department)
                .filter(
                    departments.Department.name ==
                    updated_detail.department_name
                )
                .first()
            )

            if not department:
                return "DEPARTMENT_NOT_FOUND"

            employee_detail.department_id = department.id

        if updated_detail.name is not None:
            employee_detail.name = updated_detail.name

        if updated_detail.email is not None:
            employee_detail.email = updated_detail.email

        if updated_detail.is_active is not None:
            employee_detail.is_active = updated_detail.is_active

        db.commit()
        db.refresh(employee_detail)

        return employee_detail