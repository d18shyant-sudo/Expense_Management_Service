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
    @staticmethod
    def create_category(
        category_of_name,
        db: Session
    ):

        return (
            categories
            .create_category(
                category_of_name,
                db
            )
        )
    @staticmethod
    def update_category(
        category_id,
        updated_category,
        db
    ):

        return (
            categories
            .update_category(
                category_id,
                updated_category,
                db
            )
        )