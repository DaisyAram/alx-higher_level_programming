#!/usr/bin/python3
"""A script that takes in a URL,sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""


import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
     url = sys.argv[1]
     request = urllib.request.Request(url)
     try:
        with request.urlopen(request) as r:
            print(r.read().decode('ascii'))
    except error.HTTPError as err:
        print('Error code:{}'.format(err.code)
