#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys


if __name__ == '__main__':
    body = {}
    body['email'] = sys.argv[2]
    res = requests.post(sys.argv[1], data = body)
    content = res
    print(content.text)
