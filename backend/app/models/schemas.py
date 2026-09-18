from pydantic import BaseModel, Field, field_validator
from typing import Optional


class ImageGenerationRequest(BaseModel):
    prompt: str = Field(..., min_length=3, description="Text prompt for image generation")
    reference_image: Optional[str] = Field(default=None, description="Optional uploaded image URL")
    aspect_ratio: str = Field(default="16:9", description="Image aspect ratio")
    num_images: int = Field(default=1, ge=1, le=4)

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Prompt is required")
        return value.strip()


class VideoGenerationRequest(BaseModel):
    prompt: str = Field(..., min_length=3, description="Text prompt for video generation")
    image: Optional[str] = Field(default=None, description="Optional reference image for video generation")
    duration: int = Field(default=5, ge=1, le=30)
    aspect_ratio: str = Field(default="16:9")
    resolution: str = Field(default="720p")

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Prompt is required")
        return value.strip()


class UploadResponse(BaseModel):
    filename: str
    url: str
    size: int
    content_type: str


class GenerationRecord(BaseModel):
    id: int
    prompt: str
    input_image: Optional[str]
    result_url: Optional[str]
    generation_type: str
    status: str
    provider: str
    created_at: str


class GenerationHistoryResponse(BaseModel):
    items: list[GenerationRecord]
