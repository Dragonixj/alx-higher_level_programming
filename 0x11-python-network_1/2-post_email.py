#!/usr/bin/python3
"""Script sends a POST request and displayes the 
body of the response
"""
from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    url = argv[2]
    values = {"email": argv[2]}

    data = parse.urlencode(values)
    data = data.encode("ascii")
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
