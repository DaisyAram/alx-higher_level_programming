#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays response body
curl -sX GET $1  -L 200
