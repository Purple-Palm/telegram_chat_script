@echo off
echo Starting telegram...

start Telegram.exe
timeout /t 4 /nobreak > nul

echo Starting script...
cd data
python main.py <api_id> <api_hash>