#!/bin/bash
# sends a request to URL, and displays the size of the body of the response
curl -s -I -X GET "$1" | grep "Allow:" | cut -d' ' -f2-
