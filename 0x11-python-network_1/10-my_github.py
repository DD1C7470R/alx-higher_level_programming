#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys


if __name__ == '__main__':
    headers = {}
    username = sys.argv[1]
    headers['Authorization'] = f"token {sys.argv[2]}"

    res = requests.get(f'https://api.github.com/users/{username}', headers)
    content = res.json()
    print(content.get('id'))
