from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="AI Seminar Static Host")
app.mount("/images", StaticFiles(directory=str(BASE_DIR / "images")), name="images")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def root():
    return RedirectResponse(url="/server-laptop-hosting-guide.html")


@app.get("/guide")
def guide():
    return RedirectResponse(url="/server-laptop-hosting-guide.html")


@app.get("/server-laptop-hosting-guide.html")
def server_laptop_guide():
    return FileResponse(BASE_DIR / "server-laptop-hosting-guide.html")


@app.get("/phone-server-guide.html")
def phone_guide():
    return FileResponse(BASE_DIR / "phone-server-guide.html")


@app.get("/token-frugal-agent-playbook-2026.html")
def token_page():
    return FileResponse(BASE_DIR / "token-frugal-agent-playbook-2026.html")


@app.get("/claude-masterclass-2026.html")
def claude_page():
    return FileResponse(BASE_DIR / "claude-masterclass-2026.html")
