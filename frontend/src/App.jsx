import { useEffect, useState } from 'react'
import { checkHealth, generateImage, generateVideo, getHistory, getVideoStatus } from './services/api'

export default function App() {
  const [prompt, setPrompt] = useState('Create a cinematic scene of a futuristic city at night with flying cars.')
  const [type, setType] = useState('image')
  const [duration, setDuration] = useState(5)
  const [result, setResult] = useState(null)
  const [history, setHistory] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [backend, setBackend] = useState('checking')

  useEffect(() => {
    checkHealth().then(() => setBackend('online')).catch(() => setBackend('offline'))
    getHistory().then(setHistory).catch(() => {})
  }, [])

  async function handleGenerate() {
    if (!prompt.trim()) return setError('Enter a prompt first.')
    setLoading(true)
    setError('')
    setResult(null)
    try {
      if (type === 'image') {
        setResult(await generateImage({ prompt, reference_image: null, aspect_ratio: '16:9', num_images: 1 }))
      } else {
        const job = await generateVideo({ prompt, image: null, duration: Number(duration), aspect_ratio: '16:9', resolution: '720p' })
        setResult(job)
        const poll = async () => {
          const status = await getVideoStatus(job.job_id)
          setResult(status)
          if (status.status === 'processing') setTimeout(poll, 1000)
          else setLoading(false)
        }
        await poll()
      }
      setHistory(await getHistory())
    } catch (err) {
      setError(err.message || 'Generation failed')
    } finally {
      if (type === 'image') setLoading(false)
    }
  }

  return (
    <main className="page-shell">
      <header><p className="eyebrow">AI CREATIVE STUDIO</p><h1>Generate visuals with text, image references, and motion.</h1><p className={backend === 'online' ? 'online' : 'offline'}>Backend: {backend}</p></header>
      <section className="panel">
        <label htmlFor="prompt">Prompt</label>
        <textarea id="prompt" rows="5" value={prompt} onChange={(event) => setPrompt(event.target.value)} />
        <label>Generation type</label>
        <select value={type} onChange={(event) => setType(event.target.value)}><option value="image">Image</option><option value="video">Video</option></select>
        {type === 'video' && <><label htmlFor="duration">Duration (seconds)</label><input id="duration" type="number" min="1" max="30" value={duration} onChange={(event) => setDuration(event.target.value)} /></>}
        {error && <p className="error-box">{error}</p>}
        <button onClick={handleGenerate} disabled={loading || backend === 'offline'}>{loading ? 'Generating...' : 'Generate'}</button>
      </section>
      <section className="panel"><h2>Generated Result</h2>{result?.image_url && <img className="result-image" src={result.image_url} alt="Generated result" />}{result?.video_url && <video className="result-image" controls src={result.video_url} />}{result?.message && <p>{result.message}</p>}{!result && <p>Your generated image or video will appear here.</p>}</section>
      <section className="panel"><h2>Generation History</h2>{history.length ? history.map((item) => <p key={item.id}>{item.prompt}</p>) : <p>No generations yet.</p>}</section>
    </main>
  )
}
