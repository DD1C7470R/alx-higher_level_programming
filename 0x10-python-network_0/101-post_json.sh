#!/bin/bash
# sends a request to URL, and displays the size of the body of the response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
