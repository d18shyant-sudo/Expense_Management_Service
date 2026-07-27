from models import *
from engine import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
class categories:
    def get_category(db:Session):
        results = db.query(category.Category).all()
        return results
    @staticmethod
    def create_category(
        category_of_name,
        db: Session
    ):
        existing_category = (
            db.query(category.Category).filter(
                category.Category.name == category_of_name.category_name
            )
            .first()
        )

        if existing_category:
            return "CATEGORY_ALREADY_EXISTS"

        categories_name = Category(
            name=category_of_name.category_name
        )

        db.add(categories_name)
        db.commit()
        db.refresh(categories_name)

        return categories_name
    @staticmethod
    def update_category(
        category_id,
        updated_category,
        db: Session
    ):

        category_update = (
            db.query(category.Category)
            .filter(
                category.Category.id == category_id
            )
            .first()
        )

        if not category_update:
            return "CATEGORY_NOT_FOUND"

        existing_category = (
            db.query(category.Category)
            .filter(
                category.Category.name == updated_category.category_name
            )
            .first()
        )

        if (
            existing_category
            and
            existing_category.id != category_update.id
        ):
            return "CATEGORY_ALREADY_EXISTS"

        category_update.name = updated_category.category_name

        db.commit()
        db.refresh(category_update)

        return category_update