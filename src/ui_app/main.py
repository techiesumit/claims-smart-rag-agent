from pathlib import Path
from typing import List

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse

import sqlite3
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Paths
ROOT_DIR = Path(__file__).resolve().parents[2]
DB_PATH = ROOT_DIR / "db" / "tracker.db"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

print("Templates directory:", TEMPLATES_DIR)
print("Exists:", TEMPLATES_DIR.exists())
print("Files:", list(TEMPLATES_DIR.glob("*")))

# Create Jinja2 environment directly (bypass Jinja2Templates)
env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    autoescape=select_autoescape(["html", "xml"]),
)

app = FastAPI(title="Claims-Smart RAG - Assignment UI")


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/")
async def home(request: Request):
    # Simple home that redirects to Day 1 by default
    return RedirectResponse(url="/day/1", status_code=302)


@app.get("/day/{day}", response_class=HTMLResponse)
async def view_day(day: int, request: Request):
    conn = get_db_connection()
    try:
        cur = conn.execute(
            "SELECT * FROM assignments WHERE day = ? ORDER BY id",
            (day,),
        )
        rows = cur.fetchall()
    finally:
        conn.close()

    assignments: List[sqlite3.Row] = rows or []

    template = env.get_template("day.html")
    html = template.render(
        request=request,
        day=day,
        assignments=assignments,
        status_options=["pending", "in_progress", "done"],
    )
    return HTMLResponse(content=html)


@app.post("/assignment/{assignment_id}")
async def update_assignment(
    assignment_id: int,
    day: int = Form(...),
    status: str = Form(...),
    notes: str = Form(""),
):
    if status not in ["pending", "in_progress", "done"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    conn = get_db_connection()
    try:
        with conn:
            cur = conn.execute(
                "UPDATE assignments SET status = ?, notes = ? WHERE id = ?",
                (status, notes, assignment_id),
            )
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Assignment not found")
    finally:
        conn.close()

    # Redirect back to the same day view
    return RedirectResponse(url=f"/day/{day}", status_code=303)