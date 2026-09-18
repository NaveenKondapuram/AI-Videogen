const API_URL = import.meta.env.VITE_API_URL || ''

async function request(path, options = {}) {
  let response
  try {
    response = await fetch(`${API_URL}${path}`, {
      headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
      ...options,
    })
  } catch {
    throw new Error('Cannot connect to the backend. Start FastAPI on http://127.0.0.1:8000 and try again.')
  }

  const payload = await response.json().catch(() => ({}))
  if (!response.ok) throw new Error(payload.detail || `Request failed (${response.status})`)
  return payload
}

export async function checkHealth() {
  return request('/health')
}

export async function uploadImage(file) {
  const formData = new FormData()
  formData.append('file', file)
  let response
  try {
    response = await fetch(`${API_URL}/api/upload`, { method: 'POST', body: formData })
  } catch {
    throw new Error('Cannot connect to the backend. Start FastAPI on http://127.0.0.1:8000 and try again.')
  }
  const payload = await response.json().catch(() => ({}))
  if (!response.ok) throw new Error(payload.detail || `Upload failed (${response.status})`)
  return payload
}

export const generateImage = (data) => request('/api/generate/image', { method: 'POST', body: JSON.stringify(data) })
export const generateVideo = (data) => request('/api/generate/video', { method: 'POST', body: JSON.stringify(data) })
export const getVideoStatus = (jobId) => request(`/api/video/status/${jobId}`)
export const getHistory = async () => (await request('/api/history')).items || []
export const deleteHistoryItem = (id) => request(`/api/history/${id}`, { method: 'DELETE' })
