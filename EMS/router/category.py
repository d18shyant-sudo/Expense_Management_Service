from schema.category import Category_name
from engine import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from service.category import category_service
from auth import require_role
router = APIRouter(prefix="/api/v1",tags=["Categories"])
@router.get("/get-all-category-name",response_model=list[Category_name])
def get_category(db:Session = Depends(get_db),user = Depends(require_role("Finance_Head","Finance_admin","Manager","Employee"))):
    try:
        results = category_service.get_category(db)
        if results:
            return JSONResponse(status_code=200,content=[result for result in results])
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No Categories found"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
@router.post("/categories")
def create_category(
    category_detail: Category_name,
    db: Session = Depends(get_db),user = Depends(require_role("admin"))
):
    try:

        result = (
            category_service
            .create_category(
                category_detail,
                db
            )
        )

        if result == "CATEGORY_ALREADY_EXISTS":

            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Category already exists"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "message":
                "Category created successfully",
                "id":
                str(result.id),
                "name":
                result.name
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
@router.put("/categories/{category_id}")
def update_category(
    category_id: str,
    update_category: Category_name,
    db: Session = Depends(get_db),user = Depends(require_role("admin"))
):
    try:

        result = (
            category_service
            .update_category(
                category_id,
                update_category,
                db
            )
        )

        if result == "CATEGORY_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Category not found"
                }
            )

        if result == "CATEGORY_ALREADY_EXISTS":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Category already exists"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "message":
                "Category updated successfully",
                "id":
                str(result.id),
                "name":
                result.name
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )