# paddle_service.py

from typing import List
from app.models import PaddleLocation

paddle_db: List[PaddleLocation] = []
next_id = 1

def get_all_paddles() -> List[PaddleLocation]:
    return paddle_db

def create_paddle(paddle: PaddleLocation) -> PaddleLocation:
    global next_id
    paddle.id = next_id
    next_id += 1
    paddle_db.append(paddle)
    return paddle

def update_paddle(paddle_id: int, updated_paddle: PaddleLocation) -> PaddleLocation:
    for index, paddle in enumerate(paddle_db):
        if paddle.id == paddle_id:
            updated_paddle.id = paddle_id
            updated_paddle.created_at = paddle.created_at
            paddle_db[index] = updated_paddle
            return updated_paddle
    raise ValueError("Paddle log not found")

def delete_paddle(paddle_id: int) -> None:
    for index, paddle in enumerate(paddle_db):
        if paddle.id == paddle_id:
            del paddle_db[index]
            return
    raise ValueError("Paddle log not found")
