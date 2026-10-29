@echo off

py -m pip install py-cpuinfo
if %errorlevel% neq 0 (
    echo Failed to install py-cpuinfo, exiting.
    pause
    exit /b %errorlevel%
)

py index.py

pause
