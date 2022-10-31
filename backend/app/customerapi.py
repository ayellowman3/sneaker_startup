from http.server import HTTPServer, BaseHTTPRequestHandler

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        output = ''
        output += '<html><body>'
        output += '<p>Not added to cart</p>'
        output += '</body></html>'
        self.wfile.write(output.encode())


    def do_POST(self):
        if self.path.endswith('/cart'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            output = ''
            output += '<html><body>'
            output += '<p>Added to cart</p>'
            output += '</body></html>'


def main():
    PORT = 8000
    server_address = (0.0.0.0, PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
