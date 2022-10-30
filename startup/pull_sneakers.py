import requests
import os
import json
import time

URL = "https://sell.flightclub.com/api/public/search?page=1&perPage=20&query={sku}"
SKUS = ["dd1391","ct8012","555088","dj5423","dm0029"]

def main():
    setup()
    sneaker_data = get_sneaker_data()
    download_sneaker_img(sneaker_data)
    dict_to_json_file(f'sneakers{os.sep}data{os.sep}sneakers.json',sneaker_data)

def get_sneaker_data():
    sneaker_data = {'sneakers':[]}
    for sku in SKUS:
        r = requests.get(URL.format(sku=sku))
        data = json.loads(r.content)
        for result in data['results']:
            sneaker_data['sneakers'].append(result)
    return sneaker_data

def download_sneaker_img(sneaker_data):
    for sneaker in sneaker_data['sneakers']:
        print(sneaker['imageUrl'])
        sneaker['imageFile'] = sneaker['imageUrl'].split('/')[-1]
        if os.path.exists(f'sneakers{os.sep}img{os.sep}' + sneaker['imageFile']) == False:
            with open(f'sneakers{os.sep}img{os.sep}' + sneaker['imageFile'], 'wb') as f:
                im = requests.get(sneaker['imageUrl'])
                f.write(im.content)
            time.sleep(1)

def dict_to_json_file(filename,sneaker_data):
    with open(filename, 'w') as f:
        json.dump(sneaker_data,f)


def create_path(path):
    if os.path.exists(path) == False:
        os.mkdir(path)

def setup():
    paths = [f'sneakers{os.sep}', f'sneakers{os.sep}img{os.sep}', f'sneakers{os.sep}data{os.sep}']
    for path in paths:
        create_path(path)

if __name__ == "__main__":
    main()
