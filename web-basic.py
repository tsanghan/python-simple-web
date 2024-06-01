# Simple web application with default modules
from http.server import BaseHTTPRequestHandler, HTTPServer

class ExampleHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self._set_response()
        self.wfile.write("Hello World!".encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8080)
    print("Hosting on http://localhost:8080")
    httpd = HTTPServer(server_address, ExampleHandler)
    httpd.serve_forever()
