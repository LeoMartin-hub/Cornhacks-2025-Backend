from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from datetime import datetime, timedelta
from app.models.photo import PhotoUpload, PhotoResponse
from app.utils.encryption import encrypt_photo, decrypt_photo
from app.utils.blockchain import store_key_on_blockchain, retrieve_key_from_blockchain
from app.utils.analysis import analyze_photo
import os

router = APIRouter()

# In-memory storage for demo purposes 
photos_db = []

# Secret key for backdoor access 
BACKDOOR_SECRET_KEY = "hackathon2025"

@router.post("/upload", response_model=PhotoResponse)
async def upload_photo(file: UploadFile = File(...), description: str, unlock_date: datetime):
    # Validate unlock date (must be at least 6 months in the future)
    min_unlock_date = datetime.now() + timedelta(days=180)
    if unlock_date < min_unlock_date:
        raise HTTPException(status_code=400, detail="Unlock date must be at least 6 months in the future")

@router.get("/photo/{photo_id}", response_model=PhotoResponse)
async def get_photo(photo_id: int, secret_key: str = Query(None)):
    # Find the photo in the database
    photo = next((p for p in photos_db if p["id"] == photo_id), None)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")

    # Check if the unlock date has passed or if the backdoor secret key is provided
    if datetime.now() < photo["unlock_date"] and secret_key != BACKDOOR_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Photo is locked")

    # Decrypt the photo
    decrypted_photo = decrypt_photo(photo["encrypted_data"])

    return PhotoResponse(
        id=photo["id"],
        description=photo["description"],
        unlock_date=photo["unlock_date"],
        photo_data=decrypted_photo
    )

