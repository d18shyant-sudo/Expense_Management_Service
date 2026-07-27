from repository.departments import department
from sqlalchemy.orm import Session
class department_service:
    def get_departments(db:Session):
        try:
            results = department.get_departments(db)
            if results:
                return [
                    {
                    "department_name":result.name
                    }for result in results
                ]
            if not results:
                return []
        except Exception as e:
            raise e