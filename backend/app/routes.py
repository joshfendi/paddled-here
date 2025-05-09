from fastapi import APIRouter, HTTPException
from app.models import PaddleLocation, PaddleUpdate, PaddlesPage
from app.services import paddle_service
from typing import List
from datetime import date

router = APIRouter()

@router.get("/paddles", response_model=PaddlesPage)
def get_all(
    user_name: str = None,
    team: str = None,
    sort_by: str = None,
    desc: bool = False,
    start_date: date = None,
    end_date: date = None,
    limit: int = 10,
    offset: int = 0
):
    # Fetch filtered and paginated results along with the total count
    results, total = paddle_service.get_all_paddles(
        user_name=user_name,
        team=team,
        sort_by=sort_by,
        desc=desc,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        offset=offset
    )

    # Return structured response with pagination metadata
    return PaddlesPage(total=total, results=results)

@router.get("/paddles/{paddle_id}", response_model=PaddleLocation)
def get_paddle(paddle_id: int):
    try:
        return paddle_service.get_paddle(paddle_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Paddle log not found")

@router.post("/paddles", response_model=PaddleLocation)
def create(paddle: PaddleLocation):
    return paddle_service.create_paddle(paddle)

@router.put("/paddles/{paddle_id}", response_model=PaddleLocation)
def update(paddle_id: int, updated: PaddleLocation):
    try:
        return paddle_service.update_paddle(paddle_id, updated)
    except ValueError:
        raise HTTPException(status_code=404, detail="Paddle log not found")

@router.patch("/paddles/{paddle_id}", response_model=PaddleLocation)
def patch_paddle(paddle_id: int, patch: PaddleUpdate):
    try:
        return paddle_service.patch_paddle(paddle_id, patch)
    except ValueError:
        raise HTTPException(status_code=404, detail="Paddle log not found")

@router.delete("/paddles/{paddle_id}", status_code=204)
def delete(paddle_id: int):
    try:
        paddle_service.delete_paddle(paddle_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Paddle log not found")
