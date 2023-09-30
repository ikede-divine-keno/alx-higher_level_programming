#!/usr/bin/python3
""" script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    response = requests.post(url, data=data)
    try:
        validjson = response.json()
        if validjson == {}:
            print('No result')
        else:
            id = validjson.get('id')
            name = validjson.get('name')
            print(f"[{id}] {name}")
    except ValueError:
        print('Not a valid JSON')
