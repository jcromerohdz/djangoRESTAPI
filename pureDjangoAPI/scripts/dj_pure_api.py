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


def create_update():
    new_data = {
        'user':1,
        'content': "Another cool content"
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    # r = requests.post(BASE_URL + ENDPOINT, data=new_data)
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


# print(create_update())
# print(get_list())

def do_obj_update():
    new_data = {
        'content': "Some cool content updated"
    }
    # r = requests.put(BASE_URL + ENDPOINT + "1", data=new_data)
    r = requests.put(BASE_URL + ENDPOINT + "8", data= json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

def do_obj_delete():
    new_data = {
        'content': ""
    }
    # r = requests.put(BASE_URL + ENDPOINT + "1", data=new_data)
    r = requests.delete(BASE_URL + ENDPOINT + "8", data= json.dumps(new_data))
    # print(r.headers)
    # print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

print(do_obj_delete())
