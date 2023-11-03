import requests
import json

URL = "http://127.0.0.1:8000/product_api/"

headers = {'content-type':'application/json'}

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
        'name': 'Black-pen',
        'price': 151,
        'des': 'Nice',
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def update_data():
    data = {
        "id": 25,
        "name": "Eoni",
        "roll": 151,
        "city": "Mymensingh",
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

def delete_data(id):
    data = { "id": id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

get_data(1)
# post_data()
# update_data()
# delete_data(15)
