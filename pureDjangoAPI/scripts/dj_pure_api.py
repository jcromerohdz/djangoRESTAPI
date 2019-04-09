import json
import requests


BASE_URL = "http://127.0.0.1:7070/"

ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    print(r.status_code)
    print(type(json.dumps(data)))
    for obj in data:
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
    return data


print(get_list())
