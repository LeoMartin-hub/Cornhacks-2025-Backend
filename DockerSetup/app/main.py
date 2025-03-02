from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from app.routes.photos import router as photos_router




app = FastAPI()

origins = [
    "http://localhost:3000",  # Replace with your SvelteKit app's origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/upload")
async def upload_file(
    file: UploadFile = File(...),
    email: str = Form(...),
    time: str = Form(...),
    message: str = Form(...)
):
    # Process the uploaded file and other form data
    return {"filename": file.filename, "email": email, "time": time, "message": message}

@app.get("/")
def read_root():
    return {"Hello": "World"}
