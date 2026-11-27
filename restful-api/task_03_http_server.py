from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class my_server(BaseHTTPRequestHandler):

    def _send_message(self):
        message = b"Hello, this is a simple API!"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message)

    def _send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


    def do_GET(self):
        if self.path == "/":
            self._send_message()
        elif self.path == "/poogie":
            self._send_json({"You found the greatest of them all": "Poogie"})
        elif self.path == "/data":
            self._send_json({"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/status":
            self._send_json({"status": "OK"})
        elif self.path == "/info":
            self._send_json({"version": "1.0", "description": "A simple API built with http.server"})
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), my_server)
    print("Server running on http://localhost:8000")
    server.serve_forever()
