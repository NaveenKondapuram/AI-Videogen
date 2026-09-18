# AI Creative Studio

## Windows quick start

1. Download and extract the repository.
2. Open PowerShell in the extracted repository root.
3. Run `./run-backend.ps1` and leave it open.
4. Open a second PowerShell in the same root.
5. Run `./run-frontend.ps1` and leave it open.
6. Open http://localhost:5173.

The backend uses the mock provider by default, so no AI key is required. The backend health URL is http://localhost:8000/health.

If PowerShell blocks scripts, run `Set-ExecutionPolicy -Scope Process Bypass` once in that terminal, then run the script again.
