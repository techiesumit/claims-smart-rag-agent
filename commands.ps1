# 1) Go to project root
cd d:\claims-smart-rag-agent

# 2) Create virtual environment named .venv
python -m venv .venv

# 3) Activate the venv (PowerShell)
.\.venv\Scripts\Activate.ps1

# 4) Install dependencies from requirements.txt
pip install -r .\requirements.txt

# 5) Run seed_data.py using tracker.md as input
cd .\src

python -m tracker_app.seed_data --input ..\tracker.md

Optional
python -m tracker_app.seed_data --input tracker.csv


# Run the FastAPI app (from repo root)
uvicorn ui_app.main:app --reload --app-dir .\src --port 8000