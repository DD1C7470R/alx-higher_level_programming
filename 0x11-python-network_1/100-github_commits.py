#!/usr/bin/python3
""" Python script that takes your GitHub credentials and displays your id """
import sys
from security import safe_requests

if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    commits = safe_requests.get(url)
    for ele in commits.json()[:10]:
        name = ele.get('commit').get('author').get('name')
        print(f"{ele.get('sha')}: {name}")
