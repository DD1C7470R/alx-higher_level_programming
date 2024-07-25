#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    response = requests.get(
        f"https://api.github.com/users/{user}",
        headers={"Authorization": f"token {pwd}"},
    timeout=60)
    print(response.json().get("id"))
