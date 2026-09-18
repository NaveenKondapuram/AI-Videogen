from __future__ import annotations

import time
import uuid
from typing import Any

from app.database.db import save_generation
from app.providers.factory import get_providers

VIDEO_JOBS: dict[str, dict[str, Any]] = {}


class GenerationService:
    def __init__(self):
        self.image_provider, self.video_provider = get_providers()

    def generate_image(self, prompt: str, reference_image: str | None, aspect_ratio: str, num_images: int) -> dict[str, Any]:
        result = self.image_provider.generate_image(
            prompt=prompt,
            reference_image=reference_image,
            aspect_ratio=aspect_ratio,
            num_images=num_images,
        )
        record = {
            "prompt": prompt,
            "input_image": reference_image,
            "result_url": result.get("image_url"),
            "generation_type": "image",
            "status": "completed",
            "provider": self.image_provider.name,
            "metadata": {"aspect_ratio": aspect_ratio, "num_images": num_images, "note": result.get("note")},
        }
        save_generation(record)
        return {
            "status": "completed",
            "image_url": result.get("image_url"),
            "provider": self.image_provider.name,
            "message": result.get("note", "Image generation completed."),
        }

    def create_video_job(self, prompt: str, image: str | None, duration: int, aspect_ratio: str, resolution: str) -> dict[str, Any]:
        job_id = str(uuid.uuid4())
        VIDEO_JOBS[job_id] = {
            "job_id": job_id,
            "prompt": prompt,
            "image": image,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
            "status": "processing",
            "progress": 0,
            "created_at": time.time(),
            "provider": self.video_provider.name,
            "video_url": None,
        }

        save_generation({
            "prompt": prompt,
            "input_image": image,
            "result_url": None,
            "generation_type": "video",
            "status": "processing",
            "provider": self.video_provider.name,
            "metadata": {"duration": duration, "aspect_ratio": aspect_ratio, "resolution": resolution},
        })

        return {"job_id": job_id, "status": "processing", "provider": self.video_provider.name}

    def get_video_status(self, job_id: str) -> dict[str, Any]:
        if job_id not in VIDEO_JOBS:
            raise KeyError(f"Unknown job_id: {job_id}")

        job = VIDEO_JOBS[job_id]
        elapsed = time.time() - job["created_at"]
        if job["status"] == "processing":
            progress = min(100, int((elapsed / 4) * 100))
            job["progress"] = progress
            if elapsed >= 4:
                job["status"] = "completed"
                job["progress"] = 100
                job["video_url"] = "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
                job["note"] = "Mock provider is enabled. This is a placeholder URL for local development only."

        result = {
            "job_id": job_id,
            "status": job["status"],
            "progress": job["progress"],
            "provider": job["provider"],
        }
        if job.get("video_url"):
            result["video_url"] = job["video_url"]
        if job.get("note"):
            result["message"] = job["note"]
        return result


service = GenerationService()
