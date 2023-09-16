@echo off
Title Telechargement des modules...
python --version 3>NUL

if errorlevel 1 goto errorNoPython
pip -V>NUL

if errorlevel 1 goto errorNoPip
python -m pip install -r utils/requirements.txt

cls
Title Telechargement des modules
echo python main.py >> start.bat
start start.bat