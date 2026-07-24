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
    def post_role(db:Session,new_role):
            try:
                results = roles.post_role(db,new_role)
                if results: 
                    return results
                if not results:
                    return []
            except Exception as e:
                raise e
    def update_role(db:Session,update_role):
        try:
            results = roles.update_role(db,update_role)
            if results:
                return results
            if not results:
                return []
        except Exception as e:
            raise e
            