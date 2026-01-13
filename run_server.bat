@echo off

REM Activate virtual environment
call venv\Scripts\activate

REM Start FastAPI server (NO reload for automation)
start "" cmd /k python -m uvicorn app.main:app

REM Give server enough time to bind the port
ping 127.0.0.1 -n 6 > nul

REM Open Swagger UI
start "" http://127.0.0.1:8000/docs
