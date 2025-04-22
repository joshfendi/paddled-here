from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Paddle World"}

# Include the router from app.routes
app.include_router(router)
