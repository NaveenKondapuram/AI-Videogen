# AI Creative Studio

## Simplest Windows startup

1. Download and extract the repository.
2. Open PowerShell in the extracted project folder.
3. Run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\start.ps1
```

That single command automatically:

- creates the Python virtual environment if needed
- installs backend dependencies
- installs frontend dependencies
- starts the backend
- starts the frontend
- opens the app in your browser

Application: http://localhost:5173
Backend health: http://localhost:8000/health

The mock provider is enabled by default, so no AI API key is required for local testing.

To stop the app, close the two terminal windows opened by `start.ps1`.

## Manual startup

If you prefer separate terminals, use `run-backend.ps1` and `run-frontend.ps1`.
