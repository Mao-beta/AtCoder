@echo off
setlocal
cd /d "%~dp0"
set "PALETTE_PYTHON=%~dp0..\.venv\Scripts\pythonw.exe"
if not exist "%PALETTE_PYTHON%" (
    echo Python not found: "%PALETTE_PYTHON%"
    pause
    exit /b 1
)
start "" "%PALETTE_PYTHON%" "%~dp0cp_palette.py" %*
