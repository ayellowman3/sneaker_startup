from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        output = ''
        output += '<html><body>\n'
        output += '<a href="127.0.0.1:8000">link text</a>\n'
        output += '<div class="grid-container" style="display: grid; grid-gap: 20px; grid-template-columns: auto auto auto auto;">\n'
        f = open(f'sneakers{os.sep}data{os.sep}sneakers.json')
        data = json.load(f)
        counter = 0
        for sneaker in data['sneakers']:
            output += '<div class="grid-item" style="height: auto; width: 250px;" >\n'
            output += f'<img alt="sneakers" src="{sneaker["imageUrl"]}" style="width: 204px; height: 145px;">\n'
            output += f'<p>{sneaker}</p>\n'
            output += f'<p id="{sneaker["name"]}" onclick="myFunction' + str(counter) + '()">Add to Cart</p>\n'
            output += '<script>\n'
            output += 'function myFunction' + str(counter) + '() {\n'
            counter += 1
            output += 'let xhr = new XMLHttpRequest();'
            output += f'xhr.open("GET", "http://0.0.0.0:8000/sneakers/{sneaker["id"]}");'
            output += 'xhr.send();'
            output += f'document.getElementById("{sneaker["name"]}").innerHTML = "Added to Cart";\n'
            output += '}\n'
            output += '</script>\n'
            output += '</div>\n'
        f.close()
        output += '</div>\n'
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
