import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.lstrip("/")
        if path == "":
            path = "index.html"

        if os.path.exists(path):
            self.send_response(200)
            if path.endswith(".html"):
                self.send_header("Content-type", "text/html")
            elif path.endswith(".css"):
                self.send_header("Content-type", "text/css")
            else:
                self.send_header("Content-type", "application/octet-stream")
            self.end_headers()

            with open(path, "rb") as file:
                self.wfile.write(file.read())
            print(f"✅ Gesendet: {path}")
        else:
            self.send_error(404, f"Datei nicht gefunden: {path}")  # <<< kein Emoji mehr!
            print(f"❌ Datei nicht gefunden: {path}")  # <<< hier darf's ruhig knallen 😈

if __name__ == "__main__":
    print("🌐 Elias Webserver läuft auf http://localhost:8080 ...")
    server = HTTPServer(("localhost", 8080), MyHandler)
    server.serve_forever()
