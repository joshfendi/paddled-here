from fastapi import APIRouter, HTTPException
from app.models import PaddleLocation
from typing import List
from datetime import datetime, timezone

router = APIRouter()

paddle_db: List[PaddleLocation] = []
next_id = 1

@router.post("/paddles", response_model=PaddleLocation)
def create_paddle_location(paddle: PaddleLocation):
    global next_id
    paddle.id = next_id
    paddle.created_at = datetime.now(timezone.utc)
    next_id += 1
    paddle_db.append(paddle)
    return paddle

@router.get("/paddles", response_model=List[PaddleLocation])
def get_all_paddles():
    return paddle_db

@router.put("/paddles/{paddle_id}", response_model=PaddleLocation)
def update_paddle(paddle_id: int, updated_paddle: PaddleLocation):
    for index, paddle in enumerate(paddle_db):
        if paddle.id == paddle_id:
            updated_paddle.id = paddle_id
            updated_paddle.created_at = paddle.created_at  # preserve original timestamp
            paddle_db[index] = updated_paddle
            return updated_paddle
    raise HTTPException(status_code=404, detail="Paddle log not found")

@router.delete("/paddles/{paddle_id}", response_model=PaddleLocation)
def delete_paddle(paddle_id: int):
    for index, paddle in enumerate(paddle_db):
        if paddle.id == paddle_id:
            return paddle_db.pop(index)
    raise HTTPException(status_code=404, detail="Paddle log not found")
