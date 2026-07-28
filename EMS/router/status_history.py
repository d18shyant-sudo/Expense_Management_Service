from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from engine import get_db
from service.status_history import StatusHistoryService
from auth import require_role

router = APIRouter(
    prefix="/api/v1",
    tags=["Status History"]
)


@router.get("/status-history")
def get_status_history(
    claim_id: str,
    db: Session = Depends(get_db),
    user=Depends(
        require_role(
            "Employee",
            "Manager",
            "Finance_admin",
            "Finance_Head"
        )
    ),
):
    try:

        result = StatusHistoryService.get_status_history(
            claim_id,
            db
        )

        if not result:
            return JSONResponse(
                status_code=404,
                content={
                    "error": "Status history not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=[
                {
                    "id": str(history.id),
                    "claim_id": str(history.claim_id),
                    "approver_id": str(history.approver_id),
                    "approver_name": history.approver.name if history.approver else None,
                    "requested_amount": float(history.requested_amount),
                    "approved_amount": float(history.approved_amount),
                    "remaining_amount": float(history.remaining_amount),
                    "status": history.status,
                    "remarks": history.remarks,
                    "action_time": str(history.action_time),
                }
                for history in result
            ],
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            },
        )