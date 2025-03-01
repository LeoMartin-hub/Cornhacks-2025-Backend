from fastapi import FastAPI
from app.routes.photos import router as photos_router

app = FastAPI()

# Include routes
app.include_router(photos_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Time Capsule API!"}