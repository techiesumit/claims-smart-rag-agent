from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Hard-code templates directory just for this test
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

print("Templates directory:", TEMPLATES_DIR)
print("Exists:", TEMPLATES_DIR.exists())
print("Files:", list(TEMPLATES_DIR.glob("*")))

app = FastAPI(title="Test Jinja App")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.get("/test", response_class=HTMLResponse)
async def test_view(request: Request):
    return templates.TemplateResponse(
        "day.html",  # same template you already have
        {
            "request": request,
            "day": 1,
            "assignments": [],
            "status_options": ["pending", "in_progress", "done"],
        },
    )