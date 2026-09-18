from __future__ import annotations

import uuid
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app.config import settings
from app.database.db import delete_generation, init_db, list_generations
from app.models.schemas import ImageGenerationRequest, VideoGenerationRequest
from app.services.generation_service import service

app = FastAPI(title=settings.APP_NAME, version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=settings.FRONTEND_URLS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
UPLOAD_DIR = settings.UPLOAD_DIR
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": settings.APP_NAME}


@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)) -> dict[str, object]:
    allowed_types = {"image/jpeg", "image/png", "image/webp", "image/jpg"}
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid image format. Please upload JPG, PNG, or WEBP.")
    file_bytes = await file.read()
    if len(file_bytes) > settings.MAX_UPLOAD_SIZE_BYTES:
        raise HTTPException(status_code=413, detail="Image is too large. Please upload a smaller file.")
    original_name = Path(file.filename or "upload").name
    safe_name = f"{uuid.uuid4().hex}_{original_name.replace(' ', '_')}"
    (UPLOAD_DIR / safe_name).write_bytes(file_bytes)
    return {"filename": safe_name, "url": f"/api/uploads/{safe_name}", "size": len(file_bytes), "content_type": file.content_type}


@app.get("/api/uploads/{filename}")
def get_uploaded_file(filename: str) -> FileResponse:
    file_path = UPLOAD_DIR / Path(filename).name
    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="Uploaded file not found")
    return FileResponse(file_path)


@app.post("/api/generate/image")
def generate_image(request: ImageGenerationRequest) -> dict[str, object]:
    try:
        return service.generate_image(request.prompt, request.reference_image, request.aspect_ratio, request.num_images)
    except RuntimeError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Image generation failed. Please try again.") from exc


@app.post("/api/generate/video")
def generate_video(request: VideoGenerationRequest) -> dict[str, object]:
    try:
        return service.create_video_job(request.prompt, request.image, request.duration, request.aspect_ratio, request.resolution)
    except RuntimeError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Video generation request failed. Please try again.") from exc


@app.get("/api/video/status/{job_id}")
def get_video_status(job_id: str) -> dict[str, object]:
    try:
        return service.get_video_status(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Video job not found.") from exc


@app.get("/api/history")
def get_history() -> dict[str, object]:
    return {"items": list_generations()}


@app.delete("/api/history/{generation_id}")
def delete_history_entry(generation_id: int) -> dict[str, str]:
    if not delete_generation(generation_id):
        raise HTTPException(status_code=404, detail="Generation not found")
    return {"status": "deleted", "generation_id": str(generation_id)}
