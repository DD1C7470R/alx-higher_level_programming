#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import sys
from security import safe_requests


if __name__ == '__main__':
    res = safe_requests.get(sys.argv[1])
    if res.status_code > 399:
        print(f'Error code: {res.status_code}')
    else:
        print(res.text)
