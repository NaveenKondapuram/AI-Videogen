const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  })

  const payload = await response.json().catch(() => ({}))

  if (!response.ok) {
    throw new Error(payload.detail || 'Request failed')
  }

  return payload
}

export async function uploadImage(file) {
  const formData = new FormData()
  formData.append('file', file)

  const response = await fetch(`${API_URL}/api/upload`, {
    method: 'POST',
    body: formData,
  })

  const payload = await response.json().catch(() => ({}))

  if (!response.ok) {
    throw new Error(payload.detail || 'Upload failed')
  }

  return payload
}

export async function generateImage(data) {
  return request('/api/generate/image', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function generateVideo(data) {
  return request('/api/generate/video', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function getVideoStatus(jobId) {
  return request(`/api/video/status/${jobId}`)
}

export async function getHistory() {
  const data = await request('/api/history')
  return data.items || []
}

export async function deleteHistoryItem(id) {
  return request(`/api/history/${id}`, { method: 'DELETE' })
}
