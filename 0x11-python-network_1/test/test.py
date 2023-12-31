#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 2:
        param = {"q": sys.argv[1]}
    else:
        param = {"q": ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=param)
    try:
        resp = response.json()
        if resp:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
