#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL """
# script that takes in a URL, sends a request to the URL and
# displays the body of the response
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {}
    data['email'] = sys.argv[2]

    try:
        parsed_data = urllib.parse.urlencode(data).encode('ascii')
        with urllib.request.urlopen(url, parsed_data) as response:
            content = response.read()
            print(content.decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
