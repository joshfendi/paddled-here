from fastapi import APIRouter, HTTPException
from app.models import PaddleLocation
from typing import List
from app.services import paddle_service

router = APIRouter()

@router.get("/paddles", response_model=List[PaddleLocation])
def get_all():
    return paddle_service.get_all_paddles()

@router.post("/paddles", response_model=PaddleLocation)
def create(paddle: PaddleLocation):
    return paddle_service.create_paddle(paddle)

@router.put("/paddles/{paddle_id}", response_model=PaddleLocation)
def update(paddle_id: int, updated: PaddleLocation):
    try:
        return paddle_service.update_paddle(paddle_id, updated)
    except ValueError:
        raise HTTPException(status_code=404, detail="Paddle log not found")

@router.delete("/paddles/{paddle_id}", status_code=204)
def delete(paddle_id: int):
    try:
        paddle_service.delete_paddle(paddle_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Paddle log not found")
