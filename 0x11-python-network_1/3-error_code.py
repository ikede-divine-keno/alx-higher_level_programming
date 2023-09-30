#!/usr/bin/python3
""" Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the
response (decoded in utf-8)."""
import sys
import urllib
from urllib import request, error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            decoded_data = response.read().decode('utf-8')
            print(f"{decoded_data}")
    except error.HTTPError as e:
        print('Error code:', e.code)
