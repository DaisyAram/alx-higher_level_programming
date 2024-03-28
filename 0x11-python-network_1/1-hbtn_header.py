#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL and displays
# the value of the X-Request-Id variable found in the header of the response.
import sys
import urllib.request
url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')

    if header is not None:
        print(header)
    else:
        print("X-Request-Id not found in response headers")
