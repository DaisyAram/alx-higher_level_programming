#!/bin/bash
# takes in a URL &  displays all HTTP methods the server will accept.
curl -sX OPTIONS -i $1 | grep "Allow"
