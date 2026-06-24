# Forza Horizon 6 — Overlay Speedometer & Tachometer

Dua gauge analog (speedometer di kiri, tachometer/RPM di kanan), masing-masing
bisa dipasangi gambar custom sebagai latar dial.

## 1. Jalankan relay (sekali tiap mau main)
```
pip install websockets
python forza_relay.py
```
Secara default relay mendengar UDP di port **7777** dan menyiarkan ke
WebSocket di **ws://localhost:8765**.

## 2. Atur Data Out di game
Settings → HUD and Gameplay → Data Out:
- Data Out: **On**
- Data Out IP Address: **127.0.0.1**
- Data Out IP Port: **7777** (harus sama dengan `UDP_PORT` di forza_relay.py)

## 3. Buka overlay
Double-click `forza_overlay.html` untuk membukanya di browser. Ia otomatis
mencoba konek ke `ws://localhost:8765`:
- Kalau relay sudah jalan & game sedang dikemudikan → jarum bergerak sesuai data asli.
- Kalau belum konek → overlay jalan dalam **mode demo** (simulasi) supaya tampilannya tetap bisa dilihat.

Mau ganti alamat/port WebSocket? Klik tombol **⚙ Koneksi** di pojok kiri atas.

## 4. Pasang gambar dial custom
Klik ikon 🖼 di pojok kanan-bawah masing-masing gauge untuk upload gambar
sebagai latar dial. Jarum, angka, dan tick mark tetap berfungsi normal di
atas gambar tersebut. Klik ✕ di pojok kiri-bawah untuk menghapus gambar dan
kembali ke tampilan default.

## 5. Mode transparan (untuk OBS / Tiktok Studio)
Background overlay ini secara default sudah otomatis transparan tembus pandang tanpa perlu dicentang. Cocok dipakai langsung sebagai web/browser capture overlay di atas game.

## Catatan teknis
- Skala speedometer: 0–320 km/h (tetap).
- Skala tachometer otomatis menyesuaikan ke RPM maksimum mobil yang sedang
  dipakai (dibaca live dari field `EngineMaxRpm`), termasuk zona redline
  (~85%–100% dari RPM maksimum).
- Field gear `0` ditampilkan sebagai "N" (netral); kalau ingin logika
  netral/reverse yang lebih akurat untuk mobil tertentu, sesuaikan di bagian
  `applyTelemetry()` pada forza_overlay.html.
- Mau ubah port UDP/WS relay? Edit `UDP_PORT` / `WS_PORT` di forza_relay.py.
