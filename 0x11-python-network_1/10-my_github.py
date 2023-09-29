#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys


if __name__ == '__main__':
    headers = {}
    username = sys.argv[1]
    headers['X-GitHub-Api-Version'] = "2022-11-28"
    headers['Accept'] = "application/vnd.github+json"
    headers['Authorization'] = f"token {sys.argv[2]}"

    res = requests.get(f'https://api.github.com/users/{username}', headers)
    if res.status_code == 200:
        content = res.json()
        print(content.get('id'))
    else:
        print('None')
