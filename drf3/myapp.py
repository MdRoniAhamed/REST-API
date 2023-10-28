import requests
import json

URL = " http://127.0.0.1:8000/student_api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
        'name': 'Roni',
        'roll': 105,
        'city': 'Khulna',
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


def update_data():
    data = {
        "id": 3,
        "name": "Emran",
        "roll": 115,
        "city": "Dhaka",
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

def delete_data(id):
    data = { "id": id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data()
post_data()
# update_data()
delete_data(15)
