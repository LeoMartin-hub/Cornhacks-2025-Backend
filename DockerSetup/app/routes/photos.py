from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from datetime import datetime, timedelta
from app.models.photo import PhotoUpload, PhotoResponse
from app.encryption.encrypt import encrypt_data
from app.encryption.decrypt import decrypt_data
from app.utils.blockchain import store_key_on_blockchain
import os
from uuid import uuid4

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
    try:
        unlock_date = datetime.fromisoformat(unlock_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use ISO format (e.g., 2023-12-31T00:00:00).")

    min_unlock_date = datetime.now() + timedelta(days=180)
    if unlock_date < min_unlock_date:
        raise HTTPException(status_code=400, detail="Unlock date must be at least 6 months in the future")

    # Read the uploaded file
    try:
        file_data = await file.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read file: {str(e)}")

    # Generate a unique filename
    unique_filename = f"{uuid4().hex}.enc"
    file_path = f"app/storage/{unique_filename}"

    # Encrypt the photo
    try:
        key = get_random_bytes(16)  # Generate a new key for each file
        encrypted_data = encrypt_data(file_data, key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Encryption failed: {str(e)}")

    # Save the encrypted photo to storage
    try:
        os.makedirs("app/storage", exist_ok=True)  # Ensure the storage directory exists
        with open(file_path, "wb") as f:
            f.write(encrypted_data.encode())  # Write the base64-encoded data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

    # Store the encryption key on the blockchain
    transaction_hash = store_key_on_blockchain(key.hex(), unlock_date)

    # Save photo metadata to the database
    photo = {
        "id": len(photos_db) + 1,
        "description": description,
        "file_path": file_path,
        "unlock_date": unlock_date,
        "is_public": False,
        "transaction_hash": transaction_hash,
    }
    photos_db.append(photo)

    return photo