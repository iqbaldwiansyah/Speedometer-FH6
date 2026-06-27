<div align="center">
  <h1>🏎️ Forza Horizon 6 - Web Gauge Overlay</h1>
  <p>
    <i>Interactive, customizable, and stream-ready speedometer and tachometer overlay for Forza Horizon 6.</i>
  </p>
  <p>
    <a href="#-bahasa-indonesia">🇮🇩 Bahasa Indonesia</a> •
    <a href="#-english">🇬🇧 English</a>
  </p>
</div>

---

## 🇮🇩 Bahasa Indonesia

### 🌟 Fitur Utama
- **Real-Time Data**: Indikator Speedometer, RPM (Tachometer), dan Gear yang mulus dan sangat responsif, dikirim langsung dari *telemetry* game.
- **Live Web Configurator**: Ubah ukuran font, warna teks, jarum, jarak meteran, hingga visibilitas UI secara *live* tanpa perlu menyentuh satu baris kode pun.
- **Sistem Tema Dinamis**: Ganti desain *dial* atau panel dengan mudah. Tersedia beberapa tema bawaan.
- **Siap Streaming**: Layar otomatis transparan. Tinggal pasang di OBS Studio atau TikTok Live Studio.

### 📥 Cara Download / Instalasi
1. Klik tombol hijau **Code** di kanan atas halaman repositori ini.
2. Pilih **Download ZIP** lalu ekstrak folder tersebut di komputer Anda.
   *(Bagi pengguna Git: `git clone https://github.com/iqbaldwiansyah/Speedometer-FH6.git`)*
3. Masuk ke dalam folder hasil ekstraksi tersebut.

### 🚀 Cara Penggunaan
1. **Persiapan:** Double-klik file **`install_requirements.bat`**. Script ini otomatis mengecek dan menginstal Python serta *library* yang dibutuhkan (`websockets`). *(Catatan: Pastikan mencentang "Add Python to PATH" saat menginstal Python)*.
2. **Jalankan Relay:** Setelah siap, double-klik **`start.bat`** untuk mulai menerima data dari game. Biarkan jendela console tetap terbuka selama Anda bermain.
3. **Pengaturan di Game:** Buka Forza Horizon 6 -> **Settings -> HUD and Gameplay -> Data Out**:
   - Data Out: **On**
   - Data Out IP Address: **127.0.0.1**
   - Data Out IP Port: **7777**

### 🎨 Live Configurator & Custom Tema
1. Jalankan **`start_configurator.bat`** (otomatis membuka browser).
2. Anda bisa mengubah warna, font, dll, lalu klik **Simpan**.
3. **Membuat Tema Sendiri:** 
   - Buat folder baru di dalam direktori `themes/` (contoh: `themes/Tema_Saya`).
   - Masukkan desain Anda dengan nama `speedometer.png` dan `tacho.png` (ukuran *direkomendasikan 600x600 px*, format `.png` transparan).
   - Salin file `config.js` dan `description.json` dari tema bawaan (misal `themes/default/`) ke folder tema Anda. Edit `description.json` jika ingin mengubah nama.
   - Tema baru Anda akan otomatis terdeteksi di *Live Configurator*!

### 📹 Integrasi Software Streaming
- **OBS Studio:** Tambahkan Source baru -> **Browser**. Centang kotak **Local file**, pilih `overlay_transparent.html`. Kosongkan bagian *Custom CSS* agar layar tetap transparan. Atur ukurannya (misal 800x400).
- **TikTok Live Studio:** Tambahkan **Link / Tautan Web** (pilih file lokal jika didukung), atau buka file `overlay_transparent.html` di Google Chrome lalu tambahkan sebagai **Window Capture** di TikTok Studio.

### 🛠️ Panduan Developer & Kontribusi
Ingin menambahkan fitur, memperbaiki *bug*, atau mengembangkan script ini? Sangat disilakan (*Pull Requests are welcome*)!
- **Alur Data (Architecture):** 
  `Forza Horizon 6 (UDP 7777)` ➡️ `forza_relay.py` (Membaca struktur paket UDP) ➡️ `WebSocket (ws://localhost:8765)` ➡️ `overlay_transparent.html` (Melakukan render UI dengan JS/CSS).
- **Mengubah UI Editor:** Jika Anda menambah input baru di `editor.html`, pastikan variabel tersebut diambil oleh fungsi `gatherConfig()` dan ditangani dengan benar pada fungsi `parseAndApplyConfig()`.
- **Relay Script:** Struktur paket UDP Forza Horizon (V1/V2) bersifat sangat rigid. Jika Anda butuh menambah telemetri baru (misalnya *suspension travel* atau *tire temp*), sesuaikan *struct packing/unpacking* di dalam `forza_relay.py`.

---

## 🇬🇧 English

### 🌟 Key Features
- **Real-Time Data**: Ultra-smooth Speedometer, RPM (Tachometer), and Gear indicators derived directly from game telemetry.
- **Live Web Configurator**: Tweak font sizes, text colors, needles, gauge spacing, and UI visibility in real-time—no coding required.
- **Dynamic Theme System**: Switch dial background designs on the fly. Comes with multiple built-in themes.
- **Stream Ready**: Natively transparent background. Drag and drop ready for OBS Studio or TikTok Live Studio.

### 📥 How to Download / Install
1. Click the green **Code** button at the top right of this repository.
2. Select **Download ZIP** and extract the folder on your computer.
   *(For Git users: `git clone https://github.com/iqbaldwiansyah/Speedometer-FH6.git`)*
3. Open the extracted folder.

### 🚀 How to Use
1. **Prerequisites:** Double-click **`install_requirements.bat`**. This will check for Python and install the required library (`websockets`). *(Note: Ensure you check "Add Python to PATH" if installing Python for the first time).*
2. **Run the Relay:** Double-click **`start.bat`** to start receiving data from the game. Leave the console window open while playing.
3. **In-Game Settings:** Open Forza Horizon 6 -> **Settings -> HUD and Gameplay -> Data Out**:
   - Data Out: **On**
   - Data Out IP Address: **127.0.0.1**
   - Data Out IP Port: **7777**

### 🎨 Live Configurator & Custom Themes
1. Run **`start_configurator.bat`** (it will open a web browser automatically).
2. Adjust colors, fonts, and spacings, then hit **Save**.
3. **Creating Your Own Theme:** 
   - Create a new folder inside the `themes/` directory (e.g., `themes/My_Theme`).
   - Add your background designs named `speedometer.png` and `tacho.png` (recommended size *600x600 px*, transparent `.png`).
   - Copy `config.js` and `description.json` from another theme (e.g., `themes/default/`) into your new folder. Edit `description.json` to change the theme name.
   - Your new theme will automatically appear in the Live Configurator!

### 📹 Streaming Software Integration
- **OBS Studio:** Add a new Source -> **Browser**. Check the **Local file** box, then browse for `overlay_transparent.html`. Clear the *Custom CSS* field to ensure transparency. Set the resolution (e.g., 800x400).
- **TikTok Live Studio:** Add a **Web Link** (select local file if supported), or open `overlay_transparent.html` in Google Chrome and add it as a **Window Capture** source.

### 🛠️ Developer Guide & Contributing
Want to add features, fix bugs, or expand this script? Pull Requests are highly welcome!
- **Data Flow (Architecture):** 
  `Forza Horizon 6 (UDP 7777)` ➡️ `forza_relay.py` (Unpacks the UDP struct) ➡️ `WebSocket (ws://localhost:8765)` ➡️ `overlay_transparent.html` (Renders UI via JS/CSS).
- **Tweaking the UI Editor:** If you add new inputs to `editor.html`, make sure the variable is captured in the `gatherConfig()` function and properly handled inside `parseAndApplyConfig()`.
- **Relay Script:** The Forza Horizon UDP packet structure (V1/V2) is rigid. If you want to expose new telemetry data (like suspension travel or tire temps), you'll need to modify the struct unpacking logic in `forza_relay.py`.
