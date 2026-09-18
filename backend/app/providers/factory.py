from __future__ import annotations

import os
from typing import Tuple

from app.providers.base import AIImageProvider, AIVideoProvider
from app.providers.mock_provider import MockImageProvider, MockVideoProvider


def get_providers() -> Tuple[AIImageProvider, AIVideoProvider]:
    provider_name = os.getenv("AI_PROVIDER", "mock").lower()
    use_mock = os.getenv("USE_MOCK_PROVIDER", "true").lower() == "true"
    if use_mock or provider_name == "mock":
        return MockImageProvider(), MockVideoProvider()
    raise RuntimeError(f"Provider '{provider_name}' is not configured. Enable USE_MOCK_PROVIDER=true or add a provider implementation.")
