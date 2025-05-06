from fastapi import FastAPI
from app.routes import router
from app.db import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---- startup ----
    init_db()          # create tables, etc.
    yield
    # ---- shutdown ---  (optional clean‑up)
    # engine.dispose()  # if you have a pooled engine

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Hello, Paddle World"}

# Include the router from app.routes
app.include_router(router)
