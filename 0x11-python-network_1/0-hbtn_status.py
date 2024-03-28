#!/usr/bin/python3
""" python script that fetches
https://alx-intranet.hbtn.io/status using urllib
"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print(f'Body response:')
        print(f'    - type: <\'{type(html)}\'')
        print(f'    - content: {repr(html)}')
        print(f'    - utf8 content: {html.decode()}')
