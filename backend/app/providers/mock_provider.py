from __future__ import annotations

import base64
from html import escape
from typing import Any, Optional

from app.providers.base import AIImageProvider, AIVideoProvider


class MockImageProvider(AIImageProvider):
    name = "mock"

    def generate_image(self, prompt: str, reference_image: Optional[str] = None, aspect_ratio: str = "16:9", num_images: int = 1, **kwargs: Any) -> dict[str, Any]:
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675"><defs><linearGradient id="bg" x1="0%" x2="100%" y1="0%" y2="100%"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#7c3aed"/></linearGradient></defs><rect width="1200" height="675" fill="url(#bg)"/><circle cx="980" cy="120" r="80" fill="#fbbf24"/><circle cx="200" cy="560" r="110" fill="#22d3ee" opacity=".5"/><rect x="70" y="70" width="1060" height="535" rx="28" fill="none" stroke="#ffffff" stroke-opacity=".3"/><text x="600" y="330" text-anchor="middle" fill="white" font-size="42" font-family="Arial" font-weight="700">Mock AI Image</text><text x="600" y="390" text-anchor="middle" fill="#dbeafe" font-size="24" font-family="Arial">prompt: {escape(prompt[:80])}</text><text x="600" y="455" text-anchor="middle" fill="#dbeafe" font-size="20" font-family="Arial">Provider: mock • aspect ratio: {escape(aspect_ratio)}</text></svg>'''
        encoded = base64.b64encode(svg.encode("utf-8")).decode("ascii")
        return {"image_url": f"data:image/svg+xml;base64,{encoded}", "provider": self.name, "note": "Mock provider is enabled. This is a local placeholder image, not a real AI-generated asset."}


class MockVideoProvider(AIVideoProvider):
    name = "mock"

    def generate_video(self, prompt: str, image: Optional[str] = None, duration: int = 5, aspect_ratio: str = "16:9", resolution: str = "720p", **kwargs: Any) -> dict[str, Any]:
        return {"job_id": kwargs.get("job_id", "mock-job-id"), "status": "processing", "provider": self.name, "video_url": "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4", "note": "Mock provider is enabled. This is a placeholder video URL for local development only.", "duration": duration, "aspect_ratio": aspect_ratio, "resolution": resolution}
