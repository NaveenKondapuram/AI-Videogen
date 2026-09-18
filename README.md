# AI Creative Studio

Modern AI image and video generation app built with React + Vite frontend and Python FastAPI backend.

## Overview

This project allows users to:

- Enter a text prompt
- Upload an optional reference image
- Choose between image generation and video generation
- Use mock provider mode when no real AI API key is configured
- Save generation history locally in SQLite
- Poll video generation status and display results

## Features

- Responsive single-page UI
- Prompt + image reference flow
- Image and video generation modes
- Async video processing simulation with polling
- Upload validation and sanitization
- Provider abstraction for swapping vendors later
- History management with local SQLite persistence
- Clear error messages without exposing secrets

## Architecture

- Frontend: React + Vite + CSS
- Backend: FastAPI + Pydantic
- Storage: SQLite for generation history
- Providers: modular AI image/video provider abstraction
- Mock mode: `USE_MOCK_PROVIDER=true`

## Quick Start

1. Copy `.env.example` to `.env`
2. Install backend dependencies
3. Install frontend dependencies
4. Start backend
5. Start frontend

## Environment Setup

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Example values:

```env
USE_MOCK_PROVIDER=true
AI_PROVIDER=mock
AI_PROVIDER_API_KEY=
BACKEND_CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
MAX_UPLOAD_SIZE_MB=10
```

## Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Docker Compose

```bash
docker-compose up --build
```

## API Routes

- `POST /api/generate/image`
- `POST /api/generate/video`
- `GET /api/video/status/{job_id}`
- `POST /api/upload`
- `GET /api/history`
- `DELETE /api/history/{generation_id}`

## Example Requests

### Image generation

```bash
curl -X POST http://localhost:8000/api/generate/image \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A cinematic futuristic city at night with flying cars",
    "reference_image": "",
    "aspect_ratio": "16:9",
    "num_images": 1
  }'
```

### Video generation

```bash
curl -X POST http://localhost:8000/api/generate/video \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A cinematic camera slowly moves toward the character while the wind moves the trees.",
    "image": "",
    "duration": 5,
    "aspect_ratio": "16:9",
    "resolution": "720p"
  }'
```

### Upload image

```bash
curl -X POST http://localhost:8000/api/upload \
  -F "file=@/path/to/image.png"
```

## Mock Provider Behavior

When `USE_MOCK_PROVIDER=true`, the app automatically uses the mock provider. The mock provider is clearly labeled as mock in the API response and UI, and it is intended for development and local testing only.

## Provider Integration

To add a real provider, implement one of these interfaces and register it in the provider factory:

- `AIImageProvider`
- `AIVideoProvider`

The frontend remains unchanged because generation requests are routed through the backend abstraction layer.

## Security Notes

- Store keys only in backend environment variables
- Do not commit `.env`
- Validate file type and file size before accepting uploads
- Restrict CORS to trusted frontend origins

## License

This project is intended as a starter for AI generation workflows and can be customized to your preferred provider stack.
