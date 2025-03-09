# server.py

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

#  compatible Koyeb (fallback 8080 for local dev)
PORT = int(os.environ.get("PORT", 8080))

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Ashi Bot is running...")

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=PORT):
    server_address = ("0.0.0.0", port)
    httpd = server_class(server_address, handler_class)
    print(f"✅ Server is running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
