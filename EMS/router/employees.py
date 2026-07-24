from schema.employees import Employee_name,Employee_role,Get_Employees,Employee_department,Get_Employees_department,EmployeeCreate,EmployeeUpdate
from engine import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from service.employee import employee_service
from auth import require_role
router = APIRouter(prefix="/api/v1",tags=["Employees"])
@router.get("/get-employees",response_model=list[Get_Employees])
def get_all_employees(db:Session = Depends(get_db)):
    try:
        results = employee_service.get_all_employees(db)
        if results:
            return JSONResponse(status_code=200,content=[result for result in results])
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No Employees"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
@router.get("/get-employee",response_model=Get_Employees)
def get_employee_name(name:str,db:Session = Depends(get_db)):
    try:
        results = employee_service.get_employees_name(name,db)
        if results:
            return JSONResponse(status_code=200,content=results)
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No Employee"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
@router.get("/get-employee-role",response_model=Get_Employees)
def get_employee_role(role:str,db:Session = Depends(get_db)):
    try:
        results = employee_service.get_employees_role(role,db)
        if results:
            return JSONResponse(status_code=200,content=results)
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No role is there"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
@router.get("/get-employee-department",response_model=list[Employee_department])
def get_employee_department(department_name:str,db:Session = Depends(get_db)):
    try:
        results = employee_service.get_employees_department(department_name,db)
        if results:
            return JSONResponse(status_code=200,content=results)
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No department is there"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
@router.post("/employees")
def create_employee(
    employee_detail: EmployeeCreate,
    db: Session = Depends(get_db)
):

    try:

        result = (
            employee_service
            .create_employee(
                employee_detail,
                db
            )
        )

        if result == "ROLE_NOT_FOUND":

            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Role not found"
                }
            )

        if result == "DEPARTMENT_NOT_FOUND":

            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Department not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "message":
                "Employee created successfully",
                "id":
                str(result.id),
                "name":
                result.name,
                "email":
                result.email
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error":
                str(e)
            }
        )
@router.put("/employees/{employee_id}")
def update_employee(
    employee_id: str,
    updated_detail: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    try:

        result = (
            employee_service
            .update_employee(
                employee_id,
                updated_detail,
                db
            )
        )

        if result == "EMPLOYEE_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Employee not found"
                }
            )

        if result == "ROLE_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Role not found"
                }
            )

        if result == "DEPARTMENT_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Department not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "message":
                "Employee updated successfully",
                "id":
                str(result.id),
                "name":
                result.name,
                "email":
                result.email
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )