#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import sys
from security import safe_requests


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    response = safe_requests.get(
        f"https://api.github.com/users/{user}",
        headers={"Authorization": f"token {pwd}"},
    )
    print(response.json().get("id"))
