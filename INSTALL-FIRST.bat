@echo off

echo Installing Git Bash emulator...
choco install git -y

echo Installing telethon library for Python
pip install telethon

echo Installing asyncio and telethon libraries...
pip install asyncio telethon

echo Installing pyyaml library...
pip install pyyaml

echo Installing......
timeout /t 1 >nul
echo Installing, do not close window!

timeout /t 10 >nul
setlocal enabledelayedexpansion
set count=10
:countdown
cls
echo Script finished its work!
echo Enjoy our script v1.1.0!
echo .
echo Closing the window in !count! seconds...
set /a count-=1
if !count! GTR 0 (
  timeout /t 1 >nul
  goto countdown
)
endlocal
exit
