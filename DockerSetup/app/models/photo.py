from pydantic import BaseModel
from datetime import datetime

# Pydantic schema for photo upload
class PhotoUpload(BaseModel):
    description: str
    unlock_date: datetime

# Pydantic schema for photo response
class PhotoResponse(BaseModel):
    id: int
    description: str
    file_path: str
    unlock_date: datetime
    is_public: bool