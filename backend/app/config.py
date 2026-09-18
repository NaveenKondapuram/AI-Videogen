from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR.parent / ".env")

class Settings:
    APP_NAME = "AI Creative Studio"
    BACKEND_HOST = os.getenv("BACKEND_HOST", "0.0.0.0")
    BACKEND_PORT = int(os.getenv("BACKEND_PORT", "8000"))
    FRONTEND_URLS = [
        origin.strip()
        for origin in os.getenv("BACKEND_CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")
        if origin.strip()
    ]
    USE_MOCK_PROVIDER = os.getenv("USE_MOCK_PROVIDER", "true").lower() == "true"
    AI_PROVIDER = os.getenv("AI_PROVIDER", "mock")
    AI_PROVIDER_API_KEY = os.getenv("AI_PROVIDER_API_KEY", "")
    MAX_UPLOAD_SIZE_MB = int(os.getenv("MAX_UPLOAD_SIZE_MB", "10"))
    MAX_UPLOAD_SIZE_BYTES = MAX_UPLOAD_SIZE_MB * 1024 * 1024
    UPLOAD_DIR = BASE_DIR / "uploads"

settings = Settings()
