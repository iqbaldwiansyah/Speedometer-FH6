@echo off
title Instalasi Kebutuhan Forza Overlay
echo ==============================================
echo  Memeriksa Kebutuhan Sistem
echo ==============================================
echo.

:: Cek apakah Python sudah terinstal
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [X] Python belum terinstal atau tidak terdeteksi di PATH!
    echo.
    echo Silakan download dan instal Python secara manual dari:
    echo https://www.python.org/downloads/
    echo.
    echo PENTING: Saat menginstal, PASTIKAN mencentang opsi "Add Python to PATH"!
    echo.
    pause
    exit /b
)

echo [v] Python terdeteksi.
echo.
echo ==============================================
echo  Menginstal Library (websockets)
echo ==============================================
echo.
pip install websockets

echo.
echo ==============================================
echo Instalasi selesai! Semua kebutuhan sudah siap.
echo Sekarang Anda bisa menjalankan start.bat
echo ==============================================
pause
