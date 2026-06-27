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
    echo Jika Anda menggunakan Windows 10/11, Microsoft Store mungkin akan terbuka 
    echo otomatis untuk menginstal Python. Jika tidak, browser akan mengarahkan
    echo Anda ke situs resmi Python.
    echo.
    echo PENTING: Saat menginstal, PASTIKAN mencentang opsi "Add Python to PATH"!
    echo.
    pause
    start https://www.python.org/downloads/
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
