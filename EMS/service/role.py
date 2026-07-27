from repository.role import roles
from sqlalchemy.orm import Session
class role_service:
    def get_roles(db:Session):
        try:
            results = roles.get_roles(db)
            if results:
                return [
                    {
                    "role_name":result.role_name
                    }for result in results
                ]
            if not results:
                return []
        except Exception as e:
            raise e