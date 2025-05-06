from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print("✅ .env loaded? DATABASE_URL =", os.getenv("DATABASE_URL"))

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    print("✅ Using DB:", engine.url)  # Shows which DB you're using
    from app.models import PaddleLocation
    SQLModel.metadata.create_all(engine)
