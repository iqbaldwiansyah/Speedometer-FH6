import http.server
import socketserver
import json
import webbrowser
import threading
import os
import subprocess

PORT = 8080

class ConfigHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        if self.path == '/themes_list':
            themes = []
            if os.path.exists('themes'):
                for item in os.listdir('themes'):
                    if os.path.isdir(os.path.join('themes', item)):
                        desc_path = os.path.join('themes', item, 'description.json')
                        name = item
                        if os.path.exists(desc_path):
                            try:
                                with open(desc_path, 'r', encoding='utf-8') as f:
                                    data = json.load(f)
                                    name = data.get('nama', item)
                            except:
                                pass
                        themes.append({"id": item, "name": name})
                        
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(themes).encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            config = json.loads(data)
            
            tema = config.get("tema_aktif", "default")
            
            # 1. Simpan tema_aktif ke root config.js
            with open('config.js', 'w', encoding='utf-8') as f:
                f.write(f'const OVERLAY_CONFIG = {{\n    tema_aktif: "{tema}"\n}};\n')
            
            # 2. Simpan warna ke themes/{tema}/config.js
            js_content = "var THEME_CONFIG = {\n"
            for k, v in config.items():
                if k == "tema_aktif": continue
                val_escaped = str(v).replace('"', '\\"')
                js_content += f'    {k}: "{val_escaped}",\n'
            js_content += "};\n"
            
            theme_path = os.path.join('themes', tema, 'config.js')
            with open(theme_path, 'w', encoding='utf-8') as f:
                f.write(js_content)
                
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            
        elif self.path == '/run_relay':
            if os.name == 'nt':
                subprocess.Popen(['start', 'cmd', '/k', 'python', 'forza_relay.py'], shell=True)
            else:
                subprocess.Popen(['python', 'forza_relay.py'])
                
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            

        else:
            self.send_response(404)
            self.end_headers()

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ConfigHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    print("Menjalankan Live Web Configurator di latar belakang...")
    print(f"Buka http://localhost:{PORT}/editor.html di browser Anda.")
    
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    webbrowser.open(f'http://localhost:{PORT}/editor.html')
    
    input("Tekan Enter di sini untuk menutup Configurator...\n")
