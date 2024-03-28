#!/usr/bin/python3
#  script that takes in a URL and an email, sends a POST request to
# the passed URL with the email as a parameter, and displays the body
# of the response (decoded in utf-8)
import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <EMAIL>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode()

with urllib.request.urlopen(url, data) as response:
    html = response.read()
    print(html.decode('utf-8'))
