#!/usr/bin/bash
# takes in a URL, send a request & display the size of the body of the response
curl -s "$1" | wc -c
