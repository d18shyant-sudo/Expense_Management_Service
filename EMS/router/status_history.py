from fastapi import (
    APIRouter,
    Depends
)
from schema.status_history import StatusHistoryCreate,StatusUpdate
from fastapi.responses import (
    JSONResponse
)

from sqlalchemy.orm import Session

from engine import get_db

from service.status_history import (
    StatusHistoryService)

from auth import require_role
router = APIRouter(
    prefix="/api/v1",
    tags=["Status_History"]
)
@router.post("/status-history")
def create_status_history(
    payload: StatusHistoryCreate,
    db: Session = Depends(get_db),user = Depends(require_role("Employee","Manager"))
):
    try:

        result = (
            StatusHistoryService
            .create_status_history(
                payload,
                db
            )
        )

        if result == "CLAIM_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Claim not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
@router.put(
    "/status-history/claim"
)
def update_status_claim(
    history_id: str,
    payload: StatusHistoryCreate,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_admin","Manager"))
):
    try:

        result = (
            StatusHistoryService
            .update_status_claim(
                history_id,
                payload,
                db
            )
        )

        if result == "HISTORY_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "History not found"
                }
            )

        if result == "CLAIM_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Claim not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
@router.put(
    "/status-history/status"
)
def update_status(
    history_id: str,
    payload: StatusUpdate,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_admin","Manager","Finance_Head"))
):
    try:

        result = (
            StatusHistoryService
            .update_status(
                history_id,
                payload,
                db
            )
        )

        if result == "HISTORY_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "History not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
@router.get("/status-history")
def get_status_history(
    claim_id: str,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_admin","Manager","Finance_Head","Employee"))
):
    try:

        result = (
            StatusHistoryService.get_status_history(
                claim_id,
                db
            )
        )

        if result is None:

            return JSONResponse(
                status_code=404,
                content={
                    "error": "Expense claim not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=[
                {
                    "id": str(history.id),
                    "approver_id": str(history.approver_id),
                    "approver_name": history.approver.name,
                    "requested_amount": float(history.requested_amount),
                    "approved_amount": float(history.approved_amount),
                    "remaining_amount": float(history.remaining_amount),
                    "status": history.status,
                    "remarks": history.remarks,
                    "action_time": str(history.action_time)
                }
                for history in result
            ]
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )