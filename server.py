import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import webbrowser
import mimetypes
import json
import string

# Characters for Base62 encoding (lowercase, uppercase, digits)
BASE62_ALPHABET = string.ascii_letters + string.digits
BASE62_ALPHABET_LENGTH = len(BASE62_ALPHABET)

# Simple in-memory mapping for URLs
shortened_urls = {}

# Function to convert a number into a Base62 string
def encode_base62(num):
    if num == 0:
        return BASE62_ALPHABET[0]
    
    base62_str = []
    while num:
        base62_str.append(BASE62_ALPHABET[num % BASE62_ALPHABET_LENGTH])
        num //= BASE62_ALPHABET_LENGTH
    return ''.join(reversed(base62_str))

# Function to convert a Base62 string back to a number
def decode_base62(base62_str):
    num = 0
    for char in base62_str:
        num = num * BASE62_ALPHABET_LENGTH + BASE62_ALPHABET.index(char)
    return num

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in file_map:
            file_name = file_map[self.path]
            content_type = self.get_content_type(file_name)
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            with open(file_name, 'rb') as f:
                self.wfile.write(f.read())
        
        elif self.path.startswith('/s/'):
            short_id = self.path[len('/s/'):]
            full_url = shortened_urls.get(short_id)
            if full_url:
                self.send_response(302)  # Redirect
                self.send_header('Location', full_url)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'Short URL not found.')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        if self.path == '/shorten':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            original_url = data.get('url', '')
            
            if not original_url.startswith(('http://', 'https://')):
                original_url = 'http://' + original_url  # auto-add http:// if missing
            
            # Generate a unique hash for the URL and encode it in Base62
            short_id = encode_base62(abs(hash(original_url)) % 1000000)
            shortened_urls[short_id] = original_url

            short_url = f"http://localhost:8000/s/{short_id}"
            response = {'shortened_url': short_url}
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def get_content_type(self, file_name):
        if file_name.endswith('.js'):
            return 'application/javascript'
        elif file_name.endswith('.css'):
            return 'text/css'
        return mimetypes.guess_type(file_name)[0] or 'application/octet-stream'

# Map for static files (like before)
file_map = {
    '/': 'url-shortener/index.html',
    '/style.css': 'url-shortener/style.css',
    '/script.js': 'url-shortener/script.js',
}

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on http://localhost:8000')
    webbrowser.open('http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
    # To run the server, execute this script. It will open a web browser to the URL shortener interface.
    # You can then enter a URL to shorten it. The shortened URL will be displayed on the page.