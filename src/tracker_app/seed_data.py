"""
Seed or update the assignments table from a Markdown tracker file or a CSV file.

Usage examples:

  # From tracker.md
  python -m tracker_app.seed_data --input ../tracker.md

  # From CSV
  python -m tracker_app.seed_data --input ../tracker.csv

If the file extension is .md, Markdown parsing is used.
If the file extension is .csv, CSV parsing is used.
"""

import argparse
import csv
import re
from pathlib import Path
from typing import List, Dict, Any, Optional

from tracker_app.db import init_db, get_connection


def parse_markdown_tracker(md_path: Path) -> List[Dict[str, Any]]:
    """
    Parse a Markdown tracker file with sections per week and task tables.

    Expected structure (like your tracker.md):
      ## Week 1 – ...
      | Day | Task | Links | Done | Notes |
      | --- | ---- | ----- | ---- | ----- |
      | Day 1 | ... | [Link](url) | - [ ] |  |
      ...

    Returns a list of dicts: {week, day, title, link, status, notes}.
    """
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    rows: List[Dict[str, Any]] = []
    current_week: Optional[int] = None

    # Regex to capture "Week N" from headings like "## Week 1 – ..."
    week_re = re.compile(r"^##\s+Week\s+(\d+)")
    # Regex to parse markdown link [text](url)
    link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    in_table = False

    for line in lines:
        # Detect week headings
        week_match = week_re.match(line.strip())
        if week_match:
            current_week = int(week_match.group(1))
            in_table = False
            continue

        # Detect table header row
        if line.strip().startswith("| Day |") and "Task" in line:
            in_table = True
            continue

        # Skip the separator row
        if in_table and line.strip().startswith("| ---"):
            continue

        if in_table:
            # End of table if we hit an empty line or a line not starting with '|'
            if not line.strip().startswith("|") or line.strip() == "":
                in_table = False
                continue

            # Split columns
            # Example row:
            # | Day 1 | Create GitHub repo... | [GitHub New Repo](https://github.com/new) | - [ ] |  |
            parts = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(parts) < 5:
                # Not enough columns, skip
                continue

            day_col, task_col, link_col, done_col, notes_col = parts[:5]

            # Extract day number: "Day 1" -> 1
            day_match = re.search(r"(\d+)", day_col)
            if not day_match:
                continue
            day = int(day_match.group(1))

            title = task_col

            # Extract link URL if present
            link_match = link_re.search(link_col)
            link = link_match.group(2) if link_match else ""

            # Status mapping from Markdown checkbox to status string
            # done_col like '- [ ]' or '- [x]'
            done_col = done_col.lower()
            if "- [x]" in done_col:
                status = "done"
            else:
                # You can extend to "in_progress" if you add a separate marker
                status = "pending"

            notes = notes_col.strip()

            # If week is not detected for some reason, default to 0
            week_val = current_week if current_week is not None else 0

            rows.append(
                {
                    "week": week_val,
                    "day": day,
                    "title": title,
                    "link": link,
                    "status": status,
                    "notes": notes,
                }
            )

    return rows


def parse_csv_tracker(csv_path: Path) -> List[Dict[str, Any]]:
    """
    Parse a CSV tracker file with columns:

      week, day, title, link, status, notes

    Missing columns will be defaulted where reasonable.
    """
    rows: List[Dict[str, Any]] = []

    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for raw in reader:
            week = int(raw.get("week", 0) or 0)
            day = int(raw.get("day", 0) or 0)
            title = (raw.get("title") or "").strip()
            if not title:
                continue

            link = (raw.get("link") or "").strip()
            status = (raw.get("status") or "pending").strip().lower()
            if status not in {"pending", "in_progress", "done"}:
                status = "pending"
            notes = (raw.get("notes") or "").strip()

            rows.append(
                {
                    "week": week,
                    "day": day,
                    "title": title,
                    "link": link,
                    "status": status,
                    "notes": notes,
                }
            )

    return rows


def upsert_assignments(rows: List[Dict[str, Any]]) -> None:
    """
    Upsert rows into the assignments table based on (week, day, title).
    Requires UNIQUE(week, day, title) in schema.
    """
    if not rows:
        print("No rows to upsert.")
        return

    conn = get_connection()
    try:
        with conn:
            conn.executemany(
                """
                INSERT INTO assignments (week, day, title, link, status, notes)
                VALUES (:week, :day, :title, :link, :status, :notes)
                ON CONFLICT(week, day, title) DO UPDATE SET
                    link   = excluded.link,
                    status = excluded.status,
                    notes  = excluded.notes
                """,
                rows,
            )
    finally:
        conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Seed or update assignments from a Markdown or CSV tracker."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        required=True,
        help="Path to tracker file (Markdown .md or CSV .csv)",
    )
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    init_db()

    ext = input_path.suffix.lower()
    if ext == ".md":
        rows = parse_markdown_tracker(input_path)
    elif ext == ".csv":
        rows = parse_csv_tracker(input_path)
    else:
        raise SystemExit("Unsupported file type. Use .md or .csv")

    print(f"Parsed {len(rows)} assignments from {input_path.name}")
    upsert_assignments(rows)
    print("Upsert completed.")


if __name__ == "__main__":
    main()