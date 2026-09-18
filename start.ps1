$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

if (-not (Test-Path '.env')) {
  Copy-Item '.env.example' '.env'
}

if (-not (Test-Path '.venv\Scripts\python.exe')) {
  py -m venv '.venv'
}

Write-Host 'Installing backend dependencies...' -ForegroundColor Cyan
& '.\.venv\Scripts\python.exe' -m pip install -r '.\backend\requirements.txt'

Write-Host 'Installing frontend dependencies...' -ForegroundColor Cyan
Set-Location '.\frontend'
npm install
Set-Location $root

Write-Host 'Starting backend and frontend...' -ForegroundColor Green
Start-Process powershell -ArgumentList '-NoExit', '-ExecutionPolicy', 'Bypass', '-Command', "Set-Location '$root\backend'; & '$root\.venv\Scripts\python.exe' -m uvicorn app.main:app --host 127.0.0.1 --port 8000"
Start-Process powershell -ArgumentList '-NoExit', '-ExecutionPolicy', 'Bypass', '-Command', "Set-Location '$root\frontend'; npm run dev"

Start-Sleep -Seconds 2
Start-Process 'http://localhost:5173'
Write-Host 'Frontend: http://localhost:5173' -ForegroundColor Green
Write-Host 'Backend:  http://localhost:8000/health' -ForegroundColor Green
Write-Host 'Two new terminal windows were opened. Keep them running.' -ForegroundColor Yellow
