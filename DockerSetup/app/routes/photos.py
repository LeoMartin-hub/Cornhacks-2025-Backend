from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from datetime import datetime, timedelta
from app.models.photo import PhotoResponse  # Ensure PhotoResponse is imported
from app.utils.encryption import encrypt_photo, decrypt_photo
# from app.utils.blockchain import store_key_on_blockchain, retrieve_key_from_blockchain (BLOCKHAIN KEYS)
# from app.utils.analysis import analyze_photo (POSSIBLE AI IMPLEMENTATION)
import os

router = APIRouter()

# In-memory storage for demo purposes 
photos_db = []

# Secret key for backdoor access 
BACKDOOR_SECRET_KEY = "hackathon2025"

@router.post("/upload", response_model=PhotoResponse)
async def upload_photo(description: str, unlock_date: datetime, file: UploadFile = File(...)):
    # Validate unlock date (must be at least 6 months in the future)
    min_unlock_date = datetime.now() + timedelta(days=180)
    if unlock_date < min_unlock_date:
        raise HTTPException(status_code=400, detail="Unlock date must be at least 6 months in the future")

    