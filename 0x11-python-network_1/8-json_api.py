#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests

if __name__ == "__main__":
    try:
        param = {"q": sys.argv[1]}
    except IndexError:
        param = {"q": ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=param)
    resp = response.json()
    try:
        if resp:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
