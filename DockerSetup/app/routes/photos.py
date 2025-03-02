from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from datetime import datetime, timedelta
from app.models.photo import PhotoUpload, PhotoResponse
from app.encryption.encrypt import encrypt_data
from app.encryption.decrypt import decrypt_data
from app.utils.blockchain import store_key_on_blockchain
import os

router = APIRouter()

# In-memory storage for demo purposes (replace with a database in production)
photos_db = []

@router.post("/upload", response_model=PhotoResponse)
async def upload_photo(
    file: UploadFile = File(...),  # File upload
    description: str = Form(...),  # Form field for description
    unlock_date: str = Form(...)   # Form field for unlock_date
):
    # Validate unlock date (must be at least 6 months in the future)
    unlock_date = datetime.fromisoformat(unlock_date)
    min_unlock_date = datetime.now() + timedelta(days=180)
    if unlock_date < min_unlock_date:
        raise HTTPException(status_code=400, detail="Unlock date must be at least 6 months in the future")

    # Read the uploaded file
    file_data = await file.read()

    # Encrypt the photo and retrieve the key
    encrypted_data, key = encrypt_data(file_data)

    # Save the encrypted photo to storage
    file_path = f"app/storage/{file.filename}.enc"
    with open(file_path, "wb") as f:
        f.write(encrypted_data)

    # Store the encryption key on the blockchain
    transaction_hash = store_key_on_blockchain(key.hex(), unlock_date)

    # Save photo metadata to the database
    photo = {
        "id": len(photos_db) + 1,
        "description": description,
        "file_path": file_path,
        "unlock_date": unlock_date,
        "is_public": False,
    }
    photos_db.append(photo)

    return photo