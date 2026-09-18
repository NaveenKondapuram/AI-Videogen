const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
    ...options,
  })
  const payload = await response.json().catch(() => ({}))
  if (!response.ok) throw new Error(payload.detail || 'Request failed')
  return payload
}

export async function uploadImage(file) {
  const formData = new FormData()
  formData.append('file', file)
  const response = await fetch(`${API_URL}/api/upload`, { method: 'POST', body: formData })
  const payload = await response.json().catch(() => ({}))
  if (!response.ok) throw new Error(payload.detail || 'Upload failed')
  return payload
}

export const generateImage = (data) => request('/api/generate/image', { method: 'POST', body: JSON.stringify(data) })
export const generateVideo = (data) => request('/api/generate/video', { method: 'POST', body: JSON.stringify(data) })
export const getVideoStatus = (jobId) => request(`/api/video/status/${jobId}`)
export const getHistory = async () => (await request('/api/history')).items || []
export const deleteHistoryItem = (id) => request(`/api/history/${id}`, { method: 'DELETE' })
