#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status
- uses urlib package
- must use with statement
"""


import urllib.request

if __name__ == '__main__':

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
