import { useEffect, useState } from 'react'
import { generateImage, getHistory } from './services/api'

export default function App() {
  const [prompt, setPrompt] = useState('Create a cinematic scene of a futuristic city at night with flying cars.')
  const [result, setResult] = useState(null)
  const [history, setHistory] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  useEffect(() => { getHistory().then(setHistory).catch(() => {}) }, [])

  async function handleGenerate() {
    setLoading(true)
    setError('')
    try {
      const response = await generateImage({ prompt, reference_image: null, aspect_ratio: '16:9', num_images: 1 })
      setResult(response)
      setHistory(await getHistory())
    } catch (err) {
      setError(err.message || 'Generation failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="page-shell">
      <header><p className="eyebrow">AI CREATIVE STUDIO</p><h1>Generate visuals with text, image references, and motion.</h1></header>
      <section className="panel">
        <label htmlFor="prompt">Prompt</label>
        <textarea id="prompt" rows="5" value={prompt} onChange={(event) => setPrompt(event.target.value)} />
        {error && <p className="error-box">{error}</p>}
        <button onClick={handleGenerate} disabled={loading}>{loading ? 'Generating...' : 'Generate Image'}</button>
      </section>
      <section className="panel"><h2>Generated Result</h2>{result?.image_url ? <img className="result-image" src={result.image_url} alt="Generated result" /> : <p>Your generated image or video will appear here.</p>}</section>
      <section className="panel"><h2>Generation History</h2>{history.length ? history.map((item) => <p key={item.id}>{item.prompt}</p>) : <p>No generations yet.</p>}</section>
    </main>
  )
}
