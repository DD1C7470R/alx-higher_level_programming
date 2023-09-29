#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL """
# script that takes in a URL, sends a request to the URL and
# displays the body of the response
import urllib.request

if __name__ == "__main__":

    try:
        with urllib.request.urlopen(
                'https://alx-intranet.hbtn.io/status'
                ) as response:
            content = response.read()
            print("Body response:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", content.decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
