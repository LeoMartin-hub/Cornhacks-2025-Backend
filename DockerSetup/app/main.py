from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.photos import router as photos_router

app = FastAPI()

# Configure allowed origins (adjust as needed)
origins = [
    "http://localhost:5173",  # For SvelteKit during development
    "http://localhost:3000",  # Alternative dev environment
    "*"
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allow specified origins
    allow_credentials=True,          # Allow cookies/auth headers
    allow_methods=["*"],             # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allow all headers
)

# Include routes
app.include_router(photos_router, prefix="/api")

@app.get("/")
def read_root():
    print("Welcome to the Time Capsule API!")
    return {"message": "Welcome to the Time Capsule API!"}
