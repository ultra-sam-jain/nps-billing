#!/usr/bin/env python3
"""
NPS Portal — local dev server
Run: python server.py
Open: http://localhost:8000
"""

import http.server
import socketserver
import os

PORT = 8000
BASE = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE, **kwargs)

    def log_message(self, fmt, *args):
        print(f"  {self.address_string()}  {fmt % args}")


print(f"NPS Portal running → http://localhost:{PORT}")
print(f"  Home     : http://localhost:{PORT}/")
print(f"  Calculator: http://localhost:{PORT}/apps/nps-calculator.html")
print("Press Ctrl+C to stop.\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
