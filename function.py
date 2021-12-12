import json
import requests
import random as rd


def parser(file):
    with open(file, "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data


def requestPOST(url, headers, data):
    r = requests.post(url,
                      headers=headers,
                      json=data)
    print("Status code:", r.status_code)
    if len(r.text) > 0:
        print("Text responce:", r.json())


def random_id_pallet(num):
    word_and_number = "QWERTYUIOPADFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    pallet_id = ""
    for i in range(num):
        pallet_id = pallet_id + rd.choice(word_and_number)
    return pallet_id


