"""
Forza Horizon 6 UDP -> WebSocket relay
---------------------------------------
Mendengarkan paket "Data Out" UDP dari Forza Horizon 6, lalu meneruskan
field yang relevan (speed, RPM, gear) ke browser via WebSocket supaya bisa
dibaca oleh forza_overlay.html.

Install dependensi:
    pip install websockets

Jalankan:
    python forza_relay.py

Lalu di game: Settings > HUD and Gameplay > Data Out
    Data Out        : On
    IP Address      : 127.0.0.1
    Port            : 7777   (samakan dengan UDP_PORT di bawah)
"""

import asyncio
import json
import socket
import struct
import os

import websockets

UDP_PORT = 7777     # harus sama dengan "Data Out IP Port" di game
WS_PORT = 8765      # port yang dibaca forza_overlay.html

clients = set()
CAR_DB = {}

def load_car_db():
    global CAR_DB
    try:
        with open('Forza20620Ordinals.json', 'r', encoding='utf-8') as f:
            raw_db = json.load(f)
            # Invert the dictionary from {"CarName": "Ordinal"} to {"Ordinal": "CarName"}
            CAR_DB = {str(v): k for k, v in raw_db.items()}
        print(f"[relay] Berhasil memuat database mobil ({len(CAR_DB)} mobil).")
    except Exception as e:
        print(f"[relay] Gagal memuat Forza20620Ordinals.json: {e}")

load_car_db()


last_known_car = {
    "ordinal": 0,
    "class": 0,
    "pi": 0,
    "name": "Menunggu Telemetry..."
}

def parse_packet(data: bytes) -> dict:
    global last_known_car
    is_race_on = struct.unpack_from("<i", data, 0)[0]
    max_rpm = struct.unpack_from("<f", data, 8)[0]
    cur_rpm = struct.unpack_from("<f", data, 16)[0]
    speed_ms = struct.unpack_from("<f", data, 256)[0]
    car_ordinal = struct.unpack_from("<i", data, 212)[0]
    car_class = struct.unpack_from("<i", data, 216)[0]
    car_pi = struct.unpack_from("<i", data, 220)[0]
    gear = struct.unpack_from("<B", data, 319)[0]
    
    if car_ordinal != 0:
        car_name = CAR_DB.get(str(car_ordinal), f"Mobil tidak dikenal (ID {car_ordinal})")
        last_known_car["ordinal"] = car_ordinal
        last_known_car["class"] = car_class
        last_known_car["pi"] = car_pi
        last_known_car["name"] = car_name
    else:
        car_ordinal = last_known_car["ordinal"]
        car_class = last_known_car["class"]
        car_pi = last_known_car["pi"]
        car_name = last_known_car["name"]

    return {
        "on": bool(is_race_on),
        "rpm": cur_rpm,
        "maxRpm": max_rpm,
        "speedKmh": speed_ms * 3.6,
        "gear": gear,
        "carOrdinal": car_ordinal,
        "carName": car_name,
        "carClass": car_class,
        "carPI": car_pi,
    }


async def udp_listener():
    loop = asyncio.get_running_loop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", UDP_PORT))
    sock.setblocking(False)
    print(f"[relay] Mendengarkan telemetry UDP di port {UDP_PORT} ...")

    while True:
        data = await loop.sock_recv(sock, 512)
        if len(data) < 320:
            continue
        try:
            payload = json.dumps(parse_packet(data))
        except struct.error:
            continue
        dead = []
        for ws in clients:
            try:
                await ws.send(payload)
            except Exception:
                dead.append(ws)
        for ws in dead:
            clients.discard(ws)


async def handler(websocket):
    clients.add(websocket)
    print(f"[relay] Overlay terhubung ({len(clients)} klien aktif)")
    try:
        async for _ in websocket:
            pass  # overlay tidak mengirim apa pun, cukup dengarkan saja
    finally:
        clients.discard(websocket)
        print(f"[relay] Overlay terputus ({len(clients)} klien aktif)")


async def main():
    async with websockets.serve(handler, "localhost", WS_PORT):
        print(f"[relay] WebSocket siap di ws://localhost:{WS_PORT}")
        await udp_listener()


if __name__ == "__main__":
    asyncio.run(main())