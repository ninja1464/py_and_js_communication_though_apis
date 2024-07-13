import http.server
import socketserver
import urllib.parse

PORT = 3000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query = urllib.parse.parse_qs(parsed_path.query)
        
        if path == "/data":
            a = query.get('a', [''])[0]
            b = query.get('b', [''])[0]
            
            # Print received data
            print(f"GET request received with parameters: a={a}, b={b}")
            
            try:
                # Calculate the sum of a and b
                result = int(a) + int(b)
                response = f"Result: {result}"
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(response.encode())
            except ValueError:
                self.send_response(400)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Invalid input")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
