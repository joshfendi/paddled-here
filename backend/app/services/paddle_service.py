from typing import List
from sqlmodel import Session, select
from app.db import engine
from app.models import PaddleLocation, PaddleUpdate

def get_all_paddles(user_name: str = None, team: str = None) -> List[PaddleLocation]:
    with Session(engine) as session:
        statement = select(PaddleLocation)

        if user_name:
            statement = statement.where(PaddleLocation.user_name == user_name)
        if team:
            statement = statement.where(PaddleLocation.team == team)

        results = session.exec(statement).all()
        return results
    
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
