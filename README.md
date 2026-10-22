# ExperimentIQ

ML-powered A/B testing and business experimentation intelligence platform.

> **Status:** In development (15-day build). See [PROJECT_PROGRESS.md](PROJECT_PROGRESS.md).

## Quick start (Windows, PowerShell)

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Run the API (terminal 1):
```powershell
uvicorn experimentiq.api.main:app --reload
```
Swagger docs: http://127.0.0.1:8000/docs

Run the dashboard (terminal 2, venv activated):
```powershell
streamlit run dashboard/app.py
```

Run tests:
```powershell
pytest
```

## Data disclaimer
Results on the synthetic dataset are **synthetic**, not from a real company.

## Progress
- [x] Day 1: project setup, minimal API + dashboard