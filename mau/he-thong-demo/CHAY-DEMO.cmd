@echo off
title He thong DEMO 8766 - Test AI Kit
cd /d "%~dp0"
echo He thong DEMO (gia lap) dang chay tai http://127.0.0.1:8766  - dong cua so nay de tat.
start "" http://127.0.0.1:8766
npx -y http-server@14.1.1 . -p 8766 -a 127.0.0.1 -c-1 --silent
