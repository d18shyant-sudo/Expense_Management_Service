from schema.departments import Department_name,DepartmentCreate,DepartmentUpdate
from engine import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from service.departments import department_service
from auth import require_role
router = APIRouter(prefix="/api/v1",tags=["Departments"])
@router.get("/get-all-department-name",response_model=list[Department_name])
def get_departments(db:Session = Depends(get_db),user = Depends(require_role("Finance_Head","Finance_admin","Employee","Manager","admin"))):
    try:
        results = department_service.get_departments(db)
        if results:
            return JSONResponse(status_code=200,content=[result for result in results])
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No Departments found"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
@router.post("/departments")
def create_department(
    create_department_detail: DepartmentCreate,
    db: Session = Depends(get_db),user = Depends(require_role("admin"))
):
    try:

        result = (
            department_service
            .create_department(
                create_department_detail,
                db
            )
        )

        if result == "DEPARTMENT_ALREADY_EXISTS":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Department already exists"
                }
            )

        if result == "MANAGER_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Manager not found"
                }
            )

        if result == "FINANCE_ADMIN_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Finance admin not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "message":
                "Department created successfully",
                "id":
                str(result.id),
                "name":
                result.name,
                "manager_id":
                str(result.manager_id),
                "finance_admin_id":
                str(result.finance_admin_id)
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
@router.put("/departments/{department_id}")
def update_department(
    department_id: str,
    update_department_detail: DepartmentUpdate,
    db: Session = Depends(get_db),user = Depends(require_role("admin"))
):
    try:

        result = (
            department_service
            .update_department(
                department_id,
                update_department_detail,
                db
            )
        )

        if result == "DEPARTMENT_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Department not found"
                }
            )

        if result == "MANAGER_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Manager not found"
                }
            )

        if result == "FINANCE_ADMIN_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Finance admin not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "message":
                "Department updated successfully",
                "id":
                str(result.id),
                "name":
                result.name,
                "manager_id":
                str(result.manager_id)
                if result.manager_id
                else None,
                "finance_admin_id":
                str(result.finance_admin_id)
                if result.finance_admin_id
                else None
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )