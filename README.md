# Forza Horizon 6 — Overlay Speedometer & Tachometer

Overlay speedometer dan tachometer untuk Forza Horizon 6 berbasis web yang bisa digunakan untuk live streaming (OBS / TikTok Live Studio) dengan fitur kustomisasi lengkap.

## 1. Persiapan & Menjalankan Relay
Overlay ini membutuhkan script Python untuk meneruskan data dari game (UDP) ke browser (WebSocket).
1. Double-klik file **`install_requirements.bat`**. Script ini otomatis mengecek apakah Python sudah terinstal dan akan menginstal library yang dibutuhkan (`websockets`).
2. Jika Python belum terinstal, script akan mengarahkan Anda untuk mendownloadnya. **Penting:** Pastikan mencentang "Add Python to PATH" saat menginstal Python.
3. Setelah instalasi selesai, jalankan file **`start.bat`** (atau `python forza_relay.py` secara manual). 
4. Biarkan jendela console tetap terbuka selama Anda bermain.

Secara default relay mendengar UDP di port **7777** dan menyiarkan ke WebSocket di **ws://localhost:8765**.

## 2. Atur Data Out di Game Forza
Buka game Forza Horizon 6, masuk ke:
**Settings → HUD and Gameplay → Data Out**:
- Data Out: **On**
- Data Out IP Address: **127.0.0.1**
- Data Out IP Port: **7777** (harus sama dengan port di `forza_relay.py`)

## 3. Cara Mengatur Konfigurasi (Warna, Font, Jarak)
Anda dapat mengubah tampilan overlay secara *live* tanpa coding!
1. Double-klik file **`start_configurator.bat`** (atau jalankan `python config_tool.py` secara manual).
2. Browser Anda akan otomatis membuka **Live Web Configurator**.
3. Di sini Anda bisa mengatur:
   - Font untuk label dan angka digital
   - Warna teks, angka, jarum, dan garis (Group Merah, Hijau, Kuning)
   - Ukuran font khusus untuk **Nama Mobil**
   - Jarak antar meteran dan transparansi gambar
4. Klik **Simpan** untuk menerapkan perubahan ke overlay utama Anda.

## 4. Cara Membuat Custom Tema (Gambar Dial)
Anda bisa membuat tema background custom untuk speedometer dan tachometer sesuai selera Anda dengan sistem tema baru.
1. Buat folder baru di dalam folder **`themes/`** (misalnya `themes/Tema_Saya`).
2. Siapkan desain Anda dengan ukuran **direkomendasikan 600x600 pixels** (aspek rasio 1:1) berformat `.png` transparan.
3. Simpan gambar tersebut ke dalam folder tema Anda:
   - Untuk Speedometer: beri nama `speedometer.png`
   - Untuk Tachometer: beri nama `tacho.png`
4. Copy file `config.js` dan `description.json` dari folder tema lain (misalnya dari `themes/default/`) ke dalam folder tema baru Anda. Anda bisa mengedit `description.json` untuk mengganti nama tema.
5. Jalankan **Live Web Configurator**, dan tema baru Anda akan otomatis muncul di daftar pilihan tema siap untuk digunakan!

## 5. Cara Memasang di OBS Studio
1. Buka OBS Studio.
2. Di panel **Sources**, klik tombol **+** dan pilih **Browser**.
3. Centang kotak **Local file** dan klik **Browse**.
4. Pilih file `overlay_transparent.html` di folder ini.
5. Atur ukurannya (misal Width: 800, Height: 400).
6. Hapus isi dari kolom **Custom CSS** agar background benar-benar transparan.
7. Klik OK, lalu posisikan overlay di atas layar game Anda.

## 6. Cara Memasang di TikTok Live Studio
1. Buka TikTok Live Studio.
2. Tambahkan Source baru, pilih **Link / Tautan Web** (jika ada dukungan file lokal, pilih file `overlay_transparent.html`).
3. Jika TikTok Studio tidak mendukung file lokal secara langsung, Anda bisa membuka `overlay_transparent.html` di browser (seperti Chrome), lalu di TikTok Studio tambahkan **Window Capture** / **Tangkapan Jendela**.
4. Jika menggunakan Window Capture, Anda bisa menggunakan fitur *Chroma Key* di TikTok Studio untuk menghilangkan background hitamnya jika diperlukan. (Catatan: Overlay ini secara native sudah transparan jika di-load sebagai Browser Source).

## Catatan Tambahan
- Jika overlay belum terkoneksi ke game, ia akan berjalan dalam **Mode Demo** (simulasi) agar Anda tetap bisa mengatur warna dan memposisikan overlay di OBS.
- Skala speedometer: 0–320 km/h (tetap).
- Skala tachometer (RPM) otomatis menyesuaikan batas maksimal RPM mobil yang sedang dipakai di dalam game.
