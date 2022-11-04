from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json
import requests

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            do_homepage(self)
        elif self.path == '/cart':
            do_cart(self)
        elif self.path == '/history':
            do_history(self)

def do_homepage(self):
    self.send_response(200)
    self.send_header('content-type', 'text/html')
    self.end_headers()

    output = ''
    output += '<html><body>\n'
    output += '<a href="http://0.0.0.0:9000/cart">cart</a>'
    output += '<a href="http://0.0.0.0:9000/history">cart</a>'
    output += '<div class="grid-container" style="display: grid; grid-gap: 20px; grid-template-columns: auto auto auto auto;">\n'

    url = 'http://backend:8000/history'
    response = requests.get(url)
    data = json.loads(response.json())
    ids = data["ids"]

    f = open(f'sneakers{os.sep}data{os.sep}sneakers.json')
    data = json.load(f)

    counter = 0
    for sneaker in data['sneakers']:
        if str(sneaker["id"]) not in ids:
            output += '<div class="grid-item" style="height: auto; width: 250px;" >\n'
            output += f'<img alt="sneakers" src="{sneaker["imageUrl"]}" style="width: 204px; height: 145px;">\n'
            output += f'<p>{sneaker["name"]}</p>\n'
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

def do_cart(self):
    self.send_response(200)
    self.send_header('content-type', 'text/html')
    self.end_headers()

    output = ''
    output += '<html><body>\n'
    output += '<a href="http://0.0.0.0:9000/">home</a>'
    output += '<div class="grid-container" style="display: grid; grid-gap: 20px; grid-template-columns: auto auto auto auto;">\n'

    url = 'http://backend:8000/cart'
    response = requests.get(url)
    data = json.loads(response.json())
    ids = data["ids"]

    f = open(f'sneakers{os.sep}data{os.sep}sneakers.json')
    data = json.load(f)

    for sneaker in data['sneakers']:
        if str(sneaker["id"]) in ids:
            output += '<div class="grid-item" style="height: auto; width: 250px;" >\n'
            output += f'<img alt="sneakers" src="{sneaker["imageUrl"]}" style="width: 204px; height: 145px;">\n'
            output += f'<p>{sneaker["name"]}</p>\n'
            output += '</div>\n'

    f.close()

    output += '</div>\n'
    if len(ids) == 0:
        output += f'<p>Cart is empty</p>\n'
    else:
        output += f'<p id="checkout" onclick="checkout()">Checkout</p>\n'
        output += '<script>\n'
        output += 'function checkout() {\n'
        output += 'let xhr = new XMLHttpRequest();'
        output += f'xhr.open("POST", "http://0.0.0.0:8000/checkout");'
        output += 'xhr.send();'
        output += f'document.getElementById("{sneaker["name"]}").innerHTML = "Added to Cart";\n'
        output += '}\n'
        output += '</script>\n'

    output += '</body></html>'
    self.wfile.write(output.encode())

def do_history(self):
    self.send_response(200)
    self.send_header('content-type', 'text/html')
    self.end_headers()

    output = ''
    output += '<html><body>\n'
    output += '<p>Order History</p>'
    output += '<a href="http://0.0.0.0:9000/">home</a>'
    output += '<a href="http://0.0.0.0:9000/cart">cart</a>'
    output += '<div class="grid-container" style="display: grid; grid-gap: 20px; grid-template-columns: auto auto auto auto;">\n'

    url = 'http://backend:8000/history'
    response = requests.get(url)
    data = json.loads(response.json())
    ids = data["ids"]

    f = open(f'sneakers{os.sep}data{os.sep}sneakers.json')
    data = json.load(f)

    for sneaker in data['sneakers']:
        if str(sneaker["id"]) in ids:
            output += '<div class="grid-item" style="height: auto; width: 250px;" >\n'
            output += f'<img alt="sneakers" src="{sneaker["imageUrl"]}" style="width: 204px; height: 145px;">\n'
            output += f'<p>{sneaker["name"]}</p>\n'
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
