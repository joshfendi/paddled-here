from typing import List
from sqlmodel import Session, select
from app.db import engine
from app.models import PaddleLocation, PaddleUpdate

from datetime import date

from typing import Tuple

def get_all_paddles(
    user_name: str = None,
    team: str = None,
    sort_by: str = None,
    desc: bool = False,
    start_date: date = None,
    end_date: date = None,
    limit: int = 10,
    offset: int = 0
) -> Tuple[List[PaddleLocation], int]:
    with Session(engine) as session:
        # Build the base SELECT statement
        base_stmt = select(PaddleLocation)

        # Apply filters based on query parameters
        if user_name:
            base_stmt = base_stmt.where(PaddleLocation.user_name == user_name)
        if team:
            base_stmt = base_stmt.where(PaddleLocation.team == team)
        if start_date:
            base_stmt = base_stmt.where(PaddleLocation.date >= start_date)
        if end_date:
            base_stmt = base_stmt.where(PaddleLocation.date <= end_date)

        # Get total number of matching records before pagination
        total = session.exec(base_stmt).all()
        total_count = len(total)

        # Apply sorting if the sort_by field is valid
        if sort_by in {"created_at", "date"}:
            sort_column = getattr(PaddleLocation, sort_by)
            if desc:
                sort_column = sort_column.desc()
            base_stmt = base_stmt.order_by(sort_column)

        # Apply pagination by setting offset and limit
        base_stmt = base_stmt.offset(offset).limit(limit)

        # paginate in Python
        paddles = total[offset : offset + limit]  
        return paddles, total_count
    
def get_paddle(paddle_id: int) -> PaddleLocation:
    with Session(engine) as session:
        paddle = session.get(PaddleLocation, paddle_id)
        if not paddle:
            raise ValueError("Paddle log not found")
        return paddle


def create_paddle(paddle: PaddleLocation) -> PaddleLocation:
    with Session(engine) as session:
        session.add(paddle) # stages the object for insertion
        session.commit() # commits the staged object to the database
        session.refresh(paddle) # refreshes the object with the latest data from the database
        return paddle

def update_paddle(paddle_id: int, updated_paddle: PaddleLocation) -> PaddleLocation:
    with Session(engine) as session:
        paddle = session.get(PaddleLocation, paddle_id)
        if not paddle:
            raise ValueError("Paddle log not found")
        
        updated_data = updated_paddle.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(paddle, key, value)

        session.add(paddle)
        session.commit()
        session.refresh(paddle)
        return paddle

def patch_paddle(paddle_id: int, patch: PaddleUpdate) -> PaddleLocation:
    with Session(engine) as session:
        paddle = session.get(PaddleLocation, paddle_id)
        if not paddle:
            raise ValueError("Paddle log not found")
        
        patch_data = patch.model_dump(exclude_unset=True)
        for key, value in patch_data.items():
            setattr(paddle, key, value)

        session.add(paddle)
        session.commit()
        session.refresh(paddle)
        return paddle

def delete_paddle(paddle_id: int) -> None:
    with Session(engine) as session:
        paddle = session.get(PaddleLocation, paddle_id)
        if not paddle:
            raise ValueError("Paddle log not found")
        
        session.delete(paddle)
        session.commit()
