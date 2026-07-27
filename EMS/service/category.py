from repository.category import categories
from sqlalchemy.orm import Session
class category_service:
    def get_category(db:Session):
        try:
            results = categories.get_category(db)
            if results:
                return [
                {
                "category_name":result.name
                } for result in results
                ]
            if not results:
                return []
        except Exception as e:
            raise e