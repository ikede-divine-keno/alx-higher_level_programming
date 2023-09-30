#!/usr/bin/python3
""" Write a Python script that takes in a
URL and an email, sends a POST"""
import sys
import urllib
from urllib import parse, request

if __name__ == "__main__":
    jsondata = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(jsondata).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        decoded_data = response.read().decode('utf-8')
        print(f"{decoded_data}")
