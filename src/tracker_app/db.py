import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional

DB_DIR = Path(__file__).resolve().parents[2] / "db"
DB_PATH = DB_DIR / "tracker.db"


def get_connection() -> sqlite3.Connection:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS assignments (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                week    INTEGER NOT NULL,
                day     INTEGER NOT NULL,
                title   TEXT NOT NULL,
                link    TEXT,
                status  TEXT NOT NULL DEFAULT 'pending',
                notes   TEXT,
                UNIQUE (week, day, title)
            )
            """
        )
    conn.close()


def get_assignments_for_day(day: int) -> List[sqlite3.Row]:
    conn = get_connection()
    try:
        cur = conn.execute(
            "SELECT * FROM assignments WHERE day = ? ORDER BY id", (day,)
        )
        return cur.fetchall()
    finally:
        conn.close()


def update_assignment(
    assignment_id: int,
    status: Optional[str] = None,
    notes: Optional[str] = None,
) -> None:
    conn = get_connection()
    try:
        with conn:
            if status is not None and notes is not None:
                conn.execute(
                    "UPDATE assignments SET status = ?, notes = ? WHERE id = ?",
                    (status, notes, assignment_id),
                )
            elif status is not None:
                conn.execute(
                    "UPDATE assignments SET status = ? WHERE id = ?",
                    (status, assignment_id),
                )
            elif notes is not None:
                conn.execute(
                    "UPDATE assignments SET notes = ? WHERE id = ?",
                    (notes, assignment_id),
                )
    finally:
        conn.close()


def insert_assignments(rows: List[Dict[str, Any]]) -> None:
    conn = get_connection()
    try:
        with conn:
            conn.executemany(
                """
                INSERT INTO assignments (week, day, title, link, status, notes)
                VALUES (:week, :day, :title, :link, :status, :notes)
                """,
                rows,
            )
    finally:
        conn.close()