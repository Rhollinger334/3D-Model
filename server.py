#!/usr/bin/env python3
"""Simple HTTP server for the Widowmaker 3D Model Viewer."""
import http.server
import os

PORT = 8080

os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPServer if hasattr(http.server, 'SimpleHTTPServer') else http.server.SimpleHTTPRequestHandler
print(f"Serving Widowmaker 3D Viewer at http://localhost:{PORT}")
print("Press Ctrl+C to stop.")

httpd = http.server.HTTPServer(("0.0.0.0", PORT), http.server.SimpleHTTPRequestHandler)
httpd.serve_forever()
