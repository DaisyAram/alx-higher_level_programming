#!/usr/bin/bash
# takes in a URL, send a request & display the size of the body of the response
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
