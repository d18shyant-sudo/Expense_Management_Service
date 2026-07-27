from repository.employees import employee
from sqlalchemy.orm import Session
class employee_service:
    def get_all_employees(db:Session):
        try:
            results = employee.get_all_employees(db)
            if results:
                return [
                    {
                    "name":result.name,
                    "id":str(result.id),
                    "role":result.role.role_name,
                    "department":result.department.name if result.department else None
                    } for result in results
                ]
                
            if not results:
                return []
        except Exception as e:
            raise e
    def get_employees_name(name,db:Session):
        try:
            result = employee.get_employees_name(name,db)
            if result:
                return {
                    "name":result.name,
                    "id":str(result.id),
                    "role":result.role.role_name,
                    "department":result.department.name if result.department else None
                }
            if not result:
                return []
        except Exception as e:
            raise e
    def get_employees_role(role,db:Session):
        try:
            results = employee.get_employees_role(role,db)
            if results:
                return[
                    {
                    "name":result.name,
                    "id":str(result.id),
                    "role":result.role.role_name,
                    "department":result.department.name if result.department else None
                    } for result in results
                ]
            if not results:
                return []
        except Exception as e:
            raise e
    def get_employees_department(department_name,db:Session):
        try:
            results = employee.get_employees_department(department_name,db)
            if results:
                return [{
                    "name": result.name,
                    "id":  str(result.id),
                    "role":result.role.role_name
                }for result in results]
            if not results:
                return []
        except Exception as e:
            raise e