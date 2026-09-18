import os
from typing import Tuple

from app.providers.base import AIImageProvider, AIVideoProvider
from app.providers.mock_provider import MockImageProvider, MockVideoProvider


def get_providers() -> Tuple[AIImageProvider, AIVideoProvider]:
    provider_name = os.getenv("AI_PROVIDER", "mock").lower()
    use_mock = os.getenv("USE_MOCK_PROVIDER", "true").lower() == "true"

    if use_mock or provider_name == "mock":
        return MockImageProvider(), MockVideoProvider()

    if provider_name == "openai":
        raise RuntimeError("OpenAI provider is not configured in this starter project. Set USE_MOCK_PROVIDER=true or add a provider implementation.")

    if provider_name == "replicate":
        raise RuntimeError("Replicate provider is not configured in this starter project. Set USE_MOCK_PROVIDER=true or add a provider implementation.")

    raise RuntimeError(f"Unsupported AI provider '{provider_name}'. Configure a provider or enable the mock provider.")
