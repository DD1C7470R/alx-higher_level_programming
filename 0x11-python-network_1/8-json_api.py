#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys


if __name__ == '__main__':
    body ={}
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    body['q'] = letter
    res = requests.post('http://0.0.0.0:5000/search_user', data=body)
    if res.headers.get('content-type') == 'application/json':
        data = res.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
