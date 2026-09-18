:root {
  color-scheme: dark;
  --bg: #09111f;
  --bg-soft: #111a2e;
  --panel: rgba(13, 20, 35, 0.9);
  --panel-border: rgba(148, 163, 184, 0.2);
  --card: #0f172a;
  --text: #e2e8f0;
  --muted: #94a3b8;
  --accent: #8b5cf6;
  --accent-2: #22d3ee;
  --success: #34d399;
  --danger: #f87171;
  --shadow: 0 20px 50px rgba(15, 23, 42, 0.45);
}

* {
  box-sizing: border-box;
}

html, body, #root {
  margin: 0;
  min-height: 100%;
  font-family: Inter, 'Segoe UI', sans-serif;
  background:
    radial-gradient(circle at top left, rgba(139, 92, 246, 0.24), transparent 28%),
    radial-gradient(circle at bottom right, rgba(34, 211, 238, 0.2), transparent 25%),
    var(--bg);
  color: var(--text);
}

button, input, select, textarea {
  font: inherit;
}

.page-shell {
  max-width: 1400px;
  margin: 0 auto;
  padding: 32px 20px 56px;
}

.topbar {
  margin-bottom: 20px;
}

.topbar h1 {
  margin: 8px 0 0;
  font-size: clamp(2rem, 3vw, 3rem);
  line-height: 1.1;
}

.eyebrow {
  margin: 0;
  color: var(--accent-2);
  letter-spacing: 0.18em;
  font-size: 0.75rem;
  font-weight: 700;
}

.studio-grid {
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  gap: 20px;
}

.panel {
  background: rgba(15, 23, 42, 0.82);
  border: 1px solid var(--panel-border);
  border-radius: 24px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(18px);
}

.creator-panel, .result-panel {
  padding: 24px;
}

.field-group {
  margin-bottom: 18px;
}

.field-group label {
  display: block;
  margin-bottom: 8px;
  font-size: 0.95rem;
  font-weight: 600;
}

textarea, input, select {
  width: 100%;
  border: 1px solid rgba(148, 163, 184, 0.2);
  background: rgba(15, 23, 42, 0.8);
  color: var(--text);
  border-radius: 16px;
  padding: 14px 16px;
}

textarea {
  resize: vertical;
  min-height: 130px;
}

.drop-zone {
  position: relative;
  min-height: 200px;
  border: 1px dashed rgba(148, 163, 184, 0.5);
  border-radius: 18px;
  background: rgba(9, 17, 31, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  cursor: pointer;
}

.drop-text {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  color: var(--muted);
}

.image-preview-wrap {
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-preview {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.settings-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.segmented-control {
  display: inline-flex;
  border: 1px solid rgba(148, 163, 184, 0.22);
  background: rgba(15, 23, 42, 0.9);
  border-radius: 14px;
  padding: 6px;
  gap: 10px;
}

.segmented-control button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: none;
  background: transparent;
  color: var(--text);
  padding: 10px 18px;
  border-radius: 10px;
  cursor: pointer;
}

.segmented-control button.active {
  background: linear-gradient(135deg, var(--accent), #6d28d9);
  box-shadow: 0 10px 30px rgba(139, 92, 246, 0.35);
}

.primary-button,
.secondary-button,
.chip,
.icon-button {
  border: none;
  cursor: pointer;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.primary-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  padding: 16px 20px;
  border-radius: 16px;
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
  color: white;
  font-weight: 700;
  box-shadow: 0 20px 35px rgba(139, 92, 246, 0.28);
}

.primary-button:disabled {
  opacity: 0.75;
  cursor: not-allowed;
}

.secondary-button,
.chip {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 14px;
  border-radius: 12px;
  background: rgba(148, 163, 184, 0.08);
  color: var(--text);
}

.secondary-button {
  background: rgba(148, 163, 184, 0.12);
}

.chip.danger {
  position: absolute;
  bottom: 12px;
  right: 12px;
  background: rgba(248, 113, 113, 0.12);
  color: #fecaca;
}

.small-status,
.status-note,
.empty-history {
  color: var(--muted);
}

.error-box {
  margin: 14px 0;
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(248, 113, 113, 0.1);
  border: 1px solid rgba(248, 113, 113, 0.3);
  color: #fecaca;
}

.result-header,
.history-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.result-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.empty-result {
  min-height: 430px;
  border: 1px dashed rgba(148, 163, 184, 0.28);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  color: var(--muted);
  gap: 12px;
  background: rgba(9, 17, 31, 0.65);
}

.media-stage {
  min-height: 430px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-radius: 18px;
  overflow: hidden;
  background: rgba(9, 17, 31, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.2);
}

.final-media {
  width: 100%;
  height: 100%;
  max-height: 520px;
  object-fit: cover;
}

.processing-box {
  align-items: center;
  justify-content: center;
  gap: 18px;
  padding: 16px;
}

.spinner {
  width: 38px;
  height: 38px;
  border: 4px solid rgba(148, 163, 184, 0.2);
  border-top-color: var(--accent-2);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.progress-bar {
  width: min(300px, 80%);
  height: 10px;
  background: rgba(148, 163, 184, 0.12);
  border-radius: 999px;
  overflow: hidden;
}

.progress-bar span {
  display: block;
  height: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg, var(--accent-2), var(--accent));
}

.history-panel {
  margin-top: 20px;
  padding: 22px 24px 18px;
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.history-item {
  display: grid;
  grid-template-columns: 120px minmax(0, 1fr) auto;
  gap: 14px;
  background: rgba(9, 17, 31, 0.72);
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 18px;
  padding: 12px;
}

.history-thumb-wrap {
  width: 120px;
  height: 84px;
  border-radius: 12px;
  overflow: hidden;
}

.history-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.history-thumb.placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(139, 92, 246, 0.2);
  color: white;
}

.history-body {
  min-width: 0;
}

.history-meta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 8px;
}

.pill {
  display: inline-flex;
  background: rgba(139, 92, 246, 0.2);
  color: #ddd6fe;
  padding: 4px 8px;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 700;
}

.pill.muted {
  background: rgba(148, 163, 184, 0.12);
  color: var(--muted);
}

.history-prompt {
  margin: 0 0 6px;
  font-weight: 600;
  line-height: 1.5;
}

.history-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.icon-button {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: rgba(148, 163, 184, 0.08);
  color: var(--text);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.icon-button.danger {
  background: rgba(248, 113, 113, 0.08);
  color: #fecaca;
}

@media (max-width: 900px) {
  .studio-grid {
    grid-template-columns: 1fr;
  }

  .history-item {
    grid-template-columns: 1fr;
  }
}
