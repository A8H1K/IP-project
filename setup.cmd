@echo off

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and retry.
    exit /b 1
)

:: Install required Python packages
python -m pip install --upgrade pip
python -m pip install matplotlib mysql-connector-python pandas

:: Setting up MySQL Database
set MYSQL_USER=root
set MYSQL_PASSWORD=root
set MYSQL_DB=project_db

:: Create database and tables
python db_setup.py

:: Run main project script to generate required files
python "IP project.py"

echo Setup completed successfully!
pause
