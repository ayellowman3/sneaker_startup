from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        output = ''
        output += '<html><body>'
        output += '<a href="127.0.0.1:8000">link text</a>'
        output += '<div class="grid-container" style="display: grid; grid-gap: 20px; grid-template-columns: auto auto auto auto;">'
        f = open(f'sneakers{os.sep}data{os.sep}sneakers.json')
        data = json.load(f)
        for sneaker in data['sneakers']:
            output += '<div class="grid-item" style="height: auto; width: 250px;" >'
            output += f'<img alt="{sneaker["name"]}" src="{sneaker["imageUrl"]}" style="width: 204px; height: 145px;">'
            output += f'<p>{sneaker}</p>'
            output += '</div>'
        f.close()
        output += '</div>'
        output += '</body></html>'
        self.wfile.write(output.encode())

def main():
    PORT = 9000
    server_address = ('0.0.0.0', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
