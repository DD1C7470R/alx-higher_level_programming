#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    content = res
    print("Body response:")
    print("\t- type:", type(content.text))
    print("\t- content:", content.text)
