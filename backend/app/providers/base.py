from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class AIImageProvider(ABC):
    name: str = "base"

    @abstractmethod
    def generate_image(self, prompt: str, reference_image: Optional[str] = None, aspect_ratio: str = "16:9", num_images: int = 1, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError


class AIVideoProvider(ABC):
    name: str = "base"

    @abstractmethod
    def generate_video(self, prompt: str, image: Optional[str] = None, duration: int = 5, aspect_ratio: str = "16:9", resolution: str = "720p", **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError
