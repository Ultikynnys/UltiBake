@echo off
REM Navigate to the directory of the batch file
cd /d "%~dp0"

REM Execute the Python script using pythonw to avoid opening a console window
pythonW changelogger.py
