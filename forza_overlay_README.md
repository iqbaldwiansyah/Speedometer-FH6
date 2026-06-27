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
1. Jalankan `python config_tool.py`.
2. Browser Anda akan otomatis membuka **Live Web Configurator**.
3. Di sini Anda bisa mengatur:
   - Font untuk label dan angka digital
   - Warna teks, angka, jarum, dan garis (Group Merah, Hijau, Kuning)
   - Ukuran font khusus untuk **Nama Mobil**
   - Jarak antar meteran dan transparansi gambar
4. Klik **Simpan** untuk menerapkan perubahan ke overlay utama Anda.

## 4. Cara Membuat Custom Tema (Gambar Dial)
Anda bisa mengganti background dari speedometer dan tachometer sesuai selera Anda.
1. Buat gambar desain Anda dengan ukuran **direkomendasikan 600x600 pixels** (aspek rasio 1:1) dan simpan dalam format `.png` dengan *background transparent*.
2. Simpan gambar tersebut ke dalam folder `image/`.
   - Untuk Speedometer: beri nama `speedometer.png`
   - Untuk Tachometer: beri nama `tacho.png`
3. Refresh overlay Anda, dan gambar akan otomatis termuat. Anda bisa mengatur tingkat kecerahan dan transparansi gambar melalui Configurator.

## 5. Cara Memasang di OBS Studio
1. Buka OBS Studio.
2. Di panel **Sources**, klik tombol **+** dan pilih **Browser**.
3. Centang kotak **Local file** dan klik **Browse**.
4. Pilih file `forza_overlay.html` di folder ini.
5. Atur ukurannya (misal Width: 800, Height: 400).
6. Hapus isi dari kolom **Custom CSS** agar background benar-benar transparan.
7. Klik OK, lalu posisikan overlay di atas layar game Anda.

## 6. Cara Memasang di TikTok Live Studio
1. Buka TikTok Live Studio.
2. Tambahkan Source baru, pilih **Link / Tautan Web** (jika ada dukungan file lokal, pilih file `forza_overlay.html`).
3. Jika TikTok Studio tidak mendukung file lokal secara langsung, Anda bisa membuka `forza_overlay.html` di browser (seperti Chrome), lalu di TikTok Studio tambahkan **Window Capture** / **Tangkapan Jendela**.
4. Jika menggunakan Window Capture, Anda bisa menggunakan fitur *Chroma Key* di TikTok Studio untuk menghilangkan background hitamnya jika diperlukan. (Catatan: Overlay ini secara native sudah transparan jika di-load sebagai Browser Source).

## Catatan Tambahan
- Jika overlay belum terkoneksi ke game, ia akan berjalan dalam **Mode Demo** (simulasi) agar Anda tetap bisa mengatur warna dan memposisikan overlay di OBS.
- Skala speedometer: 0–320 km/h (tetap).
- Skala tachometer (RPM) otomatis menyesuaikan batas maksimal RPM mobil yang sedang dipakai di dalam game.
