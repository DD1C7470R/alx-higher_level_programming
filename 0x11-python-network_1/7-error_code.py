#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code > 399:
        print(f'Error code: {res.status_code}')
    else:
        print(res.text)
