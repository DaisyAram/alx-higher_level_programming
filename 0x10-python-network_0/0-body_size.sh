#!/bin/bash
# takes a URL as an argument, sends a request & displays the body response size
curl -s $1 | wc -c
