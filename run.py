"""
Server Entry Point
Run with: python run.py
"""
from pathlib import Path
import sys

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import uvicorn
from app.config import HOST, PORT

if __name__ == "__main__":
    print(f"============================================================")
    print(f" Enterprise Expense Claim & Reimbursement Portal")
    print(f"============================================================")
    print(f" Dashboard URL:  http://{HOST}:{PORT}")
    print(f" Swagger Docs:   http://{HOST}:{PORT}/docs")
    print(f" API Docs Alias: http://{HOST}:{PORT}/api-docs")
    print(f" Health Check:   http://{HOST}:{PORT}/health")
    print(f"============================================================")
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=False)
