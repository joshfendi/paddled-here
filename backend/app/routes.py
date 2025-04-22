from fastapi import APIRouter
from app.models import PaddleLocation
from typing import List

router = APIRouter()

paddle_db: List[PaddleLocation] = []
next_id = 1

@router.post("/paddles", response_model=PaddleLocation)
def create_paddle_location(paddle: PaddleLocation):
    global next_id
    paddle.id = next_id
    next_id += 1
    paddle_db.append(paddle)
    return paddle

@router.get("/paddles", response_model=List[PaddleLocation])
def get_all_paddles():
    return paddle_db
