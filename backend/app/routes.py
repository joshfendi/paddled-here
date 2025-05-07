from fastapi import APIRouter, HTTPException
from app.models import PaddleLocation
from app.models import PaddleUpdate
from typing import List
from app.services import paddle_service

router = APIRouter()

@router.get("/paddles", response_model=List[PaddleLocation])
def get_all(user_name: str = None, team: str = None):
    return paddle_service.get_all_paddles(user_name=user_name, team=team)

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
