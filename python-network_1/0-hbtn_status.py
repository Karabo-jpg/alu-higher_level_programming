#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using the urllib package."""

import urllib.request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    # Create a request with a User-Agent header
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
