from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from datetime import datetime, timedelta
from Crypto.Random import get_random_bytes
from app.models.photo import PhotoResponse
from app.encryption.encrypt import encrypt_data
from app.encryption.decrypt import decrypt_data
#from app.index import store_key_on_blockchain
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
    print("test sucess")
    return photo